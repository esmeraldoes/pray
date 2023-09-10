# Generated by Django 4.2.2 on 2023-09-05 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='church',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='churches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='community',
            name='description',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='church',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_churches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='church',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='joined_communities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='joined_teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='led_teams', to=settings.AUTH_USER_MODEL),
        ),
    ]