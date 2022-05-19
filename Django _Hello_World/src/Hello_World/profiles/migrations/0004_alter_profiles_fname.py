# Generated by Django 4.0.4 on 2022-05-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profiles_fname_alter_profiles_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='fname',
            field=models.CharField(blank=True, choices=[('Ms', 'Ms'), ('Mr', 'Mr'), ('Mrs', 'Mrs')], default='', max_length=50),
        ),
    ]