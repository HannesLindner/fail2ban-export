#!/usr/bin/env python3
import re, subprocess, argparse
from prometheus_client import CollectorRegistry, Counter, write_to_textfile
from config import *
## Commandline args
parser = argparse.ArgumentParser(description="Exports fail2ban-client metrics.")
parser.add_argument('-j', '--jail', help="Jail name to be exported", required=True)
parser.add_argument('-f', '--file', help="File to be saved. path + name")
args = parser.parse_args()
## Regex
keys = '|'.join(parseKeys.keys())
pattern = re.compile(r'('+ keys + ')\s*(\d*)')
if args.jail:
    registry = CollectorRegistry()
    process = subprocess.Popen(['fail2ban-client', 'status', args.jail], stdout=subprocess.PIPE)
    response = process.communicate()[0].decode('utf-8')
    match = re.findall(pattern, response)
    for m in match:
        print(m[1])
        counter = Counter(parseKeys[m[0]][0], parseKeys[m[0]][1], ['jail'] ,registry=registry)
        counter.labels(args.jail).inc(float(m[1]))

    write_to_textfile((args.file or (EXPORT_LOCATION + EXPORT_FILE_NAME)).replace('{{jail}}', args.jail), registry)