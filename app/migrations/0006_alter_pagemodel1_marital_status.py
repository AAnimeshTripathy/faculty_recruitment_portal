# Generated by Django 5.0.4 on 2024-05-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_pagemodel1_remove_contactdetails_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemodel1',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], max_length=20),
        ),
    ]
