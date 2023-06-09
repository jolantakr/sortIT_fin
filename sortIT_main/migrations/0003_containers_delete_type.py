# Generated by Django 4.1.7 on 2023-06-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortIT_main', '0002_type_alter_category_id_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Containers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('detail1_name', models.CharField(max_length=100)),
                ('detail1_description', models.TextField()),
                ('detail2_name', models.CharField(max_length=100)),
                ('detail2_description', models.TextField()),
                ('detail3_name', models.CharField(max_length=100)),
                ('detail3_description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
