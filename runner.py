from bottle import *
import bottle
import os

application = default_app()

@route("/")
def home():
	return template("index.html")

@route("/list")
def list():
	return template("AniList.html")

@route("/Boruto")
def boruto():
	return template("Boruto.html")

@route("/Boku")
def boku():
	return template("Boku.html")

@route("/OPM")
def opm():
	return template("OPM.html")

@route("/OnePiece")
def onepiece():
	return template("OnePiece.html")

@route("/DbSuper")
def dbsuper():
	return template("DbSuper.html")

@route("/Akame")
def akame():
	return template("Akame.html")

@route("/Noragami")
def noragami():
	return template("Noragami.html")

@route("/anotherPage")
def anoPage():
	return template("anotherPage.html")

#specifying the path for the file
@route('/<filepath:path>')
@route('/list/<filepath:path>')
@route('/Boruto/<filepath:path>')
@route('/Boku/<filepath:path>')
@route('/OPM/<filepath:path>')
@route('/OnePiece/<filepath:path>')
@route('/DbSuper/<filepath:path>')
@route('/Akame/<filepath:path>')
@route('/Noragami/<filepath:path>')
@route('/anotherPage/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__=='__main__':
	application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9595)))