from django.test import TestCase
from django.urls import resolve, reverse
from .views import HomePageView


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve("/")
        self.assertEquals(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse("articles-category-list", args=("name",))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_articles_view_status_code(self):
        url = reverse("articles-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_articles_detail_view_status_code(self):
        url = reverse(
            "news-detail",
            args=(
                "year",
                "month",
                "day",
                "slug",
            ),
        )
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
