# Generated by Django 4.2.5 on 2024-02-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_todo_upload_image_alter_todo_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='upload_image',
        ),
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
