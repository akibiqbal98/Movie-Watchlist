from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from myapp.tests.test_models import create_movie, create_user_profile, create_playlist
import datetime


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        credentials = {
            'username': 'TestUser',
            'password': 'user1234'
        }
        self.test_user = User.objects.create_user(**credentials)
        self.user_profile1 = create_user_profile(self.test_user, False)

    def test_home_GET(self):
        url = reverse('myapp:home')
        response = self.client.get(url)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/collection.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_login_GET(self):
        url = reverse('myapp:login')
        response = self.client.get(url)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/login.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_login_POST(self):
        url = reverse('myapp:login')
        form_data = {'username': 'TestUser', 'password': 'user1234'}
        response = self.client.post(url, form_data, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/collection.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_logout_POST(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:logout')
        response = self.client.post(url, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/collection.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_moviedetails_GET(self):
        test_movie1 = create_movie(title='Released Test',
                                   releasedate=datetime.date(
                                       2016, 5, 13),
                                   )
        url = reverse('myapp:moviedetails', args=[test_movie1.slug])
        response = self.client.get(url)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/moviedetails.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_signup_GET(self):
        url = reverse('myapp:signup')
        response = self.client.get(url)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/signup.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_signup_POST(self):
        url = reverse('myapp:signup')
        form_data = {
            'first_name': 'Dummy',
            'last_name': 'User',
            'username': 'DummyUser',
            'email': 'dummy.user@gmail.com',
            'password1': 'user1234',
            'password2': 'user1234',
        }
        response = self.client.post(url, form_data, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/collection.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_search_GET(self):
        url = reverse('myapp:search')
        response = self.client.get(url)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/search.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_search_POST(self):
        url = reverse('myapp:search')
        form_data = {'searched': 'Movie Test'}
        response = self.client.post(url, form_data, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/search.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_userprofile_GET(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:userprofile')
        response = self.client.get(url)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/userprofile.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_playlistdetails_GET(self):
        self.client.login(username='TestUser', password='user1234')

        dummy_playlist = create_playlist(title='Test Playlist',
                                         createdby=self.test_user)

        url = reverse('myapp:playlistdetails', args=[dummy_playlist.slug])
        response = self.client.get(url)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/playlistdetails.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_createmovie_GET(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:createmovie')
        response = self.client.get(url, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/createmovie.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_createmovie_POST(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:createmovie')
        form_data = {
            'title': 'Dummy Movie 3',
            'releasedate': '05/31/2021',
            'language': 'en-US',
            'description': 'N/A'
        }
        response = self.client.post(url, form_data, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/createmovie.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_requestmovie_GET(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:requestmovie')
        response = self.client.get(url, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/requestmovie.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_requestmovie_POST(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:requestmovie')
        form_data = {
            'movietitle': 'Dummy Movie 4',
            'releasedate': '12/31/2021',
            'language': 'en-US',
        }
        response = self.client.post(url, form_data, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/requestmovie.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_createlist_GET(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:createlist')
        response = self.client.get(url, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/createlist.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_createlist_POST(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:createlist')
        form_data = {
            'title': 'Action',
            'description': 'N/A'
        }
        response = self.client.post(url, form_data, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/collection.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_addtoplaylist_POST(self):
        self.client.login(username='TestUser', password='user1234')
        test_movie1 = create_movie(title='Released Test',
                                   releasedate=datetime.date(
                                       2016, 5, 13),
                                   )
        dummy_playlist = create_playlist(title='Test Playlist',
                                         createdby=self.test_user)

        url = reverse('myapp:addtoplaylist', args=[
                      dummy_playlist.slug, test_movie1.slug])
        response = self.client.post(url, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/moviedetails.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_removefromplaylist_POST(self):
        self.client.login(username='TestUser', password='user1234')
        test_movie1 = create_movie(title='Released Test',
                                   releasedate=datetime.date(
                                       2016, 5, 13),
                                   )
        dummy_playlist = create_playlist(title='Test Playlist',
                                         createdby=self.test_user)

        url = reverse('myapp:removefromplaylist',
                      args=[dummy_playlist.slug,
                            test_movie1.slug])
        response = self.client.post(url, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/playlistdetails.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_donate_GET(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:donate')
        response = self.client.get(url)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/donate.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)

    def test_donate_POST(self):
        self.client.login(username='TestUser', password='user1234')
        url = reverse('myapp:donate')
        form_data = {
            'payment': 'paid'
        }
        response = self.client.post(url, form_data, follow=True)

        # SUCCESS TEST
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/userprofile.html')

        # FAIL TEST
        self.assertNotEquals(response.status_code, not 200)
