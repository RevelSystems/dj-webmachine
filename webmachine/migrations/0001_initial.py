# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=32)),
                ('secret', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('status', models.SmallIntegerField(default=1, choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Canceled'), (4, 'Rejected')])),
                ('user', models.ForeignKey(related_name='consumers_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nonce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token_key', models.CharField(max_length=32)),
                ('consumer_key', models.CharField(max_length=32)),
                ('key', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=32)),
                ('secret', models.CharField(max_length=32)),
                ('token_type', models.SmallIntegerField(choices=[(1, 'Access'), (2, 'Request')])),
                ('callback', models.CharField(max_length=2048)),
                ('callback_confirmed', models.BooleanField(default=False)),
                ('verifier', models.CharField(max_length=16)),
                ('timestamp', models.IntegerField(default=1454057645.71723)),
                ('is_approved', models.BooleanField(default=False)),
                ('consumer', models.ForeignKey(related_name='tokens_consumer', to='webmachine.Consumer')),
                ('user', models.ForeignKey(related_name='tokens_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
