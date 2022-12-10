from django.utils import timezone

from django.db import models
from django.urls import reverse


class Category(models.Model):
    category = models.CharField(
        "Category", max_length=250, help_text="Max length is 250"
    )
    slug = models.SlugField("Slug", null=True)

    class Meta:
        verbose_name = "Категорія для публікації"
        verbose_name_plural = "Категорії для публікації"

    def __str__(self) -> str:
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse("articles-category-list", kwargs={"slug": self.slug})
        except:
            url = "/"
        return url


class Article(models.Model):
    title = models.CharField("Title", max_length=250, help_text="Max length is 250")
    description = models.TextField(blank=True, verbose_name="Description")
    pub_date = models.DateTimeField("Publish Date", default=timezone.now)
    slug = models.SlugField("Slug", unique_for_date="pub_date")
    main_page = models.BooleanField("Main Page", default=False, help_text="Show")
    category = models.ForeignKey(
        Category,
        related_name="articles",
        blank=True,
        null=True,
        verbose_name="Category",
        on_delete=models.CASCADE,
    )
    objects = models.Manager()

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            url = reverse(
                "news-detail",
                kwargs={
                    "year": self.pub_date.strftime("%Y"),
                    "month": self.pub_date.strftime("%m"),
                    "day": self.pub_date.strftime("%d"),
                    "slug": self.slug,
                },
            )
        except:
            url = "/"

        return url


class ArticleImage(models.Model):
    article = models.ForeignKey(
        Article, verbose_name="Article", related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField("Picture", upload_to="photos")
    title = models.CharField(
        "Title", max_length=250, help_text="Максимум 250 символів", blank=True
    )

    class Meta:
        verbose_name = "Фото для статті"
        verbose_name_plural = "Фото для статті"

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return self.image.name.rsplit("/", 1)[-1]
