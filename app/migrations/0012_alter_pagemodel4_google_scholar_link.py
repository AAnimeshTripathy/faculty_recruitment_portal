# Generated by Django 5.0.4 on 2024-05-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_pagemodel4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemodel4',
            name='google_scholar_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
