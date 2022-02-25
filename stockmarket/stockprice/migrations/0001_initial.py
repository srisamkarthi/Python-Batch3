# Generated by Django 3.2.7 on 2022-01-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sprice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockName', models.CharField(max_length=50)),
                ('stockType', models.CharField(max_length=50)),
                ('exchangeName', models.CharField(max_length=50)),
                ('stockPrice', models.IntegerField()),
            ],
            options={
                'db_table': 'stock_price',
            },
        ),
    ]