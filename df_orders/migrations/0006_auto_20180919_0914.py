# Generated by Django 2.1.1 on 2018-09-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_orders', '0005_auto_20180918_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='odate',
            field=models.DateField(auto_now=True, verbose_name='订单日期'),
        ),
    ]