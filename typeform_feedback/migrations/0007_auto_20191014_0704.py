# Generated by Django 2.2.5 on 2019-10-14 12:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typeform_feedback', '0006_auto_20191010_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergenerictypeformfeedback',
            name='_response',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True),
        ),
    ]
