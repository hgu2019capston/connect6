# Generated by Django 2.2.1 on 2019-07-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AddField(
            model_name='session',
            name='manager_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
