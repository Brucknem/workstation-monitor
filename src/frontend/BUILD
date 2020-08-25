filegroup(
    name = "notebooks_folder",
    srcs = glob(["*.ipynb"],
    exclude=["run.py", "run", "__init__.py"]),
    visibility = ["//visibility:public"],
)

py_binary(
    name = "run",
    srcs = ["run.py"],
    data = [":notebooks_folder"],
    deps = [
        "//src/utils:load_logs",
    ],
    imports = ["venv"],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "app",
    srcs = ["app.py"],
    imports = ["../../venv"],
    data = [
        "//src/frontend/templates:templates",
        "//src/frontend/static:static",
    ],
    deps = [
        "//src/utils:load_logs"
    ],
    visibility = ["//visibility:public"],
)