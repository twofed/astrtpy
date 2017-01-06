from databases import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,Table
from sqlalchemy.sql import select


class SUser(Base):
    __tablename__ = 'sip_buddies'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    callerid = Column(String(80), unique=False)
    defaultuser= Column(String(80), unique=True)
    regexten= Column(String(80), unique=False)
    secret= Column(String(80), unique=True)
    accountcode= Column(String(20), unique=False)
    context= Column(String(80), unique=False)
    amaflags= Column(String(7), unique=False)
    callgroup= Column(String(10), unique=True)
    canreinvite= Column(String(3), unique=False)
    defaultip= Column(String(15), unique=False)
    dtmfmode= Column(String(7), unique=False)
    fromuser= Column(String(80), unique=False)
    fromdomain= Column(String(80), unique=False)
    fullcontact= Column(String(80), unique=True)
    host= Column(String(31), unique=False)
    insecure= Column(String(4), unique=False)
    mailbox= Column(String(50), unique=False)
    md5secret= Column(String(80), unique=True)
    nat= Column(String(5), unique=False)
    deny= Column(String(95), unique=False)
    permit= Column(String(95), unique=False)
    mask= Column(String(95), unique=False)
    pickupgroup= Column(String(10), unique=False)
    port= Column(String(5), unique=False)
    qualify= Column(String(3), unique=False)
    restrictcid= Column(String(1), unique=False)
    rtptimeout= Column(String(3), unique=False)
    rtpholdtimeout= Column(String(3), unique=False)
    type= Column(String(6), unique=False)
    disallow= Column(String(100), unique=False)
    allow= Column(String(100), unique=False)
    musiconhold= Column(String(100), unique=False)
    regseconds= Column(Integer, unique=False)
    ipaddr= Column(String(15), unique=False)
    cancallforward= Column(String(3), unique=False)
    lastms= Column(Integer, unique=False)
    useragent= Column(String(255), unique=False)
    regserver= Column(String(100), unique=False)
    lastmoddate= Column(DateTime, unique=False)#!
    lastmoduser= Column(String(100), unique=False)
    access= Column(String(100), unique=False)
    callbackextension= Column(String(100), unique=False)
    calllimit = Column(Integer, unique=False)

    def __init__(self, name=None, callerid=None):
        self.name = name
        self.callerid = callerid

    def __repr__(self):
        return '%s %s %s' % (self.name,self.callerid,self.fullcontact)


class TExt(Base):
    __tablename__ = 'extensions'
    id = Column(Integer, primary_key=True)
    context = Column(String(100), unique=False)
    exten = Column(String(100), unique=False)
    priority = Column(String(100), unique=False)
    app = Column(String(100), unique=False)
    appdata = Column(String(100), unique=False)
    lastmoddate= Column(DateTime, unique=False)#!
    lastmodname= Column(String(100), unique=False)
    access= Column(String(100), unique=False)

    def __init__(self, context=None):
        self.context= context

    def select(self,context):
        return select([TExt]).where(TExt.context==context).order_by('context','exten')


#class TCdr(Base):
#    _tablename__ = 'cdr'
#
#    def __init__(self, x):
#        x = None
