# Generated by Django 5.0 on 2023-12-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter', models.CharField(max_length=255)),
                ('qr', models.CharField(max_length=255, null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
