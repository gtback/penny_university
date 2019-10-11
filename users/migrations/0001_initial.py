# Generated by Django 2.2.6 on 2019-10-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    state_operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('slack_id', models.CharField(max_length=100, unique=True)),
                ('user_name', models.CharField(max_length=100)),
                ('real_name', models.CharField(max_length=100)),
                ('metro_name', models.CharField(max_length=200)),
                ('topics_to_learn', models.CharField(max_length=1500)),
                ('topics_to_share', models.CharField(max_length=1500)),
                ('how_you_learned_about_pennyu', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=None,
            state_operations=state_operations,
        ),
    ]
