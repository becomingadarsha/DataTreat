# Generated by Django 2.1.5 on 2019-01-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_detect', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='dtype',
            field=models.CharField(default=int, max_length=50),
            preserve_default=False,
        ),
    ]
