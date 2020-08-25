filegroup (
    name = "logs",
    srcs = glob(["logs/*.csv",]),
    visibility = ["//visibility:public"],
)

py_binary (
    name = "ui_tests",
    srcs = ["ui_tests.py"],
    deps = [
        "//src/utils",
        "//src/frontend:app"
    ],
    data = [
        ":logs"
    ],
    visibility = ["//visibility:public"],
)
