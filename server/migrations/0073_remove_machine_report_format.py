# Generated by Django 1.11 on 2018-04-30 14:28


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0072_auto_20180430_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='report_format',
        ),
    ]
