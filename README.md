### full_stack_Assignment
zeza.tech

## Available Scripts

#### Install all dependency by
##### `pip3 install -r requirements.txt`
##### `cat requirements.txt | xargs -n 1 pip install`

#### To run the server
##### `python3 manage.py runserver`

**Hint:**
*You can host both websites with different ports*





---------------------------------------------------------------------------------------------------------------------
# APIs



## GET /event
This will return all the events.

**Code** : `200 OK`
```json
[
    {
        "event_id": "1234",
        "user_id": "1f71739dbc984cd4995b2",
        "page_tags": "\" Big",
        "page_description": "KIDS BAILEY BOW II \" Big Kids\"",
        "event_time": "2021-04-06T19:35:41.124Z",
        "user_joined": "2000-12-03T15:35:38.104Z",
        "page_title": "BAILEY BOW"
    },
    {
        "event_id": "86c308cb243a449ea7d28",
        "user_id": "43d437fe-970f-11eb-9d46-b370afd8d305",
        "event_time": "2021-04-06T19:35:38.321Z",
        "user_joined": "2014-11-01T06:58:10.752Z",
        "page_tags": "Winter",
        "page_title": "Australia Mini",
        "page_description": "Ugg Australia Mini Bailey Button Women US 6 Gray Winter Boot"
    }
 ]
```

## GET /event/1234
For a Event with ID 1234. The event information will come like this.

**Code** : `200 OK`
```json
{
    "event_id": "1234",
    "user_id": "1f71739dbc984cd4995b2",
    "page_tags": "\" Big",
    "page_description": "KIDS BAILEY BOW II \" Big Kids\"",
    "event_time": "2021-04-06T19:35:41.124Z",
    "user_joined": "2000-12-03T15:35:38.104Z",
    "page_title": "BAILEY BOW"
}
```
* If the Event ID not valid.

**Code** : `500 ERROR`
```json
{
    "msg": "Invalid even_id"
}
```



## POST /event
This will SAVE the Event as provided data from Payload
```json
{
    "event_id": "1234",
    "user_id": "1f71739dbc984cd4995b2",
    "page_tags": "Big Kids",
    "page_description": "KIDS BAILEY BOW II Big Kids\"",
    "event_time": "2021-04-06T19:35:41.124Z",
    "user_joined": "2000-12-03T15:35:38.104Z",
    "page_title": "BAILEY BOW"
}
```

**Code** : `200 OK`
```
{
    "msg": "Successfully Saved"
}
```

**Code** : `500 ERROR`

```
{
    "msg": "Invalid Body"
}
```

## PUT /event/1234
## PUT /event
This will UPDATE an event, You can pass the `event_id` with the payload/ in the URL.
```json
{
    "event_id": "1234",
    "user_id": "1f71739dbc984cd4995b2",
    "page_tags": "Big Kids Test",
    "page_description": "KIDS BAILEY BOW II Big Kids\"",
    "event_time": "2021-04-06T19:35:41.124Z",
    "user_joined": "2000-12-03T15:35:38.104Z",
    "page_title": "BAILEY BOW"
}
```

**Code** : `200 OK`
```
{
    "msg": "Successfully Updated Event: {1234}""
}
```

**Code** : `500 ERROR`

```
{
    "msg": "Invalid EventID"
}
```

## DELETE /event/1234
## DELETE /event
This will DELETE an event, You can pass the `event_id` with the payload/ in the URL.

```json
{
    "event_id": "1234",
}
```

**Code** : `200 OK`
```
{
    "msg": "Successfully Deleted Event: {1234}""
}
```

**Code** : `500 ERROR`

```
{
    "msg": "Invalid EventID"
}
```


