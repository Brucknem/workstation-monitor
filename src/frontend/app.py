from src.frontend.load_logs import load_log, list_logs, extract_names, list_dirs
from flask import Flask, render_template, request, url_for, flash, redirect, session, jsonify
from markupsafe import escape
import os
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeet'
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

def render_nav_item_log_files(log_paths):
    """Renders the nav bar items displaying the log paths
    """
    items = ""
    if log_paths:
        for i, log_path in enumerate(log_paths):
            items += render_template('nav_item_log_file.html',
                                     is_active=i == 0, log_path=log_path, id=i)
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


def get_items_and_search_string():
    """Generates the default item from the session.
    """
    search_string = ""
    if 'search_string' in session:
        search_string = session['search_string']
    _, default_item = render_nav_item_log_files(list_logs(search_string))
    return {
        'default_item': default_item,
        'search_string': search_string
    }


@app.route('/search')
def search():
    search_string = request.args.get('search_string')
    if search_string:
        return generate_search_result(search_string)


@app.route('/load_log')
def request_log():
    selected_log = str(request.args.get('selected_log')).strip()
    full_path = os.path.join(session["search_string"], selected_log)
    log = load_log(full_path)

    keys = list(log.keys())
    print('*\n'*3)
    print(keys)

    source = ColumnDataSource(log)

    output_file("line.html")
    p = figure()
    p.line(x='timestamp', y=keys[0], source=source)
    show(p)

    return 'Log'


@app.route('/')
def index():
    return render_template('index.html', **get_items_and_search_string())


@app.route('/about')
def about():
    return render_template('about.html', **get_items_and_search_string())


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
