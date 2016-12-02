#!/usr/bin/env python
# -*- coding: utf-8 -*-
# root  root  root root123
import pexpect
import os
from getpass import getpass
from operator import itemgetter
computer=[{'name':'core','ip':'192.168.1.106','user':'root','passwd':'root'},
          {'name':'web','ip':'192.168.1.107','user':'root','passwd':'root123'}
          ]
def sshcon(user,ip,mypassword,cmd):
    child = pexpect.spawn('ssh %s@%s' % (user, ip))
    child.expect('password:')
    child.sendline(mypassword)
    child.expect('#')
    child.sendline(cmd)
    child.expect('#')
    print(child.before)
def scpcon(user,ip , passwd, filename, dst_path):
        passwd_key = '.*assword.*'
        if os.path.isdir(filename):
                cmdline = 'scp -r %s %s@%s:%s' % (filename, user, ip, dst_path)
        else:
                cmdline = 'scp %s %s@%s:%s' % (filename, user, ip, dst_path)
        try:
                child = pexpect.spawn(cmdline)
                child.expect(passwd_key)
                child.sendline(passwd)
                child.expect(pexpect.EOF)
                # child.interact()
                # child.read()
                child.expect('$')
                print('uploading')
                print('finsh')
        except:
                print('upload faild!')


        #
# def ssh_cmd(user,ip,passwd,cmd):
#         ssh = pexpect.spawn('ssh %s@%s' % (user, ip))
#         try:
#                 i=ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=30)
#                 if i==0:
#                         ssh.sendline(passwd)
#                 elif i == 1:
#                         ssh.sendline('yes')
#                         ssh.expect('password: ')
#                         ssh.sendline(passwd)
#                 try:
#                         ssh.expect('#')
#                         ssh.sendline(cmd)
#                 except :
#                         print('cmd,error')
#         except pexpect.EOF:
#                 print('login,EOF')
#         except pexpect.TIMEOUT:
#                 print('login,TIMEOUT')
#         else:
#                 r=ssh.read()
#                 print(r)

# def ssh_cmd(user,ip, cmd):
#         ssh = pexpect.spawn('ssh %s@%s "%s"' % (user,ip,cmd))
#         try:
#                 i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=30)
#                 if i == 0 :
#                         ssh.sendline(passwd)
#                 elif i == 1:
#                         ssh.sendline('yes')
#                         ssh.expect('password: ')
#                         ssh.sendline(passwd)
#         except pexpect.EOF:
#                 print ('EOF')
#         except pexpect.TIMEOUT:
#                 print ('TIMEOUT')
#         else:
#                 r = ssh.read()
#
#                 print (r)
#                 print(ssh.before)
#         ssh.close()

#
# def scp_cmd(file, user,ip ):
#         ssh = pexpect.spawn('scp %s %s@%s:~/' % (file, user, ip))
#         try:
#                 i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=30)
#                 if i == 0:
#                         ssh.sendline(passwd)
#                 elif i == 1:
#                         ssh.sendline('yes')
#                         ssh.expect('password: ')
#                         ssh.sendline(passwd)
#         except pexpect.EOF:
#                 print('EOF')
#         except pexpect.TIMEOUT:
#                 print('TIMEOUT')
#         else:
#                 r = ssh.read()
#
#                 print(r)
#                 print(ssh.before)
#         ssh.close()
# computer_by_name=sorted(computer,key=itemgetter('name'))

if __name__ == '__main__':
        #computer0,core
        if computer[0]['name']=='core':
                scpcon(computer[0]['user'],computer[0]['ip'],computer[0]['passwd'], '/home/g/myth/test1.txt', '~/')
                # sshcon(computer[0]['user'],computer[0]['ip'],computer[0]['passwd'],'ps -aux | grep java | awk \'{print $2}\'')
        # #computer1,
        # if computer[1]['name']=='core'
        #
        # sshcon(computer[1]['user'], computer[1]['ip'], computer[1]['passwd'],'ps -aux | grep java | awk \'{print $2}\'')
        # print(computer_by_name)t
        # print(computer[0]['name'])
        # print(computer[0][1])
        #
        # 传递值
        # file=open("/home/g/myth/test1.txt",'r')
        # a = file.read()
        # file.close()
        # for host in a.split("\n"):
        #         if host:
        #                 user,ip,cmd = host.split(",")
        #                 print ('-- %s run:%s --' % (ip, 'ps -aux'))

