import time
import os
from django.db import models
from django.conf import settings
from jsonfield import JSONField
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime


class Configuration(models.Model):
    name = models.CharField(default='global', max_length=40, primary_key=True)
    transmission_rpc_host = models.CharField(max_length=255)
    transmission_rpc_port = models.IntegerField()
    transmission_rpc_user = models.CharField(max_length=40)
    transmission_rpc_password = models.CharField(max_length=40)
    smtp_host = models.CharField(max_length=255, null=True, blank=True)
    smtp_port = models.IntegerField(null=True, blank=True)
    smtp_user = models.CharField(max_length=255, null=True, blank=True)
    smtp_from = models.CharField(max_length=255, null=True, blank=True)
    smtp_password = models.CharField(max_length=255, null=True, blank=True)
    smtp_title_prefix = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

class DownloadDirectory(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True)
    #location = models.FilePathField(path=settings.FEED_ROOT_PATH, max_length=1024,
    #                                allow_folders=True, allow_files=False)
    location = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name

class Subscription(models.Model):
    name = models.CharField(max_length=128, db_index=True, null=True)
    feed_url = models.URLField(max_length=1024, unique=True, db_index=True)
    filter_keywords = models.CharField(max_length=1024, null=True, blank=True)
    download_to = models.ForeignKey('DownloadDirectory')
    sub_directory = models.CharField(max_length=128, null=True, blank=True)
    last_active = models.DateTimeField(null=True)
    notify_user = models.ForeignKey(User,null=True)
    active = models.BooleanField(default=True)
    def get_new_downloads(self):
        from feeds.utils import get_download_links_from_rss
        
        
        all = get_download_links_from_rss(self.feed_url, self.filter_keywords)
        existing_map = {
           e.torrent_url: e for e in Download.objects.filter(torrent_url__in=[url for url in all])
        }
   
        new = [Download(subscription=self, torrent_url=k) for k in all if k not in existing_map]
        return new

    def __unicode__(self):
        return self.name

class Download(models.Model):
    subscription = models.ForeignKey('Subscription')
    torrent_url = models.URLField(max_length=1024, unique=True, db_index=True)
    name = models.CharField(max_length=1024, null=True)
    hash = models.CharField(max_length=255, null=True)
    is_completed = models.BooleanField(default=False, db_index=True)
    started = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True,blank=True)
    last_updated = models.DateTimeField(auto_now_add=True, auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def start(self):
        from feeds.utils import get_torrent_client
        tc = get_torrent_client()
        print "add torrent:", self.torrent_url
        t = tc.add_torrent(self.torrent_url)
        time.sleep(3)
        target_dir = self.subscription.download_to.location
        if self.subscription.sub_directory:
            target_dir = os.path.join(target_dir, self.subscription.sub_directory)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        t.move_data(target_dir)
        t.start()
        self.started = timezone.now()
        self.name = t.name
        self.hash = t.hashString
        self.save()
        self.subscription.last_active = timezone.now()
        self.subscription.save()
        time.sleep(0.5)

    def update_status(self):
        from feeds.utils import get_torrent_client
        if self.is_completed:
            return

        tc = get_torrent_client()
        torrents = {t.hashString:t for t in tc.get_torrents()}
        finished = False
        if self.hash in torrents:
            t = torrents[self.hash]
            print "Status:", t.status
            if t.status == 'seeding' or t.status == 'stopped':
                t.stop()
                time.sleep(0.5)
                tc.remove_torrent(t.id)
                finished = True
        else:
            finished = True

        if finished:
            self.subscription.last_active = timezone.now()
            self.finished = timezone.now()
            self.subscription.save()
            self.is_completed = True

        self.save()
