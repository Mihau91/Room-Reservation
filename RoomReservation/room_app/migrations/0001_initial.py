# Generated by Django 4.0.6 on 2022-07-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255)),
                ('room_capacity', models.PositiveIntegerField()),
                ('projector_availability', models.BooleanField(default=False)),
            ],
        ),
    ]