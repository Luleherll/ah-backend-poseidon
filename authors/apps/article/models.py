"""
class to define the structure of the article
"""

from django.db import models

# Create your models here.

from authors.apps.article.utils import generate_slug
from authors.apps.authentication.models import User


class Article(models.Model):

    # Model for an article
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articles",
        null=True
    )

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        error_messages={
            "required": "Add a title for your article."
        }
    )

    description = models.TextField(
        null=False,
        blank=False,
        error_messages={
            "required": "Add a description for your article."
        }
    )

    body = models.TextField(
        null=False,
        blank=False,
        error_messages={
            "required": "Add a body for your article."
        }
    )

    # auto_now_add sets the timezone.now when an instance is created
    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now updates the field every time the save method is called
    updated_on = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        """
        :return: string
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        override default save() to generate slug
        :param args:
        :param kwargs:
        """
        self.slug = generate_slug(Article, self)

        super(Article, self).save(*args, **kwargs)

