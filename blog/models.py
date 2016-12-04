from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    item_name = models.CharField(max_length=512, unique=True)
    author_id = models.ForeignKey('Authors')
    item_price = models.IntegerField(default='100')
    item_description = models.TextField(blank=True, max_length=512)
    release_date = models.DateField(default='2016-12-12')
    item_status = models.CharField(max_length=2, choices=[('a', 'Avialable'),('na', 'Not Avialable')])
    item_tags = models.ManyToManyField('Tags', related_name='p')
    item_rating = models.DecimalField(max_digits=2,decimal_places=1)

    def __str__(self):
        return 'Item: {o.item_name} \nPrice: {o.item_price} \nRelease Date: {o.release_date} \n'.format(o=self)


class Authors(models.Model):
    author_name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return self.author_name


class Orders(models.Model):
    order_date = models.DateField(default = '2016-12-12')
    order_adress = models.CharField(max_length=100, default='None')
    user_id = models.ForeignKey(User)
    item_id = models.ForeignKey(Items)
    #item_count = models.ManyToManyField('Items', related_name='p')
    order_status = models.CharField(max_length=2, choices=[('p', 'Packing'),('d', 'Delivering'),('f', 'Delivered'), ('c', 'Cancelled')])
    order_comment = models.TextField(max_length=512, blank=True)

    def __str__(self):
        return 'ID: {o.id} \nOrder Date: {o.order_date} \n Item: {o.item_id}'.format(o=self)


class Comments(models.Model):
    user_id = models.ForeignKey(User)
    item_id = models.ForeignKey('Items')
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


# Create your models here.
