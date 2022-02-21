from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                # ('num', models.IntegerField(blank=True, null=True)),
                # ('url', models.IntegerField(blank=True, null=True)),
                # ('memo', models.IntegerField(blank=True, null=True)),
                ('num', models.AutoField(primary_key=True)),
                ('url',  models.IntegerField(blank=True, null=True)),
                ('memo',  models.CharField(max_length=50, blank=True, null=True)),
            ],
            options={
                'db_table': 'photo',
                'managed': False,
            },
        ),
    ]
