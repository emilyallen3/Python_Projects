# Generated by Django 4.0.4 on 2022-05-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profiles_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='fname',
            field=models.CharField(blank=True, choices=[('Mrs', 'Mrs'), ('Mr', 'Mr'), ('Ms', 'Ms')], default='', max_length=50),
        ),
    ]
