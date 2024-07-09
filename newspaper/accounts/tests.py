from django.test import TestCase
from django.contrib.auth import get_user_model


class SignUpViewTests(TestCase):
    def test_sign_up_form(self):
        res = self.client.post("/accounts/signup/", {
            "username": "testuser",
            "email": "testuser@email.com",
            "password1": "testpass123",
            "password2": "testpass123",
        })
        self.assertEqual(res.status_code, 302)
