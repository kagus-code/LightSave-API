#  LightSave Api 

#### This an API endpoint for the LightSave, a WebApp that calculates the power consumption and cost ,  09/06/2021

#### By **Eston Kagwima**

## Description
this is an endpoint for an app that calculates power consumption of common house appliances and estimates the cost of running it for you 

This project was generated with [Django](https://docs.djangoproject.com/en/3.2/) version 3.2.3


### User stories Specification
- Register for an acoount if you are new.
- Sign in with the application to start using.
- Select a common house hold appliance and get its power consumption.
- The power consumption is displayed in dayly, monthly and yearly.
- Add a custom appliance if it is not present on the list from the DB.
- Get estimated cost for running that appliance for  dayly, monthly and yearly..

## Setup/Installation Requirements
- install Python3.9
- Clone this repository `https://github.com/kagus-code/LightSave-API`
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
    Access the different api endpoints by editing the url


## Technologies Used

- Django version 3.2.3
- Python
- Postgressql
- Django Restful api

## link to live site on heroku
https://flash-save.herokuapp.com/

## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima
