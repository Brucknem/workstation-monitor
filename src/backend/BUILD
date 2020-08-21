py_library(
    name = "hardware_query",
    srcs = ["hardware_query.py"],
    deps = [
    ],
    imports = ["../../venv"],
    visibility = ["//visibility:public"],
)

py_test(
    name = "gpu_query",
    srcs = ["gpu_query.py"],
    deps = [
        ":hardware_query"
    ],
    imports = ["../../venv"],
    visibility = ["//visibility:public"],
)

py_test(
    name = "cpu_query",
    srcs = ["cpu_query.py"],
    deps = [
        ":hardware_query"
    ],
    imports = ["../../venv"],
    visibility = ["//visibility:public"],
)