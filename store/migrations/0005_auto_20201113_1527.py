# Generated by Django 3.1.2 on 2020-11-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201113_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
