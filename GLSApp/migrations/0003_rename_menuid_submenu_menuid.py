# Generated by Django 4.2.2 on 2023-06-06 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("GLSApp", "0002_submenu"),
    ]

    operations = [
        migrations.RenameField(
            model_name="submenu",
            old_name="menuId",
            new_name="menuid",
        ),
    ]