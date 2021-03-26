# Generated by Django 3.1.7 on 2021-03-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('defaultmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='car_detailing.defaultmodel')),
                ('name', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(blank=True, max_length=11, null=True)),
                ('category', models.CharField(choices=[('eventual', 'Eventual'), ('frequent', 'Frequente'), ('premium', 'Premium')], default='eventual', max_length=20)),
            ],
            bases=('car_detailing.defaultmodel',),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('defaultmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='car_detailing.defaultmodel')),
                ('brand_model', models.CharField(max_length=50)),
                ('license_plate', models.CharField(blank=True, max_length=15, null=True)),
                ('color_code', models.CharField(blank=True, max_length=30, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_detailing.client')),
            ],
            bases=('car_detailing.defaultmodel',),
        ),
    ]
