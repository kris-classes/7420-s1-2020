# 7420 Web Applications Development

* [Github Mastering Markdown](https://guides.github.com/features/mastering-markdown/) - Mastering Markdown (for creating this file)


* [Django Tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
* [Customizing Django Authentication](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#substituting-a-custom-user-model)

* [Django Class-Based Views](https://ccbv.co.uk/)
* [Django Storages](https://django-storages.readthedocs.io/en/latest/index.html)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Django REST Framework Class-Based Views](http://www.cdrf.co/)

* [AWS Console](https://console.aws.amazon.com/console/home)
* [AWS Free Tier](https://aws.amazon.com/free/)
* [AWS in Plain English](https://expeditedsecurity.com/aws-in-plain-english/)
* [SendGrid](https://sendgrid.com/)
* [redis](https://redis.io)
* [Docker](https://www.docker.com/)

* [ReactJS](https://reactjs.org/)


## Python Plotting/Visualization Libraries:
* [Matplotlib](https://matplotlib.org/)
* [Plotly](https://plotly.com/python/)
* [Bokeh](https://bokeh.org/)

Resources to Learn Python:


free:

https://scrimba.com/g/gpython

## Can someone add descriptions or thumbnails of these videos?

https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-

https://www.youtube.com/watch?v=e1IyzVyrLSU

https://www.youtube.com/watch?v=yD0_1DPmfKM

https://www.youtube.com/watch?v=Z4D3M-NSN58


paid: 

https://www.udemy.com/course/complete-python-bootcamp/

https://www.udemy.com/course/python-django-dev-to-deployment/


* [AbdulAhmadzai](https://github.com/AbdulAhmadzai/WebApplicationAssignment1) - Building: building an app which is similar to face but different as well in my app you can create user and login and then you can create post and you can delete and update that post you can add friends.  so far this 
* [anil-geev](https://github.com/anil-geev/Assignment1_7420) - Building: TBD
* [beer-inder](https://github.com/beer-inder/Assignment1_7420_WebApp) - Building: Kindergarten app
* [fieldea](https://github.com/fieldea/WADA1) - Building: TBD
* [Jakeybaby](https://github.com/Jakeybaby/Assignemnt17420) - Building: simple Instagram
* [Jero327](https://github.com/Jero327/7420-Assessment) - Building: C2C platform provides the Postal services by individral, which committed to solving fast, small personal international and domestic express delivery needs.
* [lakshaysethi](https://github.com/lakshaysethi/Assignment-1-7420-ls) - Building: Instagram clone with almost all features and more 
* [manasvi](https://github.com/Manasvityagi/webapp_7420) - Building: A Dashboard for IoT Devices
* [shuang1101](https://github.com/shuang1101/WebAppAssignment1) - Building: TBD
* [tarantej](https://github.com/tarantej/assignment1_7420) - Building: Event Attendee Management system
* [TeresaZhu08](https://github.com/TeresaZhu08/Ass1) - Building: TBD
* [wandanli](https://github.com/wandanli/Web_App_Dev_Assignment1) - Building: Record All The Wonderful Moments


## Creating a database in PostgreSQL

```sql
CREATE USER myusername WITH PASSWORD 'some_password123';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myusername;
ALTER USER myusername CREATEDB;
```

## Hosting your Django app
there are several options to host your django app
1. host on your pc/laptop/dev server- use [ngrok.io](https://ngrok.io) - follow instructions after signing up
2. use heroku.com [heroku django docs](https://devcenter.heroku.com/articles/deploying-python)

### If you have problems installing psycopg2 on MacOS, the library for PostgreSQL, try this command.
```bash
LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install --upgrade psycopg2
```
