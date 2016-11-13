from django.db import models


class Users(models.Model):

    loginname = models.CharField(max_length = 512, unique = True)
    firstname = models.CharField(max_length = 512)
    lastname = models.CharField(max_length = 512)
    email = models.EmailField(max_length = 512, unique = True)

    def __str__(self):
        return 'Login: {o.loginname} \nFirst Name: {o.firstname} \nLast Name: {o.lastname} \nEmail: {o.email}'.format(o = self)


class Items(models.Model):

    item_name = models.CharField(max_length = 512, unique = True)
    author_id = None
    item_price = models.IntegerField()
    release_date = None
    item_status = None
    item_tags = None


class Authors(models.Model):
    author_name = models.CharField(max_length = 512, unique = True)


class Orders(models.Model):
    order_date = None
    user_id = None
    total_price = None
    order_status = None


class ItemOrders(models.Model):
    order_id = None
    item_id = None


class RecommendationMatrix:
    pass




# Create your models here.
