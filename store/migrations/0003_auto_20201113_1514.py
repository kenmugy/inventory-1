# Generated by Django 3.1.2 on 2020-11-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201113_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='item_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]