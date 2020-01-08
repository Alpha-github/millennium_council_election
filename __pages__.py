from flask import Flask, render_template, request, url_for, redirect
from flask import flash

baseApp = Flask(__name__, static_folder = 'static', template_folder='templates')

@baseApp.route('/')
def page():
    return render_template('__login_page.html')

if __name__ == '__main__':
    baseApp.run(host='0.0.0.0' , port=5000, debug=True)
