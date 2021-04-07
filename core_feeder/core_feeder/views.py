from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import uuid
import datetime
import random
from icecream import ic
from .common_utils import db
import requests_html
def home_page(request):
    return render(request, template_name="home_page.html")



def get_random_date_time():
    get_random = lambda start,end: random.randint(start,end)
    year, month, date = get_random(2000, 2021), get_random(1,12), get_random(1,27)
    hour, minute, second = get_random(1, 23), get_random(1, 59), get_random(1, 59)
    date_time_str = f"{year}-{month}-{date} {hour}:{minute}:{second}.{get_random(100,999)}"
    random_date_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    ic(random_date_obj)
    return random_date_obj

def get_random_sentence():
    import requests
    from bs4 import BeautifulSoup

    page = requests.get("https://www.newegg.com/Ugg-Australia/BrandStore/ID-59551").text
    soup = BeautifulSoup(page, "html.parser")

    results = soup.findAll("a", {"class": "item-title"})

    context = []
    for r in results:
        context.append(r.text.strip())
    try:
        page_description = context[random.randint(0,len(context)-1)]
        page_title = page_description.split()[1:random.randint(3,4)]
        page_title = (''.join(f" {word}" for word in page_title)).strip()
        page_tags = page_description.split()[-random.randint(2,3):-1]
        page_tags = (''.join(f" {word}" for word in page_tags)).strip()
    except:
        page_description = "Hanging Wall OrganizerOver The Door File Organizer by Hanging Wall File Folder Office Supplies Storage Organizer with 2 Stainless Steel HookHanging Storage Organizer Gray 2 Pack"
        page_title = "Hanging Wall Organizer"
        page_tags = "Hanging Wall"
    return page_description, page_title, page_tags


@csrf_exempt
def generate_random_event(request):
    page_description, page_title, page_tags = get_random_sentence()
    random_event_data = {
        "event_id":str(uuid.uuid4())[:25].replace("-",""),
        "event_time": datetime.datetime.now(),
        "page_title": page_title,
        "page_description": page_description,
        "page_tags": page_tags,
        "user_id": str(uuid.uuid1()),
        "user_joined": get_random_date_time()
    }
    ic(random_event_data)
    db.collection('FSA_Events').document(random_event_data['event_id']).set(random_event_data, merge=True)
    return JsonResponse(random_event_data, safe=False)
