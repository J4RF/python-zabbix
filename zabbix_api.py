import json
import requests

def getToken(server, username, password):

    headers={}
    headers['Content-Type']="application/json"

    data={}
    data['jsonrpc']="2.0"
    data['id']=1
    data['method']="user.login"
    data['params']={}
    data['params']['user']=username
    data['params']['password']=password

    response=requests.post("http://{}/zabbix/api_jsonrpc.php".format(server), headers=headers, data=json.dumps(data))

    return response.json()['result']


def getHostID(server, token, hostname):

    headers={}
    headers['Content-Type']="application/json"

    data={}
    data['jsonrpc']="2.0"
    data['id']=2
    data['auth']=token
    data['method']="host.get"
    data['params']={}
    data['params']['filter']={}
    data['params']['filter']['host']=hostname
    data['params']['output']="hostid"

    response=requests.post("http://{}/zabbix/api_jsonrpc.php".format(server), headers=headers, data=json.dumps(data))

    return response.json()['result'][0]['hostid']


def getItemID(server, token, host, item_key):

    headers={}
    headers['Content-Type']="application/json"

    data={}
    data['jsonrpc']="2.0"
    data['id']=2
    data['auth']=token
    data['method']="item.get"
    data['params']={}
    data['params']['hostids']=getHostID(server, token, host)
    data['params']['search']={}
    data['params']['search']['key_']=item_key
    data['params']['output']="itemid"

    response=requests.post("http://{}/zabbix/api_jsonrpc.php".format(server), headers=headers, data=json.dumps(data))

    return response.json()['result'][0]['itemid']


def getItemLastValue(server, token, host, item_key):

    headers={}
    headers['Content-Type']="application/json"

    data={}
    data['jsonrpc']="2.0"
    data['id']=2
    data['auth']=token
    data['method']="item.get"
    data['params']={}
    data['params']['filter']={}
    data['params']['filter']['host']=host
    data['params']['search']={}
    data['params']['search']['key_']=item_key

    response=requests.post("http://{}/zabbix/api_jsonrpc.php".format(server), headers=headers, data=json.dumps(data)).json()

    return response['result'][0]['lastvalue']


def getItemValues(server, token, host, item_key, time_from, time_till):

    headers={}
    headers['Content-Type']="application/json"

    data={}
    data['jsonrpc']="2.0"
    data['id']=2
    data['auth']=token
    data['method']="history.get"
    data['params']={}
    data['params']['output']="extend"
    data['params']['sortfield']="clock"
    data['params']['sortorder']="DESC"
    data['params']['itemids']=getItemID(server, token, host, item_key)
    data['params']['time_from']=time_from
    data['params']['time_till']=time_till

    response=requests.post("http://{}/zabbix/api_jsonrpc.php".format(server), headers=headers, data=json.dumps(data)).json()

    return response['result']
