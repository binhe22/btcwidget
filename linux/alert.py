import requests
import json
import time
import redis
import pyttsx
aliquot100 = 0
engine = pyttsx.init()

def run_forever():
    global aliquot100
    r = requests.get("https://data.btcchina.com/data/ticker")
    re = redis.StrictRedis(host='localhost', port=6379, db=0)
    text = r.text
    j = json.loads(text)
    nowvalue = float((j["ticker"]["last"]).encode("ascii"))
    nowtime = int(time.time())
    re.set(nowtime, nowvalue)
    nowaliquot100 = int(nowvalue/100)
    print nowvalue
    if  nowaliquot100 != aliquot100:
        if nowaliquot100 > aliquot100:
            engine.say("rise in price")
            aliquot100 =  nowaliquot100
        if nowaliquot100 < aliquot100:
            engine.say("down in price")
            aliquot100 =  nowaliquot100
        engine.runAndWait()

if __name__ == '__main__':
    while 1:
        run_forever()
        time.sleep(5)
