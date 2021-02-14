from django.db import models


class Book(models.Model):
    # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
