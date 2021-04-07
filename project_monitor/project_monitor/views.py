import json
from django.shortcuts import redirect, render
from.common_utils import*
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict




def convert_to_datetime(firebase_timeStamp):
    python_datetime = datetime.combine(
        firebase_timeStamp.date(), firebase_timeStamp.time())
    return python_datetime.strftime("%B %d, %Y, %H:%M")

def home_page(request):
    data_ref = db.collection_group('FSA_Events').order_by("event_time", direction=firestore.Query.DESCENDING).stream()
    data = []
    for event in data_ref:
        data.append(event.to_dict())
    return render(request, template_name="home_page.html", context={"data": data})

@csrf_exempt
def ajax_live_event_data(request):
    data_ref = db.collection_group('FSA_Events').order_by("event_time", direction=firestore.Query.DESCENDING).stream()
    data = []
    for event in data_ref:
        _temp = event.to_dict()
        _temp.update({
            "event_time": convert_to_datetime(_temp['event_time']),
            "user_joined": convert_to_datetime(_temp['user_joined'])
        })
        data.append(_temp)
    return JsonResponse(data, safe=False, status=200)

@csrf_exempt
def event(request, event_id=None):
    print(request, event_id)
    if request.method=='GET':
        if event_id:
            event_data = db.collection('FSA_Events').document(event_id).get().to_dict()
            if event_data:
                return JsonResponse(event_data, safe=False, status=200)
            else:
                return JsonResponse({"msg":"Invalid even_id"}, safe=False)
        else:
            event_data_ref = db.collection_group('FSA_Events').order_by("event_time", direction=firestore.Query.DESCENDING).stream()
            event_data = []
            for event in event_data_ref:
                event_data.append(event.to_dict())
            return JsonResponse(event_data, safe=False, status=200)
    
    elif request.method=='POST':
        post_data = json.loads(request.body.decode('utf-8'))
        print(post_data)
        try:
            event_id = post_data['event_id']
            prev_data = db.collection('FSA_Events').document(event_id).set(post_data, merge=True)
            return JsonResponse({"msg":"Successfully Saved"}, safe=False, status=200)
        except:
            return JsonResponse({"msg":"Invalid Body"}, safe=False, status=500)
    
    elif request.method=='PUT':
        if event_id:
            post_data = json.loads(request.body.decode('utf-8'))
            db.collection('FSA_Events').document(event_id).set(post_data, merge=True)
            return JsonResponse({"msg":f"Successfully Updated Event: {event_id}"}, safe=False, status=200)
        else:
            try:
                post_data = json.loads(request.body.decode('utf-8'))
                db.collection('FSA_Events').document(post_data['event_id']).set(post_data, merge=True)
                return JsonResponse({"msg":f"Successfully Updated Event: {post_data['event_id']}"}, safe=False, status=200)
            except:
                return JsonResponse({"msg":"Invalid EventID"}, safe=False, status=500)

    elif request.method=='DELETE':
        if event_id:
            db.collection('FSA_Events').document(event_id).delete()
            return JsonResponse({"msg":f"Successfully Deleted Event: {event_id}"}, safe=False, status=200)
        else:
            try:
                data_event_id = json.loads(request.body.decode('utf-8'))['event_id']
                db.collection('FSA_Events').document(data_event_id).delete()
                return JsonResponse({"msg":f"Successfully Deleted Event: {data_event_id}"}, safe=False, status=200)
            except:
                return JsonResponse({"msg":"Invalid EventID"}, safe=False, status=500)
    else:
        print("else")
        return JsonResponse({"msg":"success."}, safe=False)