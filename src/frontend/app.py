from src.frontend.load_logs import load_log, list_logs
from flask import Flask, render_template, request, url_for, flash, redirect, session
from markupsafe import escape
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeet'


@app.route('/logs', methods=('GET', ))
def logs():
    log_path = request.args.get('log_path')
    log_files = list_logs(log_path)

    if not log_files:
        flash('Log path is invalid!')
        return redirect(url_for('index'))
            
    return render_template(
        'logs.html', log_path=log_path, log_files=log_files)

@app.route('/log', methods=('GET', ))
def log():
    log_file = request.args.get('log_file')
    log = load_log(log_file)

    if log is None:
        flash('Log is invalid!')
        return redirect(url_for('index'))        

    return render_template(
        'log.html', log_file=log_file)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if 'log_path' in request.form:
            log_path = request.form['log_path']
            if log_path:
                session['log_path'] = log_path
                return redirect(url_for('logs', log_path=escape(log_path)))
            else:
                flash('Log path is required!')
    if 'log_path' in session:
        return render_template('index.html', log_path=session['log_path'])
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, use_debugger=True, threaded=False)
