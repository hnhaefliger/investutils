from ftplib import FTP
import requests
import random
import warnings


def get_nasdaq_listed():
    listed = []

    def callback(f):
        listed.append(f.decode('UTF-8'))

    ftp = FTP('ftp.nasdaqtrader.com')
    ftp.login()
    ftp.cwd('SymbolDirectory')

    ftp.retrbinary('RETR nasdaqlisted.txt', callback)

    listed = ''.join(listed)
    listed = listed.split('\n')
    listed = [line.split('|')[0] for line in listed][1:-1]

    return listed


def get_other_listed():
    listed = []

    def callback(f):
        listed.append(f.decode('UTF-8'))

    ftp = FTP('ftp.nasdaqtrader.com')
    ftp.login()
    ftp.cwd('SymbolDirectory')

    ftp.retrbinary('RETR otherlisted.txt', callback)

    listed = ''.join(listed)
    listed = listed.split('\n')
    listed = [line.split('|')[0] for line in listed][1:-1]

    return listed


def get_all_listed():
    return list(set(get_other_listed() + get_nasdaq_listed()))
