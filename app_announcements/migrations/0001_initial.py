# Generated by Django 5.0.6 on 2024-05-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllAnnouncements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_published', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('descriptions', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'All Announcements',
            },
        ),
    ]
