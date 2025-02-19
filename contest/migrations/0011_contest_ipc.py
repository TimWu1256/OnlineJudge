from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0010_auto_20190326_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPCContestRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_submission_number', models.IntegerField(default=0)),
                ('time_cost', models.IntegerField(default=0)),
                ('memory_cost', models.IntegerField(default=0)),
                ('submission_info', jsonfield.fields.JSONField(default={})),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ipc_contest_rank',
            },
        )
    ]
