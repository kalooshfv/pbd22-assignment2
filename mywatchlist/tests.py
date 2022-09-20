from django.test import TestCase

# Create your tests here.
# Create your tests here.
class KatalogTest(TestCase):
    def test_url(self):
        resp = self.client.get('/mywatchlist/')
        self.assertEqual(resp.status_code, 200)

    def test_template(self):
        resp = self.client.get('/mywatchlist/')
        self.assertTemplateUsed(resp, 'mywatchlist.html')

    def test_xml(self):
        resp = self.client.get('/mywatchlist/xml/')
        self.assertEqual(resp.status_code, 200)

    def test_json(self):
        resp = self.client.get('/mywatchlist/json/')
        self.assertEqual(resp.status_code, 200)