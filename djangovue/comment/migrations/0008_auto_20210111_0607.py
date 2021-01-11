# Generated by Django 3.1.1 on 2021-01-11 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0007_auto_20210111_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type_contact',
            field=models.ForeignKey(choices=[(1, 'Business'), (2, 'School'), (3, 'Club'), (4, 'Work')], default=1, on_delete=django.db.models.deletion.CASCADE, to='comment.typecontact'),
        ),
    ]
