# Generated by Django 5.0.4 on 2024-05-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_pagemodel8_delete_page8'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageModel9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declaration_agreed', models.BooleanField(default=False)),
            ],
        ),
    ]
