# Generated by Django 4.2.1 on 2023-06-18 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_id', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('users', models.ManyToManyField(related_name='guilds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuildChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('channel_type', models.IntegerField()),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discord_guilds.guild')),
            ],
        ),
        migrations.CreateModel(
            name='GuildEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.TextField(null=True)),
                ('name', models.TextField()),
                ('publish_time', models.DateTimeField()),
                ('published', models.BooleanField(default=False)),
                ('scheduled_start_time', models.DateTimeField()),
                ('scheduled_end_time', models.DateTimeField()),
                ('event_type', models.IntegerField(choices=[(1, 'Stage Instance'), (2, 'Voice'), (3, 'External')], default=1)),
                ('privacy_level', models.IntegerField(default=2)),
                ('description', models.TextField()),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discord_guilds.guild')),
            ],
        ),
        migrations.CreateModel(
            name='GuildChannelLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_users', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discord_guilds.guildchannel')),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discord_guilds.guild')),
            ],
        ),
        migrations.CreateModel(
            name='GuildAdministrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discord_id', models.CharField(max_length=255)),
                ('discord_username', models.CharField(max_length=255)),
                ('access_token', models.CharField(max_length=100)),
                ('refresh_token', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='discord_admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
