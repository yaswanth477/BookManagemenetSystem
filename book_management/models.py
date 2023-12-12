from django.db import models


class Author(models.Model):
    id = models.IntegerField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.IntegerField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title