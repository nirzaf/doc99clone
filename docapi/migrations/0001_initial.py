# Generated by Django 3.0.5 on 2020-04-11 17:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile_No', models.CharField(max_length=20)),
                ('Category', models.CharField(max_length=200)),
                ('Is_Deleted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.TextField(max_length=256)),
                ('Telephone', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=100)),
                ('Is_Deleted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('Session_Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Date', models.DateField(default=datetime.datetime.now)),
                ('Slot_Begin', models.CharField(max_length=10)),
                ('Slot_End', models.CharField(max_length=10)),
                ('Max_Limit', models.IntegerField(default=0)),
                ('Is_Deleted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Mobile_No', models.CharField(max_length=20)),
                ('Auth_Token', models.CharField(max_length=200)),
                ('Is_Deleted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalStaff',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Address', models.TextField(max_length=256)),
                ('StaffId', models.CharField(max_length=50)),
                ('User_Type', models.IntegerField(default=0)),
                ('Is_Deleted', models.BooleanField(default=True)),
                ('Hospital_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docapi.Hospitals')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('Booking_Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Booked_By', models.IntegerField(default=0)),
                ('Is_Paid', models.BooleanField(default=False)),
                ('Is_Canceled', models.BooleanField(default=False)),
                ('Is_Deleted', models.BooleanField(default=True)),
                ('Session_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docapi.Session')),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docapi.Users')),
            ],
        ),
    ]
