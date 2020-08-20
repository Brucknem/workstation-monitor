import argparse

def generate(script_path=None):
    """
    Generates a copy & paste configuration for the VS Code launch.json
    """
    if not script_path:
        script_path = ""

    path = str(script_path)
    path_without_py = path if not path.endswith('.py') else path[0:-3]

    if not path_without_py:
        path_without_py = '<ADD-PYTHON-EXECUTABLE-PATH-WITHOUT-.PY>'

    config = f"""
    {{
        "name": "Python: {path_without_py}",
        "type": "python",
        "request": "launch",
        "program": "${{workspaceFolder}}/{path_without_py}.py\","""
    config += """
        "console": "integratedTerminal",
        "env": {
            "PYTHONPATH": \"""" \
            f"${{workspaceFolder}}/bazel-bin/{path_without_py}.runfiles/:" \
            f"${{workspaceFolder}}/bazel-bin/{path_without_py}.runfiles/python/:"
    config += """"
        }
    },"""
    return config


# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--script_path", help="Script path")
args = parser.parse_args()

script_path = None
if args.script_path:
    script_path = args.script_path

print(generate(script_path=script_path))
