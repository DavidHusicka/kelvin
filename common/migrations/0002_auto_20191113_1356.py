# Generated by Django 3.0b1 on 2019-11-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'classes'},
        ),
        migrations.AlterField(
            model_name='class',
            name='code',
            field=models.CharField(max_length=20),
        ),
    ]
