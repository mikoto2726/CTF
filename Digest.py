import requests

url = "http://ctfq.u1tramarine.blue/q9/flag.html"
resu = requests.get(url).headers
print(resu["WWW-Authenticate"])

import requests
from hashlib import md5

url = "http://ctfq.u1tramarine.blue/q9/flag.html"
h1 = "c627e19450db746b739f41b64097d449"
h2 = md5(b"GET:/q9/flag.html").hexdigest()
nonce = "6pBUM430BQA=3426b41598ed0e295b0a2c02b20016b2c9fc9885"
conce = "abcd"
qop = "auth"
nc = "00000005"
digest = md5(f"{h1}:{nonce}:{nc}:{conce}:{qop}:{h2}".encode()).hexdigest()
auth = f'Digest username="q9", realm="secret", nonce="{nonce}", uri="/q9/flag.html", algorithm=MD5, response="{digest}", qop={qop}, nc={nc}, cnonce="{conce}"'

res = requests.get(url, headers={"Authorization":auth})
print(res.text)