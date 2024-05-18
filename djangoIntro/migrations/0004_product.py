# Generated by Django 5.0.6 on 2024-05-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoIntro', '0003_alter_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
