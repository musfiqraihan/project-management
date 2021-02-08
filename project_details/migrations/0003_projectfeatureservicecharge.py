# Generated by Django 3.1.5 on 2021-02-03 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_details', '0002_auto_20210203_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFeatureServiceCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.FloatField()),
                ('total', models.FloatField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('profile_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_details.projectdetail')),
            ],
        ),
    ]
