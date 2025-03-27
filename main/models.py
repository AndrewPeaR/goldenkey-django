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
    name = models.TextField(verbose_name='Имя')
    phoneNumber = models.TextField(verbose_name='Телефон')
    question = models.TextField(verbose_name='Вопрос')
    status = models.BooleanField(verbose_name='Обработан', default=False)
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обработки', auto_now=True)

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

class Memo(models.Model):
    name = models.TextField()
    doc = models.FileField(upload_to='memo')

    class Meta:
        verbose_name_plural = "Памятки"

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст новости')
    image = models.ImageField(upload_to='news', verbose_name='Картинка новости', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])

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

class Performance(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    poster = models.ImageField(upload_to='performance', verbose_name='Заставка')
    video = models.FileField(upload_to='performance', verbose_name='Видео')

    class Meta:
        verbose_name_plural = "Блок с видео"

    def __str__(self):
        return self.title
    
class PerformanceItems(models.Model):
    description = models.TextField(verbose_name='Текст')
    class Meta:
        verbose_name_plural = "Блок с преимуществами под видео"

    def __str__(self):
        return self.description
    
class Reviews(models.Model):
    name = models.TextField(verbose_name='Имя ребенка')
    parent = models.TextField(verbose_name='Родитель(ли)')
    childAge = models.TextField(verbose_name='Возраст ребенка')
    review = models.TextField(verbose_name='Отзыв')
    fileUrl = models.FileField(upload_to='reviews', verbose_name='Фото или видео отзыва')
    published = models.BooleanField(verbose_name='Видимость')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name