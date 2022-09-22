# Generated by Django 4.1.1 on 2022-09-22 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Typification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_document', models.IntegerField(choices=[(1, 'Fisico'), (2, 'Electronico')], default=1)),
                ('amount', models.PositiveIntegerField()),
                ('typification', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='typification', to='dmsapi.typification')),
            ],
        ),
    ]
