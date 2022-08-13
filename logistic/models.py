from django.db import models
from django.contrib.auth.models import User


class Logistic(models.Model):
    location = models.CharField(max_length=220)
    to_destination = models.CharField(max_length=220)
    email = models.EmailField()
    number = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.location


class About_Us(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dis = models.TextField()


class Services(models.Model):
    red = 'service_box blu_colo'
    yelldark = 'service_box yelldark_colo'
    yell = 'service_box yell_colo'
    colors = (
        ('service_box blu_colo', red),
        ('service_box yelldark_colo', yelldark),
        ('service_box yell_colo', yell),
    )
    icon = models.ImageField(upload_to='service_icons')
    title = models.CharField(max_length=170)
    background_color = models.CharField(max_length=100, choices=colors)

    def __str__(self):
        return self.title


class Vehicles:
    class AirFreight(models.Model):
        title = models.CharField(max_length=180)
        img = models.ImageField(upload_to='air-img')

        def __str__(self):
            return self.title

    class Truck(models.Model):
        title = models.CharField(max_length=180)
        img = models.ImageField(upload_to='Truck')

        def __str__(self):
            return self.title

    class RailFreight(models.Model):
        title = models.CharField(max_length=120)
        img = models.ImageField(upload_to='rail')

        def __str__(self):
            return self.title


class Testimonials:
    class Test(models.Model):
        img = models.ImageField(upload_to='testimonial_img', default='def.png')
        full_name = models.CharField(max_length=220)
        campany = models.CharField(max_length=450, blank=True, null=True)
        comment = models.TextField()

        def __str__(self):
            return self.full_name

    class Reail(models.Model):
        img = models.ImageField(upload_to='testimonial_img', default='def.png')
        full_name = models.CharField(max_length=220)
        campany = models.CharField(max_length=450, blank=True, null=True)
        comment = models.TextField()

        def __str__(self):
            return self.full_name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    message = models.TextField()

class Address(models.Model):

    address = models.CharField(max_length=220)
    phone_number = models.CharField(max_length=170)
    email = models.EmailField()




class Newsletter(models.Model):
    news = 'Addres logistic company news'
    email = models.EmailField()

    def __str__(self):
        return self.news
