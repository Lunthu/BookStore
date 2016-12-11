from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    item_name = models.CharField(max_length=512, unique=True)
    item_image = models.ImageField(upload_to='images/', blank=True, null=True)
    item_publisher = models.ForeignKey('Publishers')
    author_id = models.ForeignKey('Authors')
    item_price = models.IntegerField(default='100')
    item_description = models.TextField(blank=True, max_length=512)
    release_date = models.DateField(default='2016-12-12')
    item_status = models.CharField(max_length=2, choices=[('a', 'Доступно'),('na', 'Не доступно')])
    item_genre = models.ManyToManyField('Tags', related_name='p')
    item_rating = models.DecimalField(max_digits=2,decimal_places=1, default=0.0, editable=False)

    def __str__(self):
        return self.item_name


class Authors(models.Model):
    author_name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return self.author_name


class Publishers(models.Model):
    publisher_name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return self.publisher_name


class Orders(models.Model):
    order_date = models.DateField(auto_now=True)
    order_adress = models.CharField(max_length=100, default='None', verbose_name=u'Желаемый адрес доставки')
    user_id = models.ForeignKey(User)
    item_id = models.ForeignKey(Items, verbose_name=u'Желаемая книга')
    # item_count = models.ManyToManyField('Items', related_name='p')
    order_status = models.CharField(max_length=2, choices=[('p', 'Комплектуется'),('d', 'Отправляется'),('f', 'Отправлено'), ('c', 'Отменено')], verbose_name=u'Статус заказа')
    order_comment = models.TextField(max_length=512, blank=True, verbose_name=u'Ваш комментарий (пожелания, номер телефона для связи, т.д.)')

    def __str__(self):
        return 'ID: {o.id} \nДата заказа: {o.order_date} \n Книга: {o.item_id}'.format(o=self)


class Comments(models.Model):
    user_id = models.ForeignKey(User, blank=True)
    item_id = models.ForeignKey('Items', blank=True)
    comment_date = models.DateTimeField(auto_now=True)
    comment_text = models.TextField(max_length=512)

    def __str__(self):
        return 'User: {o.user_id}, Item: {o.item_id}, Date: {o.comment_date}, Text: {o.comment_text}'.format(o=self)

class Tags(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name


class RecommendationMatrix:
    pass

class News(models.Model):
    news_text = models.TextField(max_length=512)
    news_date = models.DateTimeField(auto_now=True)




# Create your models here.
