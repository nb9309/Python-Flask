from flask import *
app = Flask(__name__)

@app.route('/login, method=[get]')
def login():
    uname = request.args.get('uname')
    password = request.args.get('password')
    if uname == 'naresh' and password == 'nareshit':
        return 'welcome %s' %uname
    else:
        return 'invalid credentials'
    
if __name__ == '__main__':
    app.run(debug=True)