# Generated by Django 4.0.4 on 2022-05-18 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_profiles_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='fname',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], default='', max_length=50),
        ),
    ]