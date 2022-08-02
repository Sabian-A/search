from django.db import models

# Create your models here.


class PlayerRadiostation(models.Model):
    id = models.BigAutoField(primary_key=True)
    station_name = models.CharField(unique=True, max_length=100)
    station_frequency = models.FloatField()
    station_url = models.CharField(max_length=1023)
    station_cover = models.CharField(unique=True, max_length=100)
    station_description = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_radiostation'


class c(models.Model):
    id = models.BigAutoField(primary_key=True)
    station_id = models.ForeignKey(PlayerRadiostation, models.DO_NOTHING)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_radiostationfavourites'