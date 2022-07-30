# Generated by Django 4.0.6 on 2022-07-21 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('rasm', models.FileField(blank=True, upload_to='rasmlar')),
            ],
        ),
        migrations.CreateModel(
            name='Ichki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('rasm', models.FileField(upload_to='rasmlar')),
                ('bolim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Alistyleapp.bolim')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('narx', models.PositiveSmallIntegerField()),
                ('ishlab_ch', models.CharField(max_length=100)),
                ('kafolat', models.CharField(max_length=60)),
                ('yetkazish', models.CharField(max_length=50)),
                ('mavjud', models.BooleanField(default=True)),
                ('batafsil', models.TextField()),
                ('ichki', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Alistyleapp.ichki')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='')),
                ('mahsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Alistyleapp.mahsulot')),
            ],
        ),
    ]