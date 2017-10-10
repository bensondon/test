# -*- coding:UTF-8 -*-
import os
import json
aa=[d for d in os.listdir('.')]
result = json.dumps(aa, encoding='UTF-8', ensure_ascii=False)
print 'b=', result

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k,"=",v
print  [k + "=" + v for k,v in d.iteritems() ]

L = ['Hello', 'World', '18', 'Apple', None]
print [s.lower() if isinstance(s, str) else s for s in L ]