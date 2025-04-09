*This is a Advance Text Utils Django Project Taught by Youtuber CodeWithHarry. I followed his tutorial entirely and then added my own features in it to learn how to build django applications.*

The project is located in the main directory of projectspace. this directory contains all of our other directories. Namely
- templates (Manually Created)
- myproject (Django Project Directory)
- static (Manually Created)
- textutils (App directory)
- authapp (Authentication Directory)(incase if i make one)

Made some changes in the myproject/settings.py like giving path to the static and template files and changed the timezone to india for better readability of dates in models and database. **Changes have been also documented at the root of the file using python comments.**


settings.py > stores the settings for your project
manage.py > allows us to interact with the project
urls.py > contains the paths that map to your apps/urls.py and eventually views.
wsgi.py > web server gateway interface is a reliable way to host your apps (production level stuff)
asgi.py > 



How does Django Look for a view?
-> When you enter the url 127.0.0.1:8000/ the django project looks for the paths in urls.py of the project, Now i have assigned the empty path or 127.0.0.1:8000/ to the textutils application for now. so it looks for the requested view in textutils/urls.py it finds the empty path i have assigned to a demo view and renders the website as i have asked.

path('',views.index,name = 'index')
'' - is the endpoint
views.index - is the function thats supposed to run
name is the name of the url(useful in your html templates) 

Exercise - 1 : Personal Navigator
pick five websites that you use the most, you need to take those urls and create a website that will allow us to easily access those websites (Good idea for a website that can be implementedd in some diary like apps.)