from flask import Flask,jsonify, render_template

from loansapp import loansapp
from app3 import app3
main_app = Flask(__name__);
main_app.config['Debug']= True


main_app.register_blueprint(app3);
main_app.register_blueprint(loansapp)

@main_app.route('/')
def home():
    
    return render_template('index.html')


@main_app.route('/index')
def index():
    
    return render_template('index.html')


if __name__ == '__main__':
    print('Main')
    main_app.run(debug=True,host="0.0.0.0",port=9000)
