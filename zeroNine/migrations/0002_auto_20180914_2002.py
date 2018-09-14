# Generated by Django 2.1.1 on 2018-09-14 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zeroNine', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RemoveField(
            model_name='product_has_user',
            name='Product_idx',
        ),
        migrations.RemoveField(
            model_name='product_has_user',
            name='User_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='catagory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='idx',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='productName',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='product',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='zeroNine.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='userName',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='product',
            name='direct',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='facebook_addr',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_path',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='member_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='notice',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='site_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_num',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product_has_User',
        ),
    ]