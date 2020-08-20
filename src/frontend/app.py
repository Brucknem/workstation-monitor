from src.frontend.load_logs import load_log, list_logs, extract_names, list_dirs
from flask import Flask, render_template, request, url_for, flash, redirect, session, jsonify
from markupsafe import escape
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeet'

def render_nav_item_log_files(log_paths):
    """Renders the nav bar items displaying the log paths
    """
    items = ""
    if log_paths:
        for i, log_path in enumerate(log_paths):
            items += render_template('nav_item_log_file.html', is_active=i==0, log_path=log_path, id=i)
    else:
        items = render_template('nav_item_log_file.html', id=0)
    return bool(log_paths), items

def generate_search_result(search_string):
    """Generates the search result for the given search string
    """
    session['search_string'] = search_string
    log_paths = list_logs(search_string)
    found_logs, items = render_nav_item_log_files(log_paths)

    directories = []
    if not found_logs:
        directories = list_dirs(search_string)

    result = {
        'found_logs': found_logs,
        'items': items,
        'directories': directories
    }
    return jsonify(result)

def get_default_item_and_search_string():
    """Generates the default item from the session.
    """
    search_string = session['search_string']
    _, default_item = render_nav_item_log_files(list_logs(search_string))
    return {
        'default_item': default_item,
        'search_string': search_string
    }

@app.route('/', methods=('GET', 'POST'))
def index():
    search_string = request.args.get('search_string')
    if search_string:
        return generate_search_result(search_string)
    
    return render_template('index.html', **get_default_item_and_search_string())

@app.route('/about')
def about():
    return render_template('about.html', **get_default_item_and_search_string())


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, use_debugger=True, threaded=False)
