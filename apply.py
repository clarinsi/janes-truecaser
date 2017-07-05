#!/usr/bin/python
import sys
import argparse
import gzip
parser = argparse.ArgumentParser(description='Applier of the truecasing model')
parser.add_argument('-U', '--upper', help='non-lowercase first token in sentence', action='store_true')
parser.add_argument('model', help='truecasing model')
args=parser.parse_args()
model={}
for line in gzip.open(args.model):
  line=line.decode('utf8').strip().split('\t')
  model[line[0]]=line[1].split(' ')[0]
start=True
for line in sys.stdin:
  if line.strip()=='':
    start=True
    sys.stdout.write(line)
    continue
  tokens=[]
  for token in line.decode('utf8').strip().lower().split(' '):
    if start:
      if args.upper:
        if model.get(token,token)==token:
          tokens.append(token.title())
        else:
          tokens.append(model.get(token))
        start=False
        continue
    tokens.append(model.get(token,token))
    start=False
  sys.stdout.write(' '.join(tokens).encode('utf8')+'\n')
