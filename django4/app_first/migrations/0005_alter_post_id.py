# Generated by Django 3.2 on 2021-04-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_first', '0004_delete_nameform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]