# Generated by Django 4.2.5 on 2024-02-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='upload_image',
            field=models.ImageField(blank=True, null=True, upload_to='todo_images/'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(default='Default Description'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], max_length=2),
        ),
    ]
