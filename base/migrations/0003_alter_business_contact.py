# Generated by Django 5.2 on 2025-04-22 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_category_description_business_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
    ]
