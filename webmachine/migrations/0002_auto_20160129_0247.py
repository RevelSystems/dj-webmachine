# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import webmachine.models


class Migration(migrations.Migration):

    dependencies = [
        ('webmachine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='timestamp',
            field=models.IntegerField(default=webmachine.models.generate_time),
        ),
    ]
