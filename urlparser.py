#!/usr/bin/python
import os
import re


def url_parser():
    os.chdir('/home/frutkic/cronjobs/files')
    files = os.listdir('/home/frutkic/cronjobs/files')
    urls = set()
    for filename in files:
        with open(filename, 'r') as file:
            text = file.read()
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
            for x in url:
                urls.add(x)
    with open('/home/frutkic/cronjobs/out.txt', 'w') as output:
        for url in urls:
            output.write(url + '\n')


if __name__ == '__main__':
    url_parser()
