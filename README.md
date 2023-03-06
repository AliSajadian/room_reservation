# room_reservation
### Booking room test project

![Screenshot from 2023-03-06 01-34-42](https://user-images.githubusercontent.com/47317870/222989159-c9f7eb28-b7a5-4969-9b51-4fa526cda83d.png)

### Create database
```sudo -u postgres psql

   CREATE DATABASE room_rez_db;
   CREATE USER room_rez_user WITH PASSWORD 'te$Tpr0J';

   ALTER ROLE room_rez_user SET client_encoding TO 'utf8';
   ALTER ROLE room_rez_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE room_rez_user SET timezone TO 'UTC';

   GRANT ALL PRIVILEGES ON DATABASE room_rez_db TO room_rez_user;
   \q
```

### Clone project from github
```sudo apt update
   python3 install virtualenv

   mkdir reservation
   cd reservation
   
   git init 
   git clone url
   source /env/bin/activate

   pip install django djangorestframework psycopg2 django-cors-headers django-extensions pandas
   
   code .
   "CTRL + SHIFT + P --> python select interpreter --> (env)main"
   
   python manage.py makemigrations 
   python manage.py migrate
   python manage runserver
```

### Create project srom scratch
##### 
```sudo apt update
   python3 install virtualenv

   mkdir reservation
   cd reservation
   
   virtualenv env
   source /env/bin/activate
   git init 
   
   pip install django djangorestframework psycopg2 django-cors-headers django-extensions pandas
   
   django-admin startproject main
   code .
   "CTRL + SHIFT + P --> python select interpreter --> (env)main"
   cd main
   
   python manage.py startapp room_reservation
   "update settings.py file --> INSTALLED_APPS section --> DATABASES section"
   
   python manage.py migrate
   python manage.py createsuperuser
   
   "Add models"
   python manage.py makemigrations 
   python manage.py migrate
   python manage runserver
   
   "Add serializers, services, apis, urls"
```
 
 **Well done! :+1: enjoy api.
 
 ![Screenshot from 2023-03-06 10-18-27](https://user-images.githubusercontent.com/47317870/223044018-ae900a66-91bc-4272-967f-4fab2fd1d6fd.png)
 
 ![Screenshot from 2023-03-06 10-26-22](https://user-images.githubusercontent.com/47317870/223044048-6172b0ec-dcd9-4c9c-b2a2-4c2eaa719aef.png)
 
 ![Screenshot from 2023-03-06 10-26-51](https://user-images.githubusercontent.com/47317870/223044096-5d112fdb-4a5d-4158-b1e5-04f15e00328d.png)
 
 ![Screenshot from 2023-03-06 10-27-20](https://user-images.githubusercontent.com/47317870/223044141-31cd80bb-713d-41f1-baa6-ff4a6330a198.png)

