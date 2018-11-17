import transmissionrpc
import smtplib
import feedparser
import requests
from fnmatch import fnmatch

def send_email(recipients, subject, body):
    from feeds.models import Configuration
    conf = Configuration.objects.get(name='global')

    if conf.smtp_title_prefix:
        subject = conf.smtp_title_prefix + subject

    message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (
        conf.smtp_from, ", ".join(recipients), subject, body)
    server = smtplib.SMTP(conf.smtp_host, conf.smtp_port)
    server.ehlo()
    server.starttls()
    if conf.smtp_user:
        server.login(conf.smtp_user, conf.smtp_password)

    server.sendmail(conf.smtp_user, recipients, message)
    server.close()


def get_torrent_client():
    from feeds.models import Configuration
    conf = Configuration.objects.get(name='global')
    tc = transmissionrpc.Client(
        conf.transmission_rpc_host,
        port=conf.transmission_rpc_port,
        user=conf.transmission_rpc_user,
        password=conf.transmission_rpc_password)

    return tc

def get_download_links_from_rss(feed_url, filter_keys=None):
    #print "get feed from url:", feed_url
    data = requests.get(feed_url)
    fp = feedparser.parse(data.text)

    dl_list = []
    for i in xrange(len(fp['entries'])):
        if filter_keys != None and len(filter_keys):
            title = fp['entries'][i].get('title')
            #print "Title:", title
            if not fnmatch(title.lower(), filter_keys.lower()):
                continue
        magneturi =  fp['entries'][i].get('magneturi')
        if magneturi:
            dl_list.append(magneturi)
            continue
        links = fp['entries'][i]['links']
        foundone = False
        for j in xrange(len(links)):
            if 'torrent' in links[j]['type']:
                dl_list.append(links[j]['href'])
                #print 'found torrent link:', links[j]['href']
                foundone = True
                break
        if not foundone:
            dl_list.append(links[0]['href'])

    #for i in range(len(dl_list)):
    #    if dl_list[i].startswith('https'):
    #        dl_list[i] = 'http'+dl_list[i][5:]
    return dl_list

