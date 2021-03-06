import pytest

from rest_framework.test import APIClient

from users.models import UserProfile


@pytest.mark.django_db
def test_user_profile_detail():
    user = UserProfile.objects.create(
        real_name='Anonymous Profile',
        email='anonymous@profile.com',
        slack_id='required',
    )
    response = APIClient().get(f'/api/users/{user.id}/')
    assert response.data['real_name'] == 'Anonymous Profile'
    assert 'url' in response.data
