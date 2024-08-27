from flask import Flask
app = Flask(__name__)

def fun():
    return 'add_url_rule'
app.add_url_rule('/fun','fun', fun)

if __name__=='__main__':
    app.run(debug=True)
