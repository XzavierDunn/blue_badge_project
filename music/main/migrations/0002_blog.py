# Generated by Django 2.1.7 on 2019-03-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_post', models.CharField(max_length=500, verbose_name='Post:')),
            ],
        ),
    ]
