# Generated by Django 3.2.7 on 2022-01-13 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockprice', '0002_auto_20220113_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprice',
            name='market',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stockprice.market'),
        ),
    ]
