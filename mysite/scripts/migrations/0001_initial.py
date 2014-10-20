# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folderbla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Langage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('langage', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Published', models.DateTimeField(auto_now_add=True)),
                ('Last edit', models.DateTimeField()),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.TextField()),
                ('folder', models.ForeignKey(to='scripts.Folderbla')),
                ('langage', models.ForeignKey(to='scripts.Langage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
