# Generated by Django 2.1 on 2018-11-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_auto_20181103_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_brandName',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
