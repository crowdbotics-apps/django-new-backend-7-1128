from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    r2 = models.ManyToManyField(
        "home.HomePage", blank=True, related_name="customtext_r2",
    )
    r21 = models.ManyToManyField(
        "users.User", blank=True, related_name="customtext_r21",
    )
    r3 = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
