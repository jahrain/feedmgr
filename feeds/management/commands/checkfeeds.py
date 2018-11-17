import sys
import time
import logging
reload(sys)
sys.setdefaultencoding('utf-8')

from django.core.management.base import BaseCommand, CommandError
from feeds.models import *
from feeds.utils import *

logging.basicConfig(level=logging.DEBUG)
class Command(BaseCommand):
    help = 'Checks all feed subscriptions for new downloads'

    def handle(self, *args, **options):
        subs = Subscription.objects.filter(active=True)

        for sub in subs:
            finished_downloads = []
            new_downloads = []
            try:
              new_downloads = sub.get_new_downloads()
            except Exception as e:
              logging.exception(e)
            for dl in new_downloads:
                try:
                    time.sleep(5)
                    dl.start()
                except Exception as e:
                    logging.exception(e)

            for download in Download.objects.filter(subscription=sub, is_completed=False):
                print "checking", download.name
                prev_finished_status = download.is_completed
                download.update_status()
                if download.is_completed and not prev_finished_status:
                    finished_downloads.append(download)
            if len(finished_downloads):
                print "finished downloading:", "\n".join([k.name for k in finished_downloads])
                if sub.notify_user and sub.notify_user.email:
                    print "sending notification email to %s"%sub.notify_user.email
                    send_email([sub.notify_user.email], "Torrent downloads for %s completed" % sub.name,
                               "\r\n".join([k.name for k in finished_downloads]))
                    time.sleep(3)
