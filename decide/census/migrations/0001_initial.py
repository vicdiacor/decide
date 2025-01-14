# Generated by Django 2.0 on 2022-01-04 17:34

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Census',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_id', models.PositiveIntegerField()),
                ('voter_id', models.PositiveIntegerField()),
                ('adscripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ParentGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('isPublic', models.BooleanField(default=False)),
                ('voters', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.PositiveIntegerField()),
                ('group_id', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED'), ('PENDING', 'PENDING')], default='PENDING', max_length=255)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='census',
            unique_together={('voting_id', 'voter_id')},
        ),
    ]
