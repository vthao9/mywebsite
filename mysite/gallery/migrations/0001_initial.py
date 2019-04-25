# Generated by Django 2.1.7 on 2019-04-18 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('imagefile', models.ImageField(null=True, upload_to='images/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='PersonUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Image')),
            ],
        ),
    ]
