# Generated by Django 3.2.8 on 2021-10-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=100)),
                ('DateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]