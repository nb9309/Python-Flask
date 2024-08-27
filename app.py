from flask import *
app = Flask(__name__)

@app.route('/admin')
def admin():
    return 'hii how are u'

@app.route('/student')
def student():
    return 'I am student'

@app.route('/staff')
def staff():
    return 'They are staf'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'student':
        return redirect(url_for('student'))
    if name == 'staff':
        return redirect(url_for('staff'))
    

if __name__ == '__main__':
    app.run()