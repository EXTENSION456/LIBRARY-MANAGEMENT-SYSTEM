# Generated by Django 2.2.5 on 2019-11-08 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_rqstbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rqstbook',
            old_name='Name',
            new_name='Username',
        ),
    ]