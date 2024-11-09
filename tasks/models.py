from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title