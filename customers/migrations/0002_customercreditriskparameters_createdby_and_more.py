# Generated by Django 4.0.6 on 2022-12-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customercreditriskparameters',
            name='CreatedBy',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by'),
        ),
        migrations.AddField(
            model_name='customerinformation',
            name='CreatedBy',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by'),
        ),
    ]
