from flask import Flask, render_template
from flask_cors import CORS
from config import PATH_STATIC


app = Flask(__name__, static_url_path = '',  static_folder= PATH_STATIC, template_folder='static/package.nw')
app.config['SECRET_KEY'] = 'secret!'
app.config['JSON_AS_ASCII'] = False

CORS(app, supports_credentials=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print('package.nw静态服务器')
    app.run(host='0.0.0.0', port=5000)