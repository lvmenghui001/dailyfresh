# Generated by Django 2.1.1 on 2018-09-18 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0007_auto_20180918_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50, verbose_name='收货人姓名')),
                ('uaddress', models.CharField(max_length=100, verbose_name='收货地址')),
                ('uyoubian', models.CharField(default='', max_length=6, verbose_name='邮编')),
                ('uphone_num', models.CharField(default='', max_length=11, verbose_name='收货人手机')),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='uaddress',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='uphone_num',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='ushou',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='uyoubian',
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo'),
        ),
    ]