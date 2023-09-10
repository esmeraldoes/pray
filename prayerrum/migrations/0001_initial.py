# Generated by Django 4.2.2 on 2023-08-22 13:55

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
            name='PrayerRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_of', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(blank=True, related_name='prayer_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_heard', models.BooleanField(default=False)),
                ('is_muted', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prayers', to='prayerrum.prayerroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prayers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]