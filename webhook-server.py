#!/usr/bin/python3
from bottle import post, run, get, static_file
import subprocess
from ansi2html import Ansi2HTMLConverter

logs_root='/root/back-spring/logs/'
conv = Ansi2HTMLConverter()

@post("/post")
def kek():
	subprocess.run(['git', '--git-dir=/root/back-spring/.git', '--work-tree=/root/back-spring', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.run(['javaStop'])
	subprocess.run(['javaBuild2'])
	subprocess.run(['javaStart'])

@get("/")
def index():
	return "asd"

@get("/logs/java")
def javaLog():
	f = open(logs_root+'java.log')
	s = f.read()
	f.close()
#	return s.replace('\n', '<br />')
	return conv.convert(s)

@get("/logs/build")
def javaLog():
	f = open(logs_root+'build.log')
	s = f.read()
	f.close()
	return s.replace('\n', '<br />')

@get("/logs/android")
def andrLog():
	f = open("/root/back-spring/logs/android.log")
	s = f.read()
	f.close()
	return s.replace('\n', '<br />')

run(host='0.0.0.0', port=3000)
