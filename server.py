from bottle import route, run, static_file, url, request, get, redirect, default_app
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), './flames'))
from flame import flames

@get("/")
def home():
    redirect('ui/index.html')

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='.')

@get('/flames')
def getresult():
    male=request.query['male']
    female=request.query['female']
    return flames(male, female)


run(host='0.0.0.0', port=1808, reloader=True, debug=True )

# application = default_app()

