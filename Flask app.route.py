from flask import Flask
app = Flask(__name__)

@app.route('/hiii/<int:sub>')
def fun(sub):
    return 'hii how are you %d' %sub

if __name__ == '__main__':
    app.run(debug=True)
