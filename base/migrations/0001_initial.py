# Generated by Django 3.2.12 on 2024-06-21 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('bus_id', models.CharField(db_index=True, max_length=4, primary_key=True, serialize=False, unique=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('line_number', models.CharField(db_index=True, max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='OrdinATAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.line')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('passenger_id', models.CharField(db_index=True, max_length=12, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('stop_id', models.CharField(db_index=True, max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('latitude', models.FloatField(max_length=10)),
                ('longitude', models.FloatField(max_length=10)),
                ('lines', models.ManyToManyField(through='base.OrdinATAC', to='base.Line')),
            ],
        ),
        migrations.AddField(
            model_name='ordinatac',
            name='stop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.stop'),
        ),
        migrations.AddField(
            model_name='line',
            name='stops',
            field=models.ManyToManyField(through='base.OrdinATAC', to='base.Stop'),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.CharField(db_index=True, max_length=12, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('assigned_bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.bus')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.line'),
        ),
        migrations.AddField(
            model_name='bus',
            name='passengers',
            field=models.ManyToManyField(to='base.Passenger'),
        ),
    ]
