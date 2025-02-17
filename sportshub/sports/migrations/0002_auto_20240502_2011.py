# Generated by Django 3.2.7 on 2024-05-02 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=100)),
                ('stu_class', models.CharField(max_length=100)),
                ('stu_rollno', models.CharField(max_length=20)),
                ('registration_number', models.CharField(max_length=10, unique=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.event')),
            ],
        ),
    ]
