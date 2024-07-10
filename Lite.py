#coding=utf-8
import os, sys, platform
os.system('rm -rf rkb')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf rkb')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('rkb'):
        os.system('chmod 777 rkb;./rkb')
    else:
        os.system('chmod 777 rkb;./rkb')
