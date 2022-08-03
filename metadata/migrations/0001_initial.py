# Generated by Django 4.0.6 on 2022-08-03 06:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Name must be greater than 2 characters')])),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=250)),
                ('filesize', models.CharField(max_length=20)),
                ('filetype', models.CharField(max_length=20)),
                ('mimetype', models.CharField(max_length=50)),
                ('imagewidth', models.CharField(max_length=120, null=True)),
                ('imagelength', models.CharField(max_length=120, null=True)),
                ('imageorientation', models.CharField(max_length=120, null=True)),
                ('bitspixel', models.CharField(max_length=120, null=True)),
                ('pixelformat', models.CharField(max_length=120, null=True)),
                ('creationdate', models.CharField(max_length=120, null=True)),
                ('cameraaperture', models.CharField(max_length=120, null=True)),
                ('camerafocal', models.CharField(max_length=50, null=True)),
                ('cameraexposure', models.CharField(max_length=50, null=True)),
                ('cameramodel', models.CharField(max_length=120, null=True)),
                ('cameramanufacturer', models.CharField(max_length=120, null=True)),
                ('compression', models.CharField(max_length=120, null=True)),
                ('isospeed', models.CharField(max_length=50, null=True)),
                ('exifversion', models.CharField(max_length=50, null=True)),
                ('shutterspeed', models.CharField(max_length=50, null=True)),
                ('aperture', models.CharField(max_length=50, null=True)),
                ('exposure_bias', models.CharField(max_length=120, null=True)),
                ('focallength', models.CharField(max_length=50, null=True)),
                ('producer', models.CharField(max_length=120, null=True)),
                ('comment', models.CharField(max_length=120, null=True)),
                ('formatversion', models.CharField(max_length=120, null=True)),
                ('resolutionunit', models.IntegerField(null=True)),
                ('exifoffset', models.IntegerField(null=True)),
                ('make', models.CharField(max_length=120, null=True)),
                ('model', models.CharField(max_length=120, null=True)),
                ('software', models.CharField(max_length=120, null=True)),
                ('orientation', models.IntegerField(null=True)),
                ('datetime', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
