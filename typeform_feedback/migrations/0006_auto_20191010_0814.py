# Generated by Django 2.2.5 on 2019-10-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typeform_feedback', '0005_usergenerictypeformfeedback_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergenerictypeformfeedback',
            name='status',
            field=models.CharField(choices=[('N', 'Not available'), ('P', 'Pending'), ('A', 'Answered'), ('D', 'Done'), ('F', 'Fail')], default='P', max_length=1),
        ),
    ]
