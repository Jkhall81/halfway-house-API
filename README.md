# halfway-house Django REST Framework API README

Welcome to this Halfway House API!  This API provides data for a halfway house company related to houses and residents in their network.  
This README will guide you through setting up and running the project, as well as provide some essential information about its dependencies and strucutre.

## Introduction

This API uses the Django REST Framework, Django, Swagger, and Oauth2.  This project has been designed to work with Docker Compose and currently uses a sqlite database for sake of simplicity.  The database can easily be switched to something else if you wish to do so.

To run this project, you will need to set up a Docker environment based on the provided 'docker-compose.yml' file.  You can clone the project's repository
from https://github.com/Jkhall81/halfway-house-API.git.

## Setting Up the Project

Follow these steps to set up the project:

1. Clone the Repository

Clone the project's repository to your local machine using the following command:

```
git clone https://github.com/Jkhall81/halfway-house-API.git
```

2. Docker Compose

Make sure you have Docker and Docker Compose installed on your system.

Build and Run the Containers

Navigate to the project directory where you cloned the repository and run the following command to build and run the containers:

```
docker-compose up --build
```

This command will start the Django development server and the SQLite database container.  The database container will also be populated with some house and resident data from the Django fixture files.

3.  Access the API

Once the containers are up and running, you can access the API at http://localhost:8000.  You can now start developing and testing your Django REST Framework API.

4. Project Structure

```
.
├── apps
│   ├── comment
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routers.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── post
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routers.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── user
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── models.py
│       ├── pagination.py
│       ├── routers.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
└── static
```

5. Documentation

This project uses Swagger.  After the project is setup visit http://localhost:8000/swagger to view all API endpoints and documentation on those endpoints!

