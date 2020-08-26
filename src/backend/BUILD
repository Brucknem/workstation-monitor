py_library(
    name = "queries",
    srcs = [
        "__init__.py",
        "hardware_query.py",
        "cpu_query.py",
        "gpu_query.py",
        "ram_query.py",
        "sensors_query.py",
        "mock_query.py",
        ],
    imports = ["../../venv"],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "monitor",
    srcs = ["monitor.py"],
    deps = [":queries"],
    imports = ["../../venv"],
    visibility = ["//visibility:public"],
)