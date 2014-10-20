# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0003_auto_20141009_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='Published',
            new_name='pub_date',
        ),
    ]
