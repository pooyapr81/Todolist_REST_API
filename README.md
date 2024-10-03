#  Dajngo REST API

A very simple site for reminding tasks that **API** functionality is implemented in


##  Installation
Install the virtual environment
```bash
virtualenv  -p  python3.8 <your-fav-env-name>
```
To activate your virtual environment
```
source <your-fav-env-name>/bin/activate
```

Install packages and run the project
```
cd eshop/
python manage.py runserver
```

install postman and then Choose the method you want then copy and paste One of the following links based on your chosen method
**GET**
```
http://127.0.0.1:8000/task/api/tasks/
http://127.0.0.1:8000/task/api/task/<task id>
```
**POST**
```
http://127.0.0.1:8000/task/api/task/create
```
**PUT**
```
http://127.0.0.1:8000/task/api/task/<task id>/update
```
**DELETE**
```
http://127.0.0.1:8000/task/api/task/<task id>/delete
```
