# Generated by Django 4.1.1 on 2022-09-28 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('middle_name', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('region_origin', models.CharField(choices=[('Select', 'Select'), ('SouthWest', 'SouthWest'), ('SouthEast', 'SouthEast'), ('SouthSouth', 'SouthSouth'), ('NorthWest', 'NorthWest'), ('NorthEast', 'NorthEast'), ('NorthCentral', 'NorthCentral')], default='Select', max_length=15)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=10)),
                ('bio', models.TextField(blank=True, max_length=150)),
                ('code', models.CharField(blank=True, max_length=6)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_type', models.CharField(choices=[('teacher', 'teacher'), ('student', 'student'), ('parent', 'parent'), ('admin', 'admin')], default='student', max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]