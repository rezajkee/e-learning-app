# Generated by Django 4.1.4 on 2022-12-21 10:37

from django.db import migrations
import educa.courses.fields


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_video_text_image_file_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="content",
            options={"ordering": ["order"]},
        ),
        migrations.AlterModelOptions(
            name="module",
            options={"ordering": ["order"]},
        ),
        migrations.AddField(
            model_name="content",
            name="order",
            field=educa.courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="module",
            name="order",
            field=educa.courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]