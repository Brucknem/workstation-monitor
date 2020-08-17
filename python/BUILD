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
        "//python/src:load_logs",
    ],
    imports = ["venv"],
    visibility = ["//visibility:public"],
)