# Generated by Django 3.2.4 on 2021-06-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightsave', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]