import pytest
from rest_framework.test import APIClient
from rest_framework import status


@pytest.mark.django_db
class TestCreatePublisherView:
    def test_create_publisher(self):
        data = {
        "name": "Test Publisher",
        "description": "Test Description",
        }
        url = "api/publishers/"

        response = APIClient().post(url, data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] is not None
        