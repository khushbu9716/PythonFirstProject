# Generated by Django 5.0.6 on 2024-05-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoIntro', '0002_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]