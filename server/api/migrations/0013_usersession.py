# Generated by Django 2.2.3 on 2019-07-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_resultomok_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('user_id', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
