# Generated by Django 4.0.4 on 2022-05-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_alter_profiles_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='fname',
            field=models.CharField(blank=True, choices=[('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Mr', 'Mr')], default='', max_length=50),
        ),
    ]
