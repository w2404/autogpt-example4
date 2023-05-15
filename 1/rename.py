import glob
import os
import re
l=[(int(re.findall('\d+',n)[0]),n) for n in glob.glob('*.json')]
l=sorted(l)
for i in range(len(l)):
    _,n1=l[i] #f'{l[i]}.json'
    n2=f'{i+1}.json'
    if n1==n2:continue
    print(n1,n2)
    os.rename(n1,n2)


