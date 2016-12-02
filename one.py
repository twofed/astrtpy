from flask import Flask,render_template, request,jsonify,abort,Response, jsonify
from jinja2 import TemplateNotFound
import databases
import simplejson as json
import tables

app = Flask(__name__, template_folder='templates')
conn = databases.engine.connect()

@app.route('/')
def form():
    return render_template('form_submit.html')


@app.route('/search/', methods=['POST'])
def search():

    name=request.form['yourname']
    sip_user_result=tables.SUser.query.filter(tables.SUser.name == name).first()
    check=request.form['check']
    try:
        sip_user_result.name==name
    except AttributeError:
        return render_template('form_submit.html',error='not found')
    if (check=='2'):

        return render_template('table_sip.html',id=sip_user_result.id
                           , accountcode= sip_user_result.accountcode
                           , disallow= sip_user_result.disallow
                           , allow= sip_user_result.allow
                           #, allowoverlap= sip_user_result.allowoverlap
                           #, allowsubscribe= sip_user_result.allowsubscribe
                           #, allowtransfer= sip_user_result.allowtransfer
                           , amaflags= sip_user_result.amaflags
                           #, autoframing= sip_user_result.autoframing
                           #, auth= sip_user_result.auth
                           #, buggymwi= sip_user_result.buggymwi
                           , callgroup= sip_user_result.callgroup
                           , callerid= sip_user_result.callerid
                           #, cid_number= sip_user_result.cid_number
                           #, fullname= sip_user_result.fullname
                           , calllimit= sip_user_result.calllimit
                           #, callingpres= sip_user_result.callingpres
                           , canreinvite= sip_user_result.canreinvite
                           , context= sip_user_result.context
                           , defaultip= sip_user_result.defaultip
                           , dtmfmode= sip_user_result.dtmfmode
                           , fromuser= sip_user_result.fromuser
                           , fromdomain= sip_user_result.fromdomain
                           , fullcontact= sip_user_result.fullcontact
                           #, g726nonstandard= sip_user_result.g726nonstandard
                           , host= sip_user_result.host
                           , insecure= sip_user_result.insecure
                           , ipaddr= sip_user_result.ipaddr
                           #, language= sip_user_result.language
                           , lastms= sip_user_result.lastms
                           , mailbox= sip_user_result.mailbox
                           #, maxcallbitrate= sip_user_result.maxcallbitrate
                           #, mohsuggest= sip_user_result.mohsuggest
                           , md5secret= sip_user_result.md5secret
                           , name= sip_user_result.name
                           , nat= sip_user_result.nat
                           #, outboundproxy= sip_user_result.outboundproxy
                           , deny= sip_user_result.deny
                           , permit= sip_user_result.permit
                           , pickupgroup= sip_user_result.pickupgroup
                           , port= sip_user_result.port
                           #, progressinband= sip_user_result.progressinband
                           #, promiscredir= sip_user_result.promiscredir
                           , qualify= sip_user_result.qualify
                           , regexten= sip_user_result.regexten
                           , regseconds= sip_user_result.regseconds
                           #, rfc2833compensate= sip_user_result.rfc2833compensate
                           , rtptimeout= sip_user_result.rtptimeout
                           , rtpholdtimeout= sip_user_result.rtpholdtimeout
                           , secret= sip_user_result.secret
                           #, setvar= sip_user_result.setvar
                           #, subscribecontext= sip_user_result.subscribecontext
                           #, subscribemwi= sip_user_result.subscribemwi
                           #, t38pt_udptl= sip_user_result.t38pt_udptl
                           #, trustrpid= sip_user_result.trustrpid
                           , type= sip_user_result.type
                           #, useclientcode= sip_user_result.useclientcode
                           #, username= sip_user_result.username
                           #, usereqphone= sip_user_result.usereqphone
                           #, videosupport= sip_user_result.videosupport
                           #, vmexten= sip_user_result.vmexten
                           , lastmoddate= sip_user_result.lastmoddate
                           , lastmoduser= sip_user_result.lastmoduser
                           , access= sip_user_result.access)
    else:
        return render_template('short_sip.html',id= sip_user_result.id
                           , name= sip_user_result.name
                           , secret= sip_user_result.secret
                           , host= sip_user_result.host
                           , type= sip_user_result.type
                           , callerid= sip_user_result.callerid
                           , accountcode= sip_user_result.accountcode
                           , allow= sip_user_result.allow
                           , calllimit= sip_user_result.calllimit
                           , nat= sip_user_result.nat
                           , permit= sip_user_result.permit
                           , deny= sip_user_result.deny
                           , ipaddr= sip_user_result.ipaddr
                           , port= sip_user_result.port
                           , fullcontact= sip_user_result.fullcontact
                           , lastms= sip_user_result.lastms
                           , regseconds= sip_user_result.regseconds
                           , lastmoddate= sip_user_result.lastmoddate
                           , lastmoduser= sip_user_result.lastmoduser
                           , access= sip_user_result.access)
@app.route('/palette/', methods=['POST'])
def table():
    global iterat
    get_context=request.form['context']
    r1= tables.TExt().select(get_context)
    res = conn.execute(r1)
    i=0
    for result in res:
        i=1
        json_res = {}
        json_res['id'] = result['id']
        json_res['context'] = result['context']
        json_res['exten'] = result['exten']
        json_res['priority'] = result['priority']
        json_res['app'] = result['app']
        json_res['appdata'] = result['appdata']
        json_res['lastmodname'] = result['lastmodname']
        json_res['lastmoddate'] = result['lastmodname']
        json_res['access'] = result['access']
        json_send =json.dumps(json_res)
    print json_send
    return render_template('palette.html',s_data=json_send,i=i)

#tuturu
#qq
@app.route('/<page>/')
def show(page):
    print page
    if page=='palette':
        return render_template('palette.html', s_data='null')
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)


if __name__ == '__main__':
    app.run(debug=False)

