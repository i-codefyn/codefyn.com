from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse,resolve

from .forms import CustomUserCreationForm # new
from .views import SignupPageView # new

class SignupPageTest(TestCase):

    username = 'newuser'
    email = 'codefyn22@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response,'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'hi it should not be here')
    

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
        self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
        [0].email, self.email)

    def test_signup_view(self): # new
        view = resolve('/accounts/signup/')
        self.assertEqual(
        view.func.__name__,
        SignupPageView.as_view().__name__
         )


class CustomUserTest(TestCase):


    def test_create_user(self):
        user = get_user_model()
        user = user.objects.create_user(
        username ='codefyn',
        email='codefyn@gmail.com',
        password = 'jaimaa@007')
        self.assertEquals(user.username, 'codefyn')
        self.assertEquals(user.email, 'codefyn@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User =get_user_model()
        admin_user = User.objects.create_superuser(
        username = 'superadmin',
        email = 'superadmin@gmail.com',
        password = 'superadmin@123'

        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
       


