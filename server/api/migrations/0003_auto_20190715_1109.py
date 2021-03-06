# Generated by Django 2.2.1 on 2019-07-15 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190711_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='stone',
            name='color',
            field=models.CharField(default='white', max_length=10),
        ),
        migrations.AddField(
            model_name='stone',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stone_session', to='api.Session'),
        ),
    ]
