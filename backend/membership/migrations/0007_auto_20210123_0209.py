# Generated by Django 3.1.5 on 2021-01-23 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("membership", "0006_auto_20210122_1704")]

    operations = [
        migrations.AddField(
            model_name="member", name="email_address", field=models.EmailField(blank=True, max_length=100, null=True)
        ),
        migrations.AlterField(
            model_name="member",
            name="ministry",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="membership.ministry"
            ),
        ),
    ]