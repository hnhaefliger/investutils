# Generated by Django 3.2.7 on 2021-09-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=8, unique=True)),
                ('ticker_type', models.CharField(max_length=16)),
            ],
        ),
    ]
