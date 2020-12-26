import json
import ssl
import urllib
import urllib.request

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

sum=0
while True:
    url=input('Enter url:')
    if len(url)<1: break

    connection=urllib.request.urlopen(url,context=ctx)
    data=connection.read()
    print(data)

    info=json.loads(data)

    for item in info['comments']:
        number=(item['count'])
        sum+=int(number)
    print(sum)
    break