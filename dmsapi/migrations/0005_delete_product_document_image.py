# Generated by Django 4.1.1 on 2022-09-28 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmsapi', '0004_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='document',
            name='image',
            field=models.ImageField(default=1, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
