# Generated by Django 2.1.15 on 2020-04-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=30)),
                ('team_name', models.CharField(max_length=30)),
                ('player_stat', models.IntegerField()),
            ],
        ),
    ]
