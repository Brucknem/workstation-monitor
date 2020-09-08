import json
import os
from pathlib import Path

from flask import Flask, render_template, request, session, jsonify

from src.utils.log_utils import list_logs, read_from_hdf5
from src.utils.search_utils import search_dirs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeet'
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

svgs = {}
svg_paths = Path('src/frontend/static/img/')
svg_files = [
    str(svg_path) for svg_path in svg_paths.iterdir()
    if svg_path.is_file() and str(svg_path).endswith('.svg')]
for svg_file in svg_files:
    with open(svg_file) as svg:
        svgs[Path(svg.name).stem] = svg.read()


def render_nav_item_log_files(log_paths):
    """Renders the nav bar items displaying the log paths
    """
    return render_template('nav_item_log_file.html', log_paths=log_paths, icon=svgs['file'])


def generate_search_result(search_string):
    """Generates the search result for the given search string
    """
    session['search_string'] = search_string.strip()
    log_paths = list_logs(session['search_string'])
    found_logs = bool(log_paths)
    items = render_nav_item_log_files(log_paths)

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
    default_item = render_nav_item_log_files(list_logs(search_string))
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

    df = read_from_hdf5(full_path, 'df')
    indices = list(read_from_hdf5(full_path, 'id'))
    values = list(read_from_hdf5(full_path, 'val'))
    indices.remove('timestamp')

    uniques = df[indices].drop_duplicates()
    identifiers = []
    for row in uniques.itertuples():
        identifier = [str(item) for item in row]
        identifier.pop(0)
        identifiers.append(", ".join(identifier))

    result = {
        'indices-select': render_template('dataframe_columns_select.html', type='indices', values=list(identifiers),
                                          icon=svgs['command']),
        'values-select': render_template('dataframe_columns_select.html', type='values', values=values,
                                         icon=svgs['crosshair'])}

    return jsonify(result)


@app.route('/show_log')
def show_log():
    selected_columns = json.loads(request.args.get('selected_columns'))
    print(selected_columns)
    return 'Lol'


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
    app.run(debug=True, use_reloader=True, use_debugger=True, threaded=True)