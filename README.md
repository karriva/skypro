инструкция:
создаем venv 
pip install -r requirements.py

выполняем миграции в базу

python ./manage.py migrate

загружаем фикстуры в базу:

python manage.py loaddata fixtures/user.json --app auth.User

python manage.py loaddata fixtures/data.json --app skypro_testdjango.user

python manage.py loaddata fixtures/token.json --app authtoken.token 

для запуска приложения:

python ./ manage.py runserver

for run tests:

python tests.py

