# Generated by Django 2.2.6 on 2019-10-10 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statuses.status')),
            ],
        ),
    ]
