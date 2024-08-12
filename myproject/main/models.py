from django.db import models
from django.utils.text import slugify
 
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    # slug = models.CharField(max_length=50, unique=True, blank=True) # Параметр unique=True гарантирует, что значение slug будет уникальным для каждого объекта Category. Параметр blank=True позволяет оставлять это поле пустым при создании нового объекта.
    img_class = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs): # Переопределяет метод save(), который вызывается при сохранении объекта Category. Это позволяет нам генерировать значение slug автоматически.
    #     if not self.slug: # Проверяет, было ли значение slug уже задано. Если нет, то оно будет сгенерировано.
    #         self.slug = slugify(self.name) # Использует функцию slugify() из Django, чтобы сгенерировать строку slug на основе значения name. Это помогает создавать SEO-дружественные URL-адреса.
    #     super().save(*args, **kwargs) # super().save(*args, **kwargs): Вызывает оригинальную реализацию метода save(), чтобы сохранить объект Category в базу данных.

class Another(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=70)
    icon_url = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=70)
    short_desc = models.TextField()
    full_desc = models.TextField()
    image_name = models.CharField(max_length=100)
    rating = models.FloatField()
    category = models.ManyToManyField(Another)

    def __str__(self):
        return self.name