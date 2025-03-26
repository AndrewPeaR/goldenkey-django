from django.db import models

class Questions(models.Model):
    name = models.TextField()
    phoneNumber = models.TextField()
    question = models.TextField()
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FAQ(models.Model):
    title = models.TextField()
    description = models.TextField()

class Docs(models.Model):
    name = models.TextField()
    doc = models.FileField(upload_to='uploads/docs')

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.FileField(upload_to='uploads/news')