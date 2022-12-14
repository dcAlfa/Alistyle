# Generated by Django 4.0.6 on 2022-07-30 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Userapp', '0002_alter_account_user'),
        ('Alistyleapp', '0002_mahsulot_chegirma_alter_ichki_bolim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tanlangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.account')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alistyleapp.mahsulot')),
            ],
        ),
        migrations.CreateModel(
            name='Savat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('narx', models.PositiveSmallIntegerField()),
                ('chegirma', models.PositiveSmallIntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.account')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alistyleapp.mahsulot')),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('mah_narx', models.PositiveSmallIntegerField()),
                ('yet_narx', models.PositiveSmallIntegerField()),
                ('umumiy_narx', models.PositiveSmallIntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.account')),
                ('savat', models.ManyToManyField(to='Ichkiapp.savat')),
            ],
        ),
    ]
