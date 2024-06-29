# Generated by Django 5.0.4 on 2024-06-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbluser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=10, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=50, null=True)),
                ('mailid', models.CharField(blank=True, max_length=50, null=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
