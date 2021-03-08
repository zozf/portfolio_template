# Generated by Django 2.2.17 on 2021-01-25 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100, verbose_name='コース')),
                ('school', models.CharField(max_length=100, verbose_name='学校')),
                ('place', models.CharField(max_length=100, verbose_name='場所')),
                ('period', models.CharField(max_length=100, verbose_name='期間')),
            ],
        ),
    ]