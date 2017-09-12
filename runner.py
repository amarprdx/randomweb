from bottle import *
import bottle
import os

application = default_app()

@route("/")
def home():
	return template("index.html")

@route("/watch")
def watch():
	return template("watch.html")

@route("/anotherPage")
def anoPage():
	return template("anotherPage.html")

#specifying the path for the file
@route('/<filepath:path>')
@route('/watch/<filepath:path>')
@route('/anotherPage/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__=='__main__':
	application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9000)))