#  Watch-Dog Web App

#### This an API endpoint for the watch-dog app which lets a user know whats happening in their neighbourhood,  04/06/2021

#### By **Eston Kagwima**

## Description
 this is an end point for a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

This project was generated with [Django](https://docs.djangoproject.com/en/3.2/) version 3.2.3


### User stories Specification
- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

## Setup/Installation Requirements
- install Python3.9
- Clone this repository `https://github.com/kagus-code/Tuzo-Awards.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
####  Create the Database
    - psql
    - CREATE DATABASE <name>;
####  .env file
Create .env file and paste paste the following and fill  required fields:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<name>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
    DB_HOST='127.0.0.1'
    MODE='dev'
    ALLOWED_HOSTS='*'
    DISABLE_COLLECTSTATIC=1
#### Run initial Migration
    python3.9 manage.py makemigrations <name of the app>
    python3.9 manage.py migrate
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000


## Technologies Used

- Django version 3.2.3
- Python
- Postgressql

## link to live site on heroku
https://kagus-watchdog.herokuapp.com/

## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima
