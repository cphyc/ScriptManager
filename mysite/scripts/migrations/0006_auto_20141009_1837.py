# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0005_auto_20141009_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='Content',
            new_name='code',
        ),
    ]
