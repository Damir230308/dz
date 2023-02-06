from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from .views import AuthorModelViewSet
from .models import Author, Book


class TestAuthorViewSet(TestCase):

    
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        respounse = view(request)
        self.assertEqual(respounse.status_code, status.HTTP_200_OK)
    
    
    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors', {
            'first_name': 'Alex', 
            'last_name': 'Pushkin',
            'birthday_year': 1880
        })
        view = AuthorModelViewSet.as_view({'post': 'create'})
        respounse = view(request)
        self.assertEqual(respounse.status_code, status.HTTP_201_CREATED)
    
    
    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors', {
            'first_name': 'Alex', 
            'last_name': 'Grin',
            'birthday_year': 1799
        })
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view({'post': 'create'})
        respounse = view(request)
        self.assertEqual(respounse.status_code, status.HTTP_201_CREATED)

    
    def test_get_detail(self):
        author = Author.objects.create(first_name='Alex', last_name='Gogol', birthday_year=1826)
        client = APIClient()
        respounse = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(respounse.status_code, status.HTTP_200_OK)

    
    def test_edit_guest(self):
        author = Author.objects.create(first_name='Alex', last_name='Bebrik', birthday_year=1826)
        client = APIClient()
        respoune = client.put(f'/api/authors/{author.id}/', {'first_name': 'Grin', 'last_name': 'sadaas', 'birthday_year': 1780})
        self.assertEqual(respoune.status_code, status.HTTP_401_UNAUTHORIZED)
    
    
    def test_edit_admin(self):
        author = Author.objects.create(first_name='Alex', last_name='Bebrik', birthday_year=1826)
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        client.login(username='admin', password='admin')
        respoune = client.put(f'/api/authors/{author.id}/', 
        {'first_name': 'Grin', 'last_name': 'sadaas', 'birthday_year': 1780})
        author = Author.objects.get(pk=author.id)

        self.assertEqual(respoune.status_code, status.HTTP_200_OK)
        self.assertEqual(author.first_name, 'Grin')
        self.assertEqual(author.last_name, 'sadaas')
        self.assertEqual(author.birthday_year, 1780)
        client.logout()
