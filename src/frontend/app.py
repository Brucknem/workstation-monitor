from src.utils.log_utils import list_logs, load_log
from src.utils.search_utils import search_dirs
from src.utils.dataframe_to_bokeh_utils import convert_dataframe_to_column_data_source
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
            items += render_template('nav_item_log_file.html',log_path=log_path, id=i)
    else:
        items = render_template('nav_item_log_file.html', id=0)
    return bool(log_paths), items


def generate_search_result(search_string):
    """Generates the search result for the given search string
    """
    session['search_string'] = search_string.strip()
    log_paths = list_logs(session['search_string'])
    found_logs, items = render_nav_item_log_files(log_paths)

    directories = []
    if not found_logs:
        directories = search_dirs(session['search_string'])

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
    return generate_search_result(search_string)


@app.route('/load_log')
def request_log():
    selected_log = str(request.args.get('selected_log')).strip()
    full_path = os.path.join(session["search_string"], selected_log)

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
    app.run(debug=True, use_reloader=False, use_debugger=True, threaded=False)
