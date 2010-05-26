# -*- coding: utf-8 -*-

import os, sys
import glob
from ConfigParser import ConfigParser

def get_feeds_settings():
    config_files = glob.glob('%s/conf/*.conf' % (os.path.abspath(sys.path[0])))

    feeds = []

    for config_file in config_files:
        config = ConfigParser()
        config.read(config_file)

        feed_dict = {
            'url': config.get('General', 'URL'),
            'torrent_path': config.get('General', 'TorrentPath'),
        }

        feeds.append(feed_dict)

    return feeds

