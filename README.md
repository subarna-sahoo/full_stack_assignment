# Full Stack Assignment: Live Event Feed & Monitor

Two Django apps that share a **Firebase Firestore** collection of user page-view events. Built as a full-stack assignment for zeza.tech.

| App | Folder | What it does |
|---|---|---|
| **Core Feeder** | `core_feeder/` | Generates realistic random page-view events (product titles scraped from a store page, random users and timestamps) and writes them to Firestore |
| **Project Monitor** | `project_monitor/` | Dashboard that polls Firestore over AJAX to show events as they arrive, plus a REST API for creating, reading, updating and deleting events |

## Setup

```bash
python3 -m venv venv && source venv/bin/activate
pip install django firebase-admin requests beautifulsoup4
```

> `requirements.txt` is a full system `pip freeze` (it includes Ubuntu packages such as `apturl` and `Brlapi`), so installing the packages above directly is simpler.

Add your Firebase service-account credentials to `firebaseConfig` in both `*/common_utils.py` files.

## Running

Run the two apps on different ports:

```bash
cd core_feeder && python3 manage.py runserver 8001        # event generator
cd project_monitor && python3 manage.py runserver 8000    # live monitor + API
```

| App | Path | Description |
|---|---|---|
| Core Feeder | `/` | Home page |
| Core Feeder | `/generate_random_event` | Create a random event in Firestore |
| Project Monitor | `/` | Live event dashboard |
| Project Monitor | `/ajax_live_event_data` | JSON feed polled by the dashboard |
| Project Monitor | `/event`, `/event/<event_id>` | REST API (below) |

---

## Events API (Project Monitor)

Base URL: `http://localhost:8000`

### GET /event
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

### GET /event/1234
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

### POST /event
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

### PUT /event/1234 · PUT /event
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
    "msg": "Successfully Updated Event: 1234"
}
```

**Code** : `500 ERROR`

```
{
    "msg": "Invalid EventID"
}
```

### DELETE /event/1234 · DELETE /event
This will DELETE an event, You can pass the `event_id` with the payload/ in the URL.

```json
{
    "event_id": "1234"
}
```

**Code** : `200 OK`
```
{
    "msg": "Successfully Deleted Event: 1234"
}
```

**Code** : `500 ERROR`

```
{
    "msg": "Invalid EventID"
}
```

## Configuration

Secrets are read from **environment variables**, so nothing sensitive lives in the code. Copy [`.env.example`](.env.example) to `.env` (it is git-ignored) or export the variables in your shell:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django `SECRET_KEY`. If unset, a random key is generated at startup (fine for local dev). |
| `DJANGO_SECRET_KEY_2` | Django `SECRET_KEY`. If unset, a random key is generated at startup (fine for local dev). for `project_monitor` |

The same values are stored as **GitHub Actions secrets** on this repo (*Settings → Secrets and variables → Actions*), so CI/CD workflows can use them as `${{ secrets.NAME }}`.
