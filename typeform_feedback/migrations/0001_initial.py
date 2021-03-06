# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-03-26 17:32
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericTypeformFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('object_id', models.IntegerField(db_index=True, null=True)),
                ('typeform_url', models.CharField(blank=True, max_length=200)),
                ('typeform_type', models.CharField(choices=[('S', 'Weekly')], max_length=1)),
                ('content_type', models.ForeignKey(null=True,
                                                   on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGenericTypeformFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('response', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('status', models.CharField(choices=[('N', 'Not available'),
                                                     ('P', 'Pending'), ('D', 'Done')], max_length=1)),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               related_name='responses', to='typeform_feedback.GenericTypeformFeedback')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
