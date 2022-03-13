# Udacity FSND final project : Casting agency By Sara Habboush

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects.

Initializing :

```bash
python3 -m venv env
```

Activating :

```bash
source venv/bin/activate
```

### Export environment variables

Export the environment variables to your local machine by running :

```bash
source setup.sh
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter/` directory and running:

```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Create local database

Create a local database then run Database Migrations :

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Running the server

From within the `capstone/` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

## API Reference

# Error Handling :

Errors are returned as JSON objects in the following format:

```bash
{
    "success": False,
    "error": 404,
    "message":"resource not found"
}
```

# Endpoints

1. GET '/movies'

- Returns a list of movies 
- When successeful it returns 200 and the following dictionaary :
```bash
{
    "movies": [
        {
            "id": 1,
            "release_date": "1-1-2022",
            "title": "Cast away"
        },
        {
            "id": 2,
            "release_date": "2-1-2022",
            "title": "Titanic"
        }
    ],
    "success": true
```
2. POST '/movies'

- Creates a new movie in the database
- Example response:

```bash
{
    "created_movie": {
        "id": 3,
        "release_date": "3-1-2022",
        "title": "Sara"
    },
    "success": true
}
```
3. DELETE '/movies'

- Delete a movie from the database
- Example response:

```bash
{
    "success": true
    "deleted": movie.format() 
}
```
```bash
{
    "deleted_movie": {
        "id": 3,
        "release_date": "3-1-2022",
        "title": "Sara"
    },
    "success": true
}
```
4. UPDATE '/movies'

- Update a movie in the database
- Example response:

```bash
{
    "success": true
    "patched_movie": movie
}
```

5. GET '/actors'

- Returns a list of actors 
- When successeful it returns 200 and the following dictionaary :
```bash
{
    'success': True,
    'actors': actors
}
```
6. POST '/actors'

- Creates a new actor in the database
- Request Arguments: {name:string, age:string, gender:string}
- Example response:

```bash
{
    "success": True,
    "created": actor
}
```
```bash
{
    "actors": [
        {
            "age": 30,
            "gender": "Female",
            "id": 2,
            "name": "Kate Winslet"
        }
    ],
    "success": true
}
```
7. DELETE '/actors'

- Delete an actor from the database
- Request Arguments: {actor_id:integer}
- Example response:

```bash
{
    "success": true,
    "deleted": actor
}
```
8. UPDATE '/actors'

- Update an actor in the database
- Example response:

```bash
{
    "success": true,
    "patched_actor": actor
}
```

#### Authentication nad Token

Authentication is implemented using Auth0, it uses RBAC to assign permissions using roles, these are tokens you could use to access the endpoints.
Note: The tokens expires in 24 hours you can create your own tokens at [Auth0](https://auth0.com/). you would need to refelct this in auth.py
```py
AUTH0_DOMAIN = '<your auth domain>'
ALGORITHMS = ['RS256']
API_AUDIENCE = '<your api audience>'
```


### My auth0 sign in form 

[https://capstone-sara.us.auth0.com/authorize?audience=Agency&response_type=token&client_id=xeQ7CGfQmKBHK8N7V2khC3FEmX7fmcMH&redirect_uri=https://127.0.0.1:8080/login-results]


## Users in Auth0
## Roles and Permissions 

1. **Casting Assistant:**

- Can get actors and movies only

- Email: `assistant@agency.com`
- Password: **Sara241292)**


2. **Casting Director:**

- Can Get and Post actors and movies only


- Email: `director@agency.com`
- Password: **Sara241292)**


3. **Executive Producer:** 
- Can Get All permessions GET, POST, PATCH, DELETE actors and movies

- Email: `producer@agency.com`
- Password: **Sara241292)**


## Testing 

To run the tests, run
```
createdb <database_name>
python test.py
```