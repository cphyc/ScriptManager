# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0002_auto_20141009_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='Last edit',
            new_name='last_update',
        ),
        migrations.RenameField(
            model_name='script',
            old_name='Title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='langage',
            name='langage',
            field=models.CharField(unique=True, max_length=16),
        ),
    ]
