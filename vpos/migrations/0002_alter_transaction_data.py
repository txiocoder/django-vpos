# Generated by Django 4.0.1 on 2022-02-14 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='data',
            field=models.JSONField(default=dict, editable=False, verbose_name='additional data'),
        ),
    ]
