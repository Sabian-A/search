from django.db import models

# Create your models here.



class PlayerPodcastcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    podcast_category_title = models.CharField(unique=True, max_length=100)
    podcast_category_cover = models.CharField(unique=True, max_length=100)
    podcast_category_description = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_podcastcategory'


class PlayerPodcastepisode(models.Model):
    id = models.BigAutoField(primary_key=True)
    episode_title = models.CharField(unique=True, max_length=100)
    episode_description = models.TextField(blank=True, null=True)
    episode_file = models.CharField(unique=True, max_length=100)
    episode_status = models.BooleanField()
    episode_release_date = models.DateTimeField()
    host_id = models.ForeignKey('PlayerPodcasthost', models.DO_NOTHING)
    season_id = models.ForeignKey('PlayerPodcastseason', models.DO_NOTHING)
    podcast_category_id = models.ForeignKey(PlayerPodcastcategory, models.DO_NOTHING)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_podcastepisode'


class PlayerPodcastfavourites(models.Model):
    id = models.BigAutoField(primary_key=True)
    episode_id = models.ForeignKey(PlayerPodcastepisode, models.DO_NOTHING)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_podcastfavourites'


class PlayerPodcasthost(models.Model):
    id = models.BigAutoField(primary_key=True)
    host_name = models.CharField(unique=True, max_length=100)
    host_title = models.CharField(max_length=100)
    host_cover = models.CharField(unique=True, max_length=100)
    host_description = models.TextField(blank=True, null=True)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_podcasthost'


class PlayerPodcastplaylist(models.Model):
    id = models.BigAutoField(primary_key=True)
    playlist_name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_podcastplaylist'


class PlayerPodcastplaylistepisodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    playlist_id = models.ForeignKey(PlayerPodcastplaylist, models.DO_NOTHING)
    episode_id = models.ForeignKey(PlayerPodcastepisode, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_podcastplaylistepisodes'


class PlayerPodcastseason(models.Model):
    id = models.BigAutoField(primary_key=True)
    season_title = models.CharField(unique=True, max_length=100)
    season_cover = models.CharField(unique=True, max_length=100)
    season_description = models.TextField(blank=True, null=True)
    host_id = models.ForeignKey(PlayerPodcasthost, models.DO_NOTHING)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_podcastseason'