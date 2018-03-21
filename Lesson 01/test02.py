import os
import sys
import datetime

head = '#' + '-' * 20 + '\n' + \
       '#Function desc:\n'   + \
       '#' + '-' * 20 + '\n' + \
       '#Author:lrx\n'       + \
       '#' + '-' * 20 + '\n'

desFile = sys.argv[1]
if os.path.exists(desFile) or not desFile.endswith('.py'):
    print('%s already exist or is not a .py file!' % desFile)
    sys.exit()

fp = open(desFile, 'w')
today = str(datetime.date.today())

fp.write('#-*- coding:utf8 -*-\n')
fp.write('#Filename: ' + desFile + '\n')
fp.write(head)
fp.write('#Date: ' + today + '\n')
fp.write('#' + '-' * 20 + '\n')
fp.close()
