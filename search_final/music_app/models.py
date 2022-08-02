from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class PlayerMusicalbum(models.Model):
    id = models.BigAutoField(primary_key=True)
    album_title = models.CharField(unique=True, max_length=100)
    album_cover = models.CharField(unique=True, max_length=100)
    album_description = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    artist_id = models.ForeignKey('PlayerMusicartist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_musicalbum'


class PlayerMusicartist(models.Model):
    id = models.BigAutoField(primary_key=True)
    artist_name = models.CharField(unique=True, max_length=100)
    artist_title = models.CharField(max_length=100)
    artist_cover = models.CharField(unique=True, max_length=100)
    artist_description = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_musicartist'


class PlayerMusicfavourites(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    track_id = models.ForeignKey('PlayerMusictrack', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_musicfavourites'


class PlayerMusicgenre(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_title = models.CharField(unique=True, max_length=100)
    genre_cover = models.CharField(unique=True, max_length=100)
    genre_description = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_musicgenre'


class PlayerMusiclyrics(models.Model):
    id = models.BigAutoField(primary_key=True)
    lyrics_title = models.CharField(max_length=100)
    lyrics_detail = models.TextField(unique=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    track_id = models.OneToOneField('PlayerMusictrack', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_musiclyrics'


class PlayerMusicplaylist(models.Model):
    id = models.BigAutoField(primary_key=True)
    playlist_name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_musicplaylist'


class PlayerMusicplaylisttracks(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    playlist_id = models.ForeignKey(PlayerMusicplaylist, models.DO_NOTHING)
    track_id = models.ForeignKey('PlayerMusictrack', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_musicplaylisttracks'


class PlayerMusictrack(models.Model):
    id = models.BigAutoField(primary_key=True)
    track_name = models.CharField(unique=True, max_length=100)
    track_description = models.TextField(blank=True, null=True)
    track_file = models.CharField(unique=True, max_length=100)
    track_status = models.BooleanField()
    track_release_date = models.DateTimeField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    album_id = models.ForeignKey(PlayerMusicalbum, models.DO_NOTHING)
    artist_id = models.ForeignKey(PlayerMusicartist, models.DO_NOTHING)
    genre_id = models.ForeignKey(PlayerMusicgenre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_musictrack'
