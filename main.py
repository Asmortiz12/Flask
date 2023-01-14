from flask import Flask


app = Flask(__name__)

@app.route('/1')

def Hello1():
    
    return 'Programa 1 con flask'

@app.route('/2')

def Hello2():
    
    return 'Inicio2'



if __name__ == '__main__':
    app.run(debug=True, port=5000)