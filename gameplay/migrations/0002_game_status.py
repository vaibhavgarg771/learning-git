# Generated by Django 2.2.7 on 2019-12-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('f', 'First players to move'), ('s', 'Second players to move'), ('w', 'First player won the game'), ('l', 'Second player won the game'), ('d', 'The was drawn')], default='f', max_length=1),
        ),
    ]