# Generated by Django 4.0.3 on 2022-04-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0003_alter_user_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='passsword',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
