# Generated by Django 2.2.7 on 2019-12-10 10:54

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
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('first_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_player_of_game', to=settings.AUTH_USER_MODEL)),
                ('second_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_player_of_game', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('by_first_player', models.BooleanField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game')),
            ],
        ),
    ]
