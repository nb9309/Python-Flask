from flask import *
ape = Flask(__name__)

@ape.route('/')
def fun():
    return render_template('base.html')

if __name__=='__main__':
    ape.run(debug=True)