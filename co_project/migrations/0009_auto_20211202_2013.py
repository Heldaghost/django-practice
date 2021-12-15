# Generated by Django 3.2.7 on 2021-12-02 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo_hosting', '0008_auto_20211126_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='slug',
        ),
        migrations.AlterField(
            model_name='posts',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo_hosting.collections'),
        ),
    ]