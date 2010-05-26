# -*- coding: utf-8 -*-

import feedparser
from lib.settings import get_feeds_settings

feeds = get_feeds_settings()
feeds_history = []

for feed in feeds:
    stats = {'d': 0, 'r': 0, 'f': 0}
    print 'Reading %s with Last-Modified %s' % (feed['url'], 'TODO')
    d = feedparser.parse(feed['url'])
    print '%s, %d new entries' % (d['feed']['subtitle'], len(d['entries']))

    for feed_entry in d['entries']:
        torrent_url = feed_entry['links'][0]['href']
        print 'Processing %s' % (torrent_url)

        if torrent_url not in feeds_history:
            try:
                stats['d'] += 1
                print '          + Downloaded'

            except:
                stats['f'] += 1
                print '          * Failed'

        else:
            stats['r'] += 1
            print '              - Repeated'

