#!/usr/bin/python
import sys
memory={}
sent=[]
for line in sys.stdin:
  if line.strip()=='':
    for token in sent[1:]:
      key=token.lower()
      if key not in memory:
        memory[key]={}
      memory[key][token]=memory[key].get(token,0)+1
    sent=[]
  else:
    sent.extend(line.decode('utf8').strip().split(' '))
for key in sorted(memory,key=lambda x:-sum(memory[x].values())):
  sys.stdout.write(key.encode('utf8'))
  for variant,freq in sorted(memory[key].items(),key=lambda x:-x[1]):
    sys.stdout.write('\t'+variant.encode('utf8')+' '+str(freq))
  sys.stdout.write('\n')
