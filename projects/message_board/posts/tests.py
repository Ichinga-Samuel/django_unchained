from django.test import TestCase

from .models import Post


# Use TestCase for tests involving the database
# all test methods must start with the word test
class PostTest(TestCase):
    # Use the setUpTestData method to set up data that will be used by all test methods
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test post.")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test post.")

    def test_data_retrival(self):
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.id, self.post.id)
