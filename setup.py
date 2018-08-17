#!/usr/bin/env python
import os
import sys
import subprocess

def setup():
  _BASE = os.path.abspath(os.path.dirname(__file__))
  _FRONTEND = os.path.join(_BASE, 'frontend')
  _BACKEND = os.path.join(_BASE, 'backend')

  commands = [
    {'sh':'pipenv install', 'cwd':'.'},
    {'sh':'npm install', 'cwd':_FRONTEND},
    {'sh':'npm run build', 'cwd':_FRONTEND},
    {'sh':'python manage.py collectstatic --no-input', 'cwd':_BACKEND},
    {'sh':'python manage.py runserver', 'cwd':_BACKEND},
  ]

  for c in commands:
    p = subprocess.Popen(c['sh'].split(' '), cwd=c['cwd'], shell=True)
    p.wait()

if __name__ == '__main__':
  setup()
