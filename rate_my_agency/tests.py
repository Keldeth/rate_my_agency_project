from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from rate_my_agency.models import Agency
from rate_my_agency.views import index, about, show_city, show_agency, add_comment, add_like, add_dislike, delete_rating, register, register_agency, register_tenant, user_login, user_logout, add_image

# Unit testing for the rate_my_agency app:

class TestViews(TestCase):
    def test_index_view_GET(self):
        client = Client()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rate_my_agency/index.html')

    def test_about_view_GET(self):
        client = Client()
        response = self.client.get(reverse('rate_my_agency:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rate_my_agency/about.html')

    def test_register_view_GET(self):
        client = Client()
        response = self.client.get(reverse('rate_my_agency:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rate_my_agency/register.html')

    def test_register_agency_view_POST(self):
        client = Client()
        response = self.client.post(reverse('rate_my_agency:register_agency'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rate_my_agency/register_agency.html')

    def test_register_tenant_view_POST(self):
        client = Client()
        response = self.client.post(reverse('rate_my_agency:register_agency'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rate_my_agency/register_agency.html')


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_about_url_is_resolved(self):
        url = reverse('rate_my_agency:about')
        self.assertEquals(resolve(url).func, about)

    def test_show_city_url_is_resolved(self):
        url = reverse('rate_my_agency:show_city', args=['some-slug'])
        self.assertEquals(resolve(url).func, show_city)

    def test_register_url_is_resolved(self):
        url = reverse('rate_my_agency:register')
        self.assertEquals(resolve(url).func, register)

    def test_register_tenant_url_is_resolved(self):
        url = reverse('rate_my_agency:register_tenant')
        self.assertEquals(resolve(url).func, register_tenant)

    def test_register_agency_url_is_resolved(self):
        url = reverse('rate_my_agency:register_agency')
        self.assertEquals(resolve(url).func, register_agency)

    def test_user_login_url_is_resolved(self):
        url = reverse('rate_my_agency:login')
        self.assertEquals(resolve(url).func, user_login)

    def test_User_logout_url_is_resolved(self):
        url = reverse('rate_my_agency:logout')
        self.assertEquals(resolve(url).func, user_logout)

    def test_show_agency_url_is_resolved(self):
        url = reverse('rate_my_agency:show_agency', args=['some-slug'])
        self.assertEquals(resolve(url).func, show_agency)

    def test_add_comment_url_is_resolved(self):
        url = reverse('rate_my_agency:add_comment', args=['some-slug'])
        self.assertEquals(resolve(url).func, add_comment)

    def test_add_image_url_is_resolved(self):
        url = reverse('rate_my_agency:add_image', args=['some-slug'])
        self.assertEquals(resolve(url).func, add_image)

    def test_add_like_url_is_resolved(self):
        url = reverse('rate_my_agency:add_like', args=['some-slug'])
        self.assertEquals(resolve(url).func, add_like)

    def test_add_dislike_url_is_resolved(self):
        url = reverse('rate_my_agency:add_dislike', args=['some-slug'])
        self.assertEquals(resolve(url).func, add_dislike)

    def test_delete_rating_url_is_resolved(self):
        url = reverse('rate_my_agency:delete_rating', args=['some-slug'])
        self.assertEquals(resolve(url).func, delete_rating)








