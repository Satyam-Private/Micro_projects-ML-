from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['GET' , 'POST'])
def result():
    if request.method == 'POST': 
        name = request.form['name']
        mail = request.form['mail']
        text = request.form['text']
    my_info = {
        'name' : name, 
        'mail' : mail,
        'text' : text
    }
    
    return render_template('result.html' , params = my_info)


if __name__ == '__main__':
    app.run(debug=True)