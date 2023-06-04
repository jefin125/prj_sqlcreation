# Generated by Django 4.1.7 on 2023-03-21 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
