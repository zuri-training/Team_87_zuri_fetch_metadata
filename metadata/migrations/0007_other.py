# Generated by Django 4.0.6 on 2022-08-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0006_delete_other'),
    ]

    operations = [
        migrations.CreateModel(
            name='other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]