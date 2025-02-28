# Generated by Django 5.0.6 on 2024-05-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_datetime', models.DateTimeField()),
                ('news_name', models.CharField(max_length=255)),
                ('news_description', models.TextField()),
                ('news_text', models.TextField()),
                ('news_photo', models.ImageField(upload_to='news_photos/')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
