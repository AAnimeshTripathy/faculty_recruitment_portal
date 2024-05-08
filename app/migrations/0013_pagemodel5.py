# Generated by Django 5.0.4 on 2024-05-08 17:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_pagemodel4_google_scholar_link'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PageModel5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society_name', models.CharField(max_length=100)),
                ('membership_status', models.CharField(max_length=20)),
                ('training_type', models.CharField(max_length=100)),
                ('training_organisation', models.CharField(max_length=100)),
                ('training_year', models.CharField(max_length=4)),
                ('training_durations', models.IntegerField()),
                ('award_name', models.CharField(max_length=100)),
                ('awarded_by', models.CharField(max_length=100)),
                ('award_year', models.CharField(max_length=4)),
                ('sponsored_agency', models.CharField(max_length=100)),
                ('sponsored_title', models.CharField(max_length=100)),
                ('sponsored_amount', models.CharField(max_length=100)),
                ('sponsored_period', models.CharField(max_length=100)),
                ('sponsored_role', models.CharField(max_length=100)),
                ('sponsored_status', models.CharField(max_length=100)),
                ('consultancy_organisation', models.CharField(max_length=100)),
                ('consultancy_title', models.CharField(max_length=100)),
                ('consultancy_amount', models.CharField(max_length=100)),
                ('consultancy_period', models.CharField(max_length=100)),
                ('consultancy_role', models.CharField(max_length=100)),
                ('consultancy_status', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
