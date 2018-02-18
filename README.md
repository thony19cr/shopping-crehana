- Use python 2.7
- pip install virtualenv
- Directory used is envs/
- virtualen shopping
- Inside the folder 'shopping': 'source Script/activate'

- Install dependencies: `pip install -r requirements.txt` (for development)
- Create database user and set a password and create a db for the application

- Make migrations/(estructura to database): 'python manage.py migrate'
```
./manage.py migrate productos
./manage.py migrate usuarios
./manage.py migrate ventas
```

- Run Django: 'python manage.py runserver'