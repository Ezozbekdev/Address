# Generated by Django 4.1 on 2022-08-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistic',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]