# Generated by Django 5.0.4 on 2024-05-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_application_contactdetails_correspondenceaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='advertisement_number',
            field=models.CharField(max_length=100),
        ),
    ]
