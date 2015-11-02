#!/usr/bin/python
import time


file = open('/home/frutkic/cronjobs/output.txt', 'a')
file.write(time.ctime() + '\n')
file.close()
