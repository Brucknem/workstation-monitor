from src.frontend.load_logs import load_log
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeet'

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        log_path = request.form['log_path']

        if not log_path:
            flash('Log path is required!')
        else:
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, use_debugger=True, threaded=False)