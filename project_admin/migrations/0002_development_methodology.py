# Generated by Django 3.1.5 on 2021-01-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='development_methodology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
