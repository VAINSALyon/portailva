# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-16 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_resourcefile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcefile',
            options={'permissions': (('file.manage_resources', 'Gérer les resources disponibles aux associations'),)},
        ),
    ]
