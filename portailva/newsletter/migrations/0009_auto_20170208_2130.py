# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-08 21:30
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_auto_20170131_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=models.ImageField(blank=True, help_text="Cette image est utilisée dans l'envoie de la newsletter VA", null=True, upload_to='', verbose_name='Image à la une'),
        ),
    ]
