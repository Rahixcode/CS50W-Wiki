from django.test import TestCase, Client


class SearchTest(TestCase):
    def test_search_query(self):
        client = Client()
        response = client.get("/search/", {"q": "Python"})

        print(response.status_code)
        print(response.content.decode())

        self.assertEqual(response.status_code, 200)