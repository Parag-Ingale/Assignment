# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2020-09-05 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='doc_pdf',
            field=models.FileField(default='DEFAULT VALUE', upload_to='documents/'),
        ),
    ]
