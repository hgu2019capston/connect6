# Generated by Django 2.2.1 on 2019-07-15 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_stone_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stone',
            name='order',
        ),
    ]
