#!/usr/bin/python3
from bottle import post, run
import subprocess

@post("/post")
def kek():
	subprocess.run(['git', '--git-dir=/root/back-spring/.git', '--work-tree=/root/back-spring', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

run(host='0.0.0.0', port=3000)
