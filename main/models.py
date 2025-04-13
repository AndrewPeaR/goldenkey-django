from django.db import models
from django.core.validators import FileExtensionValidator
from tinymce.models import HTMLField

# , null=True, blank=True
def path_filial_video(instance, filename):
    return '/'.join(filter(None, ('filials', instance.name, 'video', filename)))

class Filials(models.Model):
    name = models.CharField(verbose_name='Название филиала', max_length=100)
    slug = models.SlugField(unique=True)
    city = models.CharField(verbose_name='Город', max_length=100)
    street = models.CharField(verbose_name='Улица', max_length=150)
    timework = models.CharField(verbose_name='Время работы', max_length=100)
    group = models.CharField(verbose_name='Возраст для группы', max_length=100)
    count_child = models.CharField(verbose_name='До скольки детей идет набор', max_length=100)
    new = models.BooleanField(verbose_name='Статус нового', default=False, null=True, blank=True)
    poster = models.ImageField(verbose_name='Превью видео', upload_to=path_filial_video, validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], default='')

    class Meta:
        verbose_name_plural = "Филиалы"

    def __str__(self):
        return self.name

def path_filials_news(instance, filename):
    return '/'.join(filter(None, ('filialsNews', instance.filials.name, filename)))

class FilialsNews(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    filials = models.ForeignKey(Filials, on_delete = models.DO_NOTHING)
    image = models.ImageField(upload_to=path_filials_news, verbose_name='Картинка новости', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    class Meta:
        verbose_name_plural = "Новости филиалов"

    def __str__(self):
        return self.title

def path_filials_team(instance, filename):
    return '/'.join(filter(None, ('filialsTeam', instance.filials.name, filename)))

class FilialsTeam(models.Model):
    firstname = models.CharField(verbose_name='Имя Отчество', max_length=200)
    lastname = models.CharField(verbose_name='Фамилия', max_length=100)
    status = models.CharField(verbose_name='Профессия', max_length=100)
    expirience = models.CharField(verbose_name='Количество опыта', max_length=50)
    quote = models.TextField(verbose_name='Цитата', null=True, blank=True)
    filials = models.ForeignKey(Filials, on_delete = models.DO_NOTHING)
    image = models.ImageField(verbose_name='Фотография', upload_to=path_filials_team, validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    callToAction = models.TextField(verbose_name='Призыв к действию', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Работники филиалов"

    def __str__(self):
        return self.lastname + ' ' + self.firstname

class DocumentsPage(models.Model):
    title = models.TextField()
    content = HTMLField()
    
    class Pages(models.TextChoices):
        GOLDENKEY = 'GLK', 'ООО «Золотой ключик»'
        BASHAEVA = 'BSH', 'ИП Башаева М.Р.' 

    page = models.CharField(max_length=3, choices=Pages.choices, default=Pages.GOLDENKEY)
    
    class Meta:
        verbose_name_plural = "Страница с документами"
    def __str__(self):
        return self.title

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

class BookSend(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=70)
    phoneNumber = models.CharField(verbose_name='Телефон', max_length=25)
    email = models.CharField(verbose_name='E-mail', max_length=100)
    policy = models.BooleanField(verbose_name='Согласие на обработку персональных данных', default=False)
    send_at = models.DateTimeField(verbose_name='Дата отправления', auto_now_add=True, null=True)
    
    class Meta:
        verbose_name_plural = "Отправленния пособия для адаптации"

    def __str__(self):
        return self.name

class EmailSettings(models.Model):
    theme = models.CharField(verbose_name='Тема письма', max_length=300)
    body = models.TextField(verbose_name='Тело письма')
    pdf = models.FileField(upload_to='setting/sendBook')

    class Meta:
        verbose_name_plural = "Настройка рассылки пособия"

    def __str__(self):
        return self.theme