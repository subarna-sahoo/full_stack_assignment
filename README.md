#### full_stack_Assignment
zeza.tech

### Available Scripts

#### Install all dependency by
##### `pip3 install -r requirements.txt`

#### To run the server
##### `python3 manage.py runserver`

**Hint:**
*You can host both websites with different ports*





---------------------------------------------------------------------------------------------------------------------
## APIs



## GET /event
This will return all the events.

**Code** : `200 OK`
```json
[
    {
        "user_id": "1234",
        "page_tags": "\" Big",
        "page_description": "KIDS BAILEY BOW II \" Big Kids\"",
        "event_time": "2021-04-06T19:35:41.124Z",
        "user_joined": "2000-12-03T15:35:38.104Z",
        "event_id": "1f71739dbc984cd4995b2",
        "page_title": "BAILEY BOW"
    },
    {
        "event_time": "2021-04-06T19:35:38.321Z",
        "user_joined": "2014-11-01T06:58:10.752Z",
        "page_tags": "Winter",
        "user_id": "43d437fe-970f-11eb-9d46-b370afd8d305",
        "event_id": "86c308cb243a449ea7d28",
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
    "user_id": "1234",
    "page_tags": "\" Big",
    "page_description": "KIDS BAILEY BOW II \" Big Kids\"",
    "event_time": "2021-04-06T19:35:41.124Z",
    "user_joined": "2000-12-03T15:35:38.104Z",
    "event_id": "1f71739dbc984cd4995b2",
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
Body
```json
{
    "user_id": "1234",
    "page_tags": "\" Big",
    "page_description": "KIDS BAILEY BOW II \" Big Kids\"",
    "event_time": "2021-04-06T19:35:41.124Z",
    "user_joined": "2000-12-03T15:35:38.104Z",
    "event_id": "1f71739dbc984cd4995b2",
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
    "msg": "Invalid Head"
}
```



