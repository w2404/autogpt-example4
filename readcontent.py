import sys
import json
for p in sys.argv[1:]:
    o=json.load(open(p))
    if 'error' in o:continue
    f_out=open(p[:-5]+'.txt','w')
    if 'messages' in o:
        for m in o['messages']:
            f_out.write(m['content'])
    else:
        f_out.write(o['choices'][0]['message']['content'])
    if 'http_proxy' in o:
        o.pop('http_proxy')
    if 'api_key' in o:
        o.pop('api_key')
    json.dump(o,open(p,'w'))
