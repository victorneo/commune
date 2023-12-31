# Generated by Django 4.2.1 on 2023-06-20 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discord_guilds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False)),
                ('publish_time', models.DateTimeField()),
                ('guild_channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discord_guilds.guildchannel')),
            ],
        ),
    ]
