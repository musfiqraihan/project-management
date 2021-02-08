# Generated by Django 3.1.5 on 2021-02-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_details', '0005_clientprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('profile_name', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=50)),
                ('completion_date', models.CharField(max_length=50)),
                ('update_completion_date', models.DateField(auto_now_add=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
