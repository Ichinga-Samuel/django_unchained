from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Blog


class BlogsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', email='testuser@django.com',
                                                        password='test_password')
        cls.blog_1 = Blog.objects.create(title='Blog 1', author=cls.user, body='Blog 1 body')

    def test_blog_model(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.title, 'Blog 1')
        self.assertEqual(blog.author, self.user)
        self.assertEqual(blog.body, 'Blog 1 body')

    def test_blog_views(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_blog_detail_view(self):
        res = self.client.get('/blog/1/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'blogs/blog_detail.html')
        res = self.client.get(reverse('blog_detail', kwargs={'pk': 1}))
        self.assertEqual(res.status_code, 200)

    def test_blog_create_view(self):
        res = self.client.post(reverse('new_blog'), data={
            "title": "The New Blog",
            "body": "A New Blog body",
             "author": self.user.id
        })
        # Redirects to the home page.
        self.assertEqual(res.status_code, 302)
        # Check if the blog was created.
        self.assertEqual(Blog.objects.get(title__exact='The New Blog').title, "The New Blog")

    def test_blog_update_view(self):
        res = self.client.post(reverse('blog_update', args=[1]), {
            'title': 'Updated Blog',
            'body': 'Updated Blog body'
        })
        # Redirects to the home page.
        self.assertEqual(res.status_code, 302)
        # Check if the blog was updated.
        self.assertEqual(Blog.objects.get(id=1).title, "Updated Blog")

    def test_blog_delete_view(self):
        res = self.client.post(reverse('blog_delete', args='1'))
        # Redirects to the home page.
        self.assertEqual(res.status_code, 302)
