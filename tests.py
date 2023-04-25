import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skypro_testdjango.settings")
django.setup()


from rest_framework.test import APIClient
from skypro_testdjango.models import User
from rest_framework.authtoken.models import Token


api = APIClient(raise_request_exception=False)
user1 = User.objects.get(id=1)
token1 = Token.objects.get(user=user1).key
user2 = User.objects.get(id=2)
token2 = Token.objects.get(user=user2).key

answers = api.get('http://127.0.0.1:8000/get/resume/', headers={'Authorization': 'Token ' + token1})
assert answers.status_code == 200

answer = api.get('http://127.0.0.1:8000/get/resume/1/', headers={'Authorization': 'Token ' + token1})
assert answer.status_code == 200

answers = api.get('http://127.0.0.1:8000/get/resume/', headers={'Authorization': 'Token ' + token2})
assert answers.status_code == 200

answer = api.get('http://127.0.0.1:8000/get/resume/1/', headers={'Authorization': 'Token ' + token2})
assert answer.status_code == 200

patch = api.patch('http://127.0.0.1:8000/modify/resume/1/', headers={'Authorization': 'Token ' + token1}, data={'status': 'work'})
assert patch.status_code == 200

patch = api.patch('http://127.0.0.1:8000/modify/resume/1/', headers={'Authorization': 'Token ' + token2}, data={'status': 'work'})
assert patch.status_code == 404
