# Generated by Django 3.2.13 on 2022-12-16 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('Barbering', 'Barbering'), ('Bear Trimming', 'Bear Trimming'), ('Wash, Cut and style', 'Wash, Cut and style'), ('Fades', 'Fades'), ('Line Ups', 'Line Ups'), ('Head Shave', 'Head Shave'), ('Scalp Treatment', 'Scalp Treatment'), ('Colour', 'Colour'), ('Kids', 'Kids')], default='Doctor care', max_length=50),
        ),
    ]
