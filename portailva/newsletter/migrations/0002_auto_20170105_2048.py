# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlenewsletterelement',
            options={'verbose_name': 'Article de newsletter'},
        ),
        migrations.AlterModelOptions(
            name='eventnewsletterelement',
            options={'verbose_name': 'Evenement de newsletter'},
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='articles',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='articles',
            field=models.ManyToManyField(related_name='newletter', to='newsletter.ArticleNewsletterElement', verbose_name='Articles'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='events',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='events',
            field=models.ManyToManyField(related_name='newletter', to='newsletter.EventNewsletterElement', verbose_name='Evènements'),
        ),
    ]