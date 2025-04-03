| creating an environment 
>> virtualenv env 

| Activating it
>> env\Scripts\activate.ps1

| Installing dependencies
>> pip install django django-extensions djangorestframework

| Creating a Django project
>> django-admin startproject myproject

|| Changing the directory name fron myproject to projectspace

| Starting an app
>> django-admin startapp quickstart

|| configuring your project and app
>>  INSTALLED_APPs [ 
    'quickstart.apps.QuickstartConfig',
    'rest_framework',
    'django_extensions'
]
>> configured the template and static files directory
    'DIRS': [BASE_DIR / 'templates'],
    'DIRS': [BASE_DIR / 'static'],

>> Changed Timezones for better readibility

 TIME_ZONE = 'Asia/Kolkata'


>> created a model in quickstart.models
>> created views for the quickstart app

>> created a model in classes/models
>> created Class based views for classes app








