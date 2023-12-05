from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('trade_code', models.CharField(max_length=255)),
                ('high', models.CharField(max_length=255)),
                ('low', models.CharField(max_length=255)),
                ('open', models.CharField(max_length=255)),
                ('close', models.CharField(max_length=255)),
                ('volume', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Data',
            },
        ),
    ]