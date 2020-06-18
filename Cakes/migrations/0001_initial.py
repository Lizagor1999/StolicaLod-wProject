# Generated by Django 3.0.7 on 2020-06-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_name', models.CharField(max_length=255)),
                ('cake_number', models.PositiveIntegerField(unique=True)),
                ('cake_price', models.PositiveIntegerField(unique=True)),
                ('cake_description', models.CharField(max_length=255)),
            ],
        ),
    ]
