# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20180701_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default='', to='lists.List'),
        ),
    ]
