# Generated by Django 2.1.1 on 2018-09-15 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_orders', '0003_auto_20180629_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='df_user',
            new_name='user',
        ),
    ]