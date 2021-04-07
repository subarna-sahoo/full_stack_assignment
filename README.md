### full_stack_Assignment
##### zeza.tech

# Available Scripts

#### Install all dependency by
##### `pip3 install -r requirements.txt`

#### *To run the server*
##### `python3 manage.py runserver`

**Hint:**
*You can host both websites with different ports*



## APIs


## Success Response

**Code** : `200 OK`

**Content examples**

For a User with ID 1234 on the local database where that User has saved. The event information will come like this.

```json
{
    "id": 1234,
    "first_name": "Joe",
    "last_name": "Bloggs",
    "email": "joe25@example.com"
}
```

For a user with ID 4321 on the local database but no details have been set yet.

```json
{
    "id": 4321,
    "first_name": "",
    "last_name": "",
    "email": ""
}
```

## Notes

* If the User does not have a `UserInfo` instance when requested then one will
  be created for them.
