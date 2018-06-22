# Generated by Django 2.0.6 on 2018-06-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testdb',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'stud',
                'ordering': ['roll'],
            },
        ),
    ]
