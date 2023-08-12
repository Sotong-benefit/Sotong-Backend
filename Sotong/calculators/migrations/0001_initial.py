# Generated by Django 4.2.4 on 2023-08-11 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marry', models.IntegerField(verbose_name='여행경비')),
                ('welfare', models.IntegerField(verbose_name='복지 자격 여부')),
                ('income_myself', models.IntegerField(verbose_name='본인 소득')),
                ('imcome_fam', models.IntegerField(verbose_name='가구원 소득')),
                ('house', models.IntegerField(verbose_name='주택,건축물')),
                ('land', models.IntegerField(verbose_name='토지')),
                ('rental_deposit', models.IntegerField(verbose_name='임차 보증금')),
                ('property', models.IntegerField(verbose_name='기타 재산')),
                ('car', models.IntegerField(verbose_name='차량 가격')),
                ('finance', models.IntegerField(verbose_name='금융 재산')),
                ('dept', models.IntegerField(verbose_name='부채')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
