# Generated by Django 4.1.7 on 2023-06-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortIT_main', '0006_remove_location_locationid_remove_location_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=15, default=0.0, max_digits=18),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=15, default=0.0, max_digits=18),
        ),
    ]
