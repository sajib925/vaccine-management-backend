# Generated by Django 5.0.6 on 2024-08-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.TextField(),
        ),
    ]
