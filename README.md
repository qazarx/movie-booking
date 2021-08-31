# Movie Booking
###By - Shantanu Singh

###About
Language: Python.

Framework: Django rest framework.

Authentication: Token based authentication.

Database: sqlLite3.

###Deployment
This application has been deployed in heroku.
To check the api mentioned below please use this url:

https://blooming-stream-87221.herokuapp.com/

###Manual Deployment
Please make sure python 3.8 is installed before proceeding. 
Follow the steps below:

1. Use the link to clone the application in local:
   
    https://github.com/qazarx/movie-booking.git
   
2. When cloning is done, open cmd in the directory where the project was cloned.
3. Install virtual environment with the command below:

     ` pip install virtualenv`
4. Creat virtual environment with the command below:

     ` virtualenv myenv`
5. Navigate to myenv/bin/activate to activate venv using cd 'folder name'.
6. Go back to the project directory using cd..
7. Run following command to install requirements:

    `pip install -r requirements.txt `
8. Run following command to run application:
   `python manage.py runserver 8000`
9. Use postman to check following api

##api list
1. To get all the movies playing in your city:
    
    `api/movie_booking/movie/?city=Delhi` GET
   

2. To get all city:

    `api/movie_booking/city/` GET


3. To get cinema with shows and show times for a cinema, we filter the data in the UI if the show is not present:

    `api/movie_booking/cinema/{cinema_id}/` GET


4. To get show's seat availability:

    `api/movie_booking/shows/{show_id}?show_seats=true` GET

   
5. To register:

    `api/account/register/` POST
   
    use POST form data as example:
   
   ` email:firstdev@gmail.com`
   
    `username:firstdev`
   
    `password:firstdev`
   
    `repeat_password:firstdev`

    this will generate user with a token, which needs to send with authenticated requests


6. To login 
    
    `api/account/login/` POST
   
    use POST form data as example:
   
   ` username:firstdev@gmail.com` (please enter email in front of username, not username, it's a bug with django )
   
    `password:firstdev`
   
    this will generate a token, which needs to send with authenticated requests
   
7. To book a ticket

   `api/movie_booking/booking/` POST

   use POST json as example

     ` {
       "cinema_seats":[2,3],
       "show":1
      }`
   
   this http request will require authorization, basically add token from login in this format

   `Authorization: Token {token}`
   
###Admin panel

1. Go to https://blooming-stream-87221.herokuapp.com/ to access admin panel to get existing data and add new data.
2. User credentials email-`admin@admin.com` password=`admin` to login

###Architecture Decision
1. Small application hence no microservices.
2. Rapid Application Development hence Django and sqlLite3.


### Notes

1. Application is stateless.
2. Service is hosted in public cloud - Heroku
3. CI/CD is implemented with heroku git, committing with this git from cli will work.

   `https://git.heroku.com/blooming-stream-87221.git`, 

   It will require my heroku login though. Will try to get it up and running from github.

4. Used python inbuilt logging.