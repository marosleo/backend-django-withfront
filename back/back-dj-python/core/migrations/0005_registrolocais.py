# Generated by Django 4.0.6 on 2022-08-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_tag_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrolocais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
            ],
        ),
    ]
