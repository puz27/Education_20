# Generated by Django 4.2.3 on 2023-07-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
