# Generated by Django 2.2.1 on 2019-08-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
    ]
