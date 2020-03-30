from argparse import ArgumentParser
from os import path
from random import randint
from subprocess import call
from subprocess import getoutput as shell
from sys import exit
from threading import Thread
from time import sleep

from core.browser import Browser
from core.queue import Queue
from core.tor import Tor


class Views(Browser, Tor):

    def __init__(self, urllist, visits, min, max):

        self.bots = 5 # max amount of bots to use
        self.count = 0 # returning bots
        self.ip = None
        self.alive = True
        self.targets = {} # {url: visits}
        self.recentIPs = Queue(10)

        self.min = int(min)
        self.max = int(max)
        self.visits = int(visits)

        if not path.exists(urllist):
            exit('Error: Unable to locate `{}`'.format(urllist))

        # read the url list
        with open(urllist, 'r') as f:
            try:
                for url in [_ for _ in f.read().split('\n') if _]:
                    self.targets[url] = 0 # initial view
            except Exception as err:exit('Error:', err)

    def display(self, url):
        n = '\033[0m'  # null ---> reset
        r = '\033[31m' # red
        g = '\033[32m' # green
        y = '\033[33m' # yellow
        b = '\033[34m' # blue

        call('clear')
        print('')
        print('  +------ Youtube Views ------+')
        print('  [-] Url: {}{}{}'.format(g, url, n))
        print('  [-] Proxy IP: {}{}{}'.format(b, self.ip, n))
        print('  [-] Visits: {}{}{}'.format(y, self.targets[url], n))
