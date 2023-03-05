# Generated by Django 4.1.7 on 2023-03-03 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "room_reservation",
            "0002_rename_remployeetype_employeetype_guest_last_name_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="booking", name="booking_room",),
        migrations.AddField(
            model_name="booking",
            name="rooms",
            field=models.ManyToManyField(
                related_name="booking_room", to="room_reservation.room"
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="guest",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="booking_guest",
                to="room_reservation.guest",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="hotel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="hotel_room",
                to="room_reservation.hotel",
            ),
        ),
        migrations.DeleteModel(name="Booking_Room_Junc",),
    ]