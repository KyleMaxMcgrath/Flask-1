from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def show_add():
  return str(add(int(request.args['a']),int(request.args['b'])))

@app.route('/sub')
def show_sub():
  return str(sub(int(request.args['a']),int(request.args['b'])))

@app.route('/mult')
def show_mult():
  return str(mult(int(request.args['a']),int(request.args['b'])))

@app.route('/div')
def show_div():
  return str(div(int(request.args['a']),int(request.args['b'])))

OPERATIONS = {
  'add': add,
  'sub': sub,
  'mult': mult,
  'div': div
}

@app.route('/math/<op>')
def show_math(op):
  return str(OPERATIONS[op](int(request.args['a']), int(request.args['b'])))
