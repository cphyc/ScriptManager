# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0004_auto_20141009_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='pub_date',
            new_name='publication_date',
        ),
    ]
