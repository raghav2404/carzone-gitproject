CARZONE-- A Used Car Selling Business Website---
The basic scenario of this project is, we are making a website for a car business owner who wants to list his cars on his website and allow the user to come to his site and browse through all of his latest cars and featured cars, search and filter the cars by model or price, and make some inquiries about his cars that are out for the sale.           
The project consist of Following Modules:
Home:Consist of front landing page and dislays the featured and remaining cars.Allows navigation to Contacts ,Services,Cars And About Us Page
Cars:Consist of all the cars added from the backend.User can go to individual car_detail page from here , view the pics and features of car and also make inquiry about the car.
Teams:Dispay the teams data on home page i.e ceo,director etc 
Contacts:User can send his general non car spefic queries using contact form.An email would be sent to site admin to check panel for the details
Accounts:Configure facebook and google login and smtp authentication to send mails
Admin:Django Panel is the backend of the site from where we can insert the cars data,see all the users,superuser ,their queries,social accounts connected and manage them

Postgres Database (Pg Admin) is connected to the Django App and carzone_db is db for the project
Schema created in models.py for  team,car,contact and other tables.
Crud operations can be performed on carzone_db.
After user registers or logs in using google/fb he is directed to his dashboard page which consist all the queries made by him.
The project uses following tech stack/tools:
Django  (Python Web framework which follows MVT design pattern--model view template)
PostgresSql (Rdbms)
Bootstrap (Template /frontend pages)
Heroku -- (Deployment)

I have mainly worked on backend web development in this project. it uses bootstrap template and css files for the frontend part.
I have build django apps,models(db) configured them, inquiry,contact,mail sending and login ,authenication part.Also customised backend--django admin to display data clearly.
