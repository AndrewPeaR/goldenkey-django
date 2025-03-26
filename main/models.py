from django.db import models
from django.core.validators import FileExtensionValidator

class MainBlock(models.Model):
    title = models.TextField()
    undertitle = models.TextField()
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Главный блок"

    def __str__(self):
        return self.title

class WelcomeBlock(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    undertitle = models.TextField(verbose_name='Подзаголовок')
    description = models.TextField(verbose_name='Описание')
    callToAction = models.TextField(verbose_name='Призыв к действию')
    nameOfCEO = models.TextField(verbose_name='ФИО Руководителя')
    CEO = models.TextField(verbose_name='Должность')
    sign = models.ImageField(upload_to='sign', verbose_name='Картинка подписи', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    
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

class Advantages(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='advantages', verbose_name='Картинка преимущества', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])

    class Meta:
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return self.title
