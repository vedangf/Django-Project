# Generated by Django 3.2.7 on 2021-09-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0004_city_city_pic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subject1',
            new_name='Subject',
        ),
        migrations.AlterField(
            model_name='city',
            name='city_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
