from django.db import models

class MainBlock(models.Model):
    title = models.TextField()
    undertitle = models.TextField()
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Главный блок"

    def __str__(self):
        return self.title

class WelcomeBlock(models.Model):
    title = models.TextField()
    undertitle = models.TextField()
    description = models.TextField()
    callToAction = models.TextField()
    nameOfCEO = models.TextField()
    CEO = models.TextField()
    sign = models.FileField(upload_to='uploads/WelcomeBlock')
    
    class Meta:
        verbose_name_plural = "Приветственный блок"

    def __str__(self):
        return self.title

class Questions(models.Model):
    name = models.TextField()
    phoneNumber = models.TextField()
    question = models.TextField()
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.name

class FAQ(models.Model):
    title = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Частые задаваемые вопросы"

    def __str__(self):
        return self.title

class Docs(models.Model):
    name = models.TextField()
    doc = models.FileField(upload_to='uploads/docs')

    class Meta:
        verbose_name_plural = "Памятки"

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.FileField(upload_to='uploads/news')

    class Meta:
        verbose_name_plural = "Последние новости"

    def __str__(self):
        return self.title