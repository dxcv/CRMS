# Generated by Django 2.1.1 on 2019-04-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0008_auto_20190427_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='跟进内容')),
                ('date', models.DateField(auto_now_add=True, verbose_name='跟进日期')),
                ('consultant', models.ForeignKey(limit_choices_to={'customer__depart__title': ['销售部', '运营部']}, on_delete='cascade', to='generic.Staffinfo', verbose_name='跟进人')),
                ('customer', models.ForeignKey(on_delete='cascade', to='generic.Customer', verbose_name='所咨询客户')),
            ],
        ),
    ]
