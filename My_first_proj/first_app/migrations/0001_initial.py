# Generated by Django 4.2.7 on 2023-11-18 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='musician',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=20)),
                ('instrument', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.musician')),
            ],
        ),
    ]
