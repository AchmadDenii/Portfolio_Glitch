from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

#Get Request ke index.html
@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

#Get Request ke about.html
@app.route('/about', methods=['GET'])
def about():
   return render_template('about.html')

#GET info ke my_name
@app.route('/info', methods=['GET'])
def get_info():
    my_name = request.args.get('my_name')
    print(my_name)
    return jsonify({ 
        'msg': 'GET info!!'
    })

#POST info ke my_name
@app.route('/info', methods=['POST'])
def post_info():
    my_name = request.form['my_name']
    print(my_name)
    return jsonify({ 
        'msg': 'POST info!!'
    })

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)