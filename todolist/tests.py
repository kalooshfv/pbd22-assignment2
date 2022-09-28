from django.test import TestCase

# Create your tests here.
class ToDoTest(TestCase):
    def test_url(self):
        resp = self.client.get('/todolist/')
        self.assertEqual(resp.status_code, 200)

    def test_template(self):
        resp = self.client.get('/todolist/')
        self.assertTemplateUsed(resp, 'todolist.html')