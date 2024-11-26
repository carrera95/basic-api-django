import pytest 
from django.urls import reverse 
from rest_framework.test import APIClient 
from rest_framework import status 
from django.contrib.auth import get_user_model 

# Test
# Succesfull User register
@pytest.mark.django_db
def test_user_register():
    # Set up url from urls.py
    client = APIClient()
    url = reverse('register')
    # Data to send
    data = {
        'username': 'testuser',
        'email': 'testuser@admin.com',
        'password': 'testuser123'
    }
    # Do the HTTP Request
    response = client.post(
        url, 
        data, 
        format='json'
    )
    # Tests
    assert response.status_code == status.HTTP_200_OK
    assert 'username' in response.data['user']
    assert response.data['user']['username'] == 'testuser'
    assert 'access' in response.data
    assert 'refresh' in response.data

# Test
# Duplicated User register
@pytest.mark.django_db
def test_duplicated_user_register():
    User = get_user_model()
    # Set up urls from urls.py
    client = APIClient()
    url = reverse('register')
    # Data to send
    data = {
        'username': 'testuser',
        'email': 'testuser@admin.com',
        'password': 'testuser123'    
    }
    # Create the first user to do the duplicate test
    User.objects.create_user(
        username='testuser', 
        email='testuser@admin.com', 
        password='testuser123'
    )
    # Do the HTTP Request
    response = client.post(
        url,
        data,
        format='json'
    )
    # Tests
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'username' in response.data or  'email' in response.data

# Test
# Missing data User register
@pytest.mark.django_db
def test_user_register_missing_data():
    # Set up urls from urls.py
    client = APIClient()
    url = reverse('register')
    # Data to send
    data = { # Missing password
        'username': 'testuser',
        'email': 'testuser@admin.com'
    }
    # Do the HTTP Request
    response = client.post(
        url,
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'password' in response.data

    data = { # Missing email
        'username': 'testuser',
        'password': 'testuser123'
    }
    # Do the HTTP Request
    response = client.post(
        url,
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'email' in response.data

    data = { # Missing username
        'email': 'testuser@admin.com',
        'password': 'testuser123'
    }
    # Do the HTTP Request
    response = client.post(
        url,
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'username' in response.data

# Test
# Invalid User mail register
@pytest.mark.django_db
def test_invalid_mail_user_register():
    # Set up url
    client = APIClient()
    url = reverse('register')
    #data
    data = {
        'username': 'testuser',
        'email': 'invalid-mail',
        'password': 'testuser123'
    }
    # Do the HTTP Request
    response = client.post(
        url,
        data,
        format='json'
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'email' in response.data