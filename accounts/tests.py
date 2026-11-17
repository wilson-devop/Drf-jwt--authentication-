from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


User = get_user_model()


class AuthenticationApiTests(APITestCase):
    def test_registration_creates_user_without_returning_password(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "wilson",
                "email": "wilson@example.com",
                "password": "StrongPassword!938",
                "password_confirm": "StrongPassword!938",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username="wilson")
        self.assertTrue(user.check_password("StrongPassword!938"))
        self.assertNotIn("password", response.data)
        self.assertNotIn("password_confirm", response.data)

    def test_registration_rejects_mismatched_passwords(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "wilson",
                "password": "StrongPassword!938",
                "password_confirm": "DifferentPassword!938",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username="wilson").exists())

    def test_login_refresh_and_logout(self):
        user = User.objects.create_user(
            username="wilson",
            password="StrongPassword!938",
        )
        login_response = self.client.post(
            reverse("accounts:login"),
            {"username": user.username, "password": "StrongPassword!938"},
            format="json",
        )

        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        access = login_response.data["access"]
        refresh = login_response.data["refresh"]

        refresh_response = self.client.post(
            reverse("accounts:refresh"),
            {"refresh": refresh},
            format="json",
        )
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
        logout_response = self.client.post(
            reverse("accounts:logout"),
            {"refresh": refresh},
            format="json",
        )
        self.assertEqual(
            logout_response.status_code,
            status.HTTP_205_RESET_CONTENT,
        )

        reuse_response = self.client.post(
            reverse("accounts:refresh"),
            {"refresh": refresh},
            format="json",
        )
        self.assertEqual(reuse_response.status_code, status.HTTP_401_UNAUTHORIZED)
