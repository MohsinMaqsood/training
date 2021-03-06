# Generated by Django 2.2.1 on 2019-05-27 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Offices', '0006_property_detail_one_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_detail',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='property_detail',
            name='price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='property_subdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_space_title', models.CharField(blank=True, max_length=30000, null=True)),
                ('subspace_detail', models.CharField(blank=True, max_length=30000, null=True)),
                ('subspace_detail_tag', models.CharField(blank=True, max_length=30000, null=True)),
                ('subspace_pics', models.CharField(blank=True, max_length=30000, null=True)),
                ('propertylink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Offices.property_detail')),
            ],
        ),
    ]
