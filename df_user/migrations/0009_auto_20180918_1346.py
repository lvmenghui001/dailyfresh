# Generated by Django 2.1.1 on 2018-09-18 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0008_auto_20180918_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteinfo',
            old_name='uphone_num',
            new_name='uphone',
        ),
    ]
