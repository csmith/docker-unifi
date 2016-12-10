#!/usr/bin/python3

import json
import requests
from distutils.version import StrictVersion

headers = {'Accept': 'application/json', 'X-Requested-With': 'XMLHttpRequest'}
host = 'https://www.ubnt.com'
address = host + '/download/?platform=unifi'
r = requests.get(address, headers=headers)

versions = []
dls = [d for d in r.json()['downloads'] if d['filename'] == 'unifi_sysvinit_all.deb']
for d in dls:
    version = StrictVersion(d['version'][1:] if d['version'][0] == 'v' else d['version'])
    changelog = d['changelog']
    uri = host + d['file_path']
    versions.append((version, changelog, uri))

versions = sorted(versions, key=lambda x: x[0], reverse=True)
labels = dict([('latest', versions[0])] + [(str(v[0]), v) for v in versions])
for i in range(20):
    try:
        labels[str(i)] = next(v for v in versions if str(v[0])[0:2] == str(i) + '.')
    except StopIteration:
        pass

for k, label in labels.items():
    print("%s %s" % (k, ' '.join(map(str, label))))
