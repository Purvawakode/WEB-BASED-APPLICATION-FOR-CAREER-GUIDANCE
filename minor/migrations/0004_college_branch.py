# Generated by Django 3.2.8 on 2021-11-08 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0003_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='minor.branch'),
            preserve_default=False,
        ),
    ]
