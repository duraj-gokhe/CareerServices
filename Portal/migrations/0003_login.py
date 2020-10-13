# Generated by Django 3.1.2 on 2020-10-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0002_auto_20201005_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('CreateDateTime', models.DateTimeField(auto_now_add=True)),
                ('LastUpdateDateTime', models.DateTimeField(auto_now_add=True)),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.person')),
            ],
        ),
    ]
