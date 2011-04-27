#!/usr/bin/env python
'''
A Jabber spam bot when your pesty coworker feels left out
and just needs some jabber messages to cheer em up.

!!!!CAUTION!!!! Can cause certain Jabber clients to crash making it quite
annoying.
'''

import xmpp
import sys
import random

f = open('randomlist.lst', 'r+')
pfile = f.read()
wlist = pfile.split('\n')

server = 'example.jabber.org'
username = 'the_spammer'
password = 'spammer_pass'
jid_resource = 'SpamBot'
tojid = 'target@exmple.jabber.org'

conn = xmpp.Client(server)
conn.connect()
auth = conn.auth(username, password, resource=jid_resource)
if not auth:
    print "Could not Authenticate!"
    sys.exit()

# Do a loop and do some conn.sends()
while 1:
    rand = random.randint(1, len(wlist)-1)
    msg = wlist[rand]
    if len(msg)  < 12:
        msg += wlist[random.randint(1, len(wlist)-1)]
    if len(msg) < 40:
        msg += wlist[random.randint(1, len(wlist)-1)]
    conn.send(xmpp.protocol.Message(tojid, msg))

