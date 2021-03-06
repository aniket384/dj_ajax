# Generated by Django 3.1.6 on 2021-02-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('city', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'participants',
            },
        ),
    ]
