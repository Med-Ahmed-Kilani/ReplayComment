# Generated by Django 3.0.2 on 2020-01-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_post_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
