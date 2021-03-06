# Generated by Django 3.0.7 on 2020-06-24 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0001_initial'),
        ('products', '0002_auto_20200622_1721'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorys.Category'),
        ),
    ]
