# Generated by Django 3.1.1 on 2021-01-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_contact_type_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typecontact',
            name='name',
            field=models.CharField(choices=[(1, 'Business'), (2, 'School'), (3, 'Club'), (4, 'Work')], default=1, max_length=50),
        ),
    ]