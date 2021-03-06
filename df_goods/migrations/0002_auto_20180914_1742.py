# Generated by Django 2.0.5 on 2018-09-14 09:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsinfo',
            options={'verbose_name': '商品表', 'verbose_name_plural': '商品表'},
        ),
        migrations.AlterModelOptions(
            name='typeinfo',
            options={'verbose_name': '商品类型表', 'verbose_name_plural': '商品类型表'},
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(verbose_name='点击量'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(verbose_name='商品详情'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gjianjie',
            field=models.CharField(max_length=200, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gkucun',
            field=models.IntegerField(verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='goods', verbose_name='商品图片'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='商品价格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(max_length=20, verbose_name='商品名'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.TypeInfo', verbose_name='商品类型'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(default='500g', max_length=20, verbose_name='规格'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='ttitle',
            field=models.CharField(max_length=20, verbose_name='商品类名'),
        ),
    ]
