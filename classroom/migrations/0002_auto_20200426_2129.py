# Generated by Django 2.2.7 on 2020-04-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='contact_day',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')], default='monday', max_length=100),
        ),
        migrations.AddField(
            model_name='mentor',
            name='contact_time',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], default='morning', max_length=100),
        ),
        migrations.AddField(
            model_name='mentor',
            name='country',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='current_occupation',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='github',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='phone_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='contact_day',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')], default='monday', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='contact_time',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], default='morning', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='current_occupation',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='linkedin',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='account_num',
            field=models.IntegerField(blank=True, default=1234, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='bank_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='billing_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='branch_code',
            field=models.IntegerField(blank=True, default=1234, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='linkedin',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]