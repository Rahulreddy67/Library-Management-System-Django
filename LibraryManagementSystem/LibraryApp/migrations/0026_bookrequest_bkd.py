# Generated by Django 3.0 on 2023-09-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0025_auto_20230918_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='bkd',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.AddBook'),
        ),
    ]