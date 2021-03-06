# Generated by Django 3.2.7 on 2021-11-12 11:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='newterm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('non_answer', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('correct', models.BooleanField(default=False)),
                ('randanswer', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('productName', models.CharField(default='', max_length=30)),
                ('productText', models.CharField(default='', max_length=1000)),
                ('like', models.IntegerField()),
                ('image', models.ImageField(upload_to='product/')),
                ('getcoin', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='manner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=18)),
                ('like', models.IntegerField()),
                ('dis_like', models.IntegerField()),
                ('hashtag_me', models.CharField(max_length=20)),
                ('hashtag_you', models.CharField(max_length=20)),
                ('hashtag_situation', models.CharField(max_length=500)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('getcoin', models.BooleanField(default=False, null=True)),
                ('secret', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='communityText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=500)),
                ('like', models.IntegerField()),
                ('dis_like', models.IntegerField()),
                ('title', models.CharField(default='', max_length=30)),
                ('selected', models.BooleanField(default=False, null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='communityComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('like', models.IntegerField()),
                ('dis_like', models.IntegerField()),
                ('text', models.CharField(max_length=300)),
                ('getcoin', models.BooleanField(default=False, null=True)),
                ('communitytext', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.communitytext')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(blank=True, default='', max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('certified', models.BooleanField(default=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
