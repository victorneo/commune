# Generated by Django 4.2.1 on 2023-06-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordGuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_id', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
