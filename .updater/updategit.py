#!/usr/bin/python3

import fileinput
import re
from os import close, remove, path
from shutil import move
from subprocess import call
from tempfile import mkstemp

assert path.isdir('.git'), "No git dir found"

def replace(file_path, pattern, subst):
    # From http://stackoverflow.com/a/39110
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(re.sub(pattern, subst, line))
    close(fh)
    remove(file_path)
    move(abs_path, file_path)

call(['git', 'fetch'])

for line in fileinput.input():
    branch, version, changelog, url = line.strip().split(' ')
    branch = 'master' if branch == 'latest' else branch
    call(['git', 'branch', branch, 'master']) # Will fail if the branch exists
    call(['git', 'checkout', branch])
    call(['git', 'rebase', 'origin/%s' % branch]) # May fail as well
    replace('Dockerfile', r'^ARG url=.*', 'ARG url=%s' % url)
    call(['git', 'commit', '-am', 'Auto update to version %s.\n\nChangelog: %s' % (version, changelog)])
    call(['git', 'push', 'origin', branch])

call(['git', 'checkout', 'master'])
