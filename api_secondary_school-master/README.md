## Installation
```
    pip install Django==4.2.4
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
```
pip install -r requi....
## Start 
```
    python3 ./manage.py runserver 0.0.0.0:3088
```

## Reference
+ Foreign key:
https://stackoverflow.com/questions/75303043/django-db-utils-operationalerror-3780-referencing-column-and-referenced-column

## CheatSheets
+ Create project
```
    django-admin startproject ProjectName 
    cd ProjectName
```
+ Rename ProjectName to settings <br>
+ Create new folder src <br>
+ Example: Create user module <br>
```
    django-admin startapp user ./src/
```
+ Example: Create migration for app: <br>
```
    python manage.py makemigrations app_name --name migration_name --empty
```
+ Related to Database: <br>
```
Make migrations: 
    python manage.py makemigrations
Migrate:
    python manage.py migrate
```