filegroup (
    name = "logs",
    srcs = glob(["logs/*.csv",]),
    visibility = ["//visibility:public"],
)

py_test (
    name = "load_logs_test",
    srcs = ["load_logs_test.py"],
    deps = [
        "//src/frontend:load_logs",
    ],
    data = [
        ":logs"
    ]
)


py_binary (
    name = "ui_tests",
    srcs = ["ui_tests.py"],
    deps = [
        "//src/frontend:load_logs",
        "//src/frontend:app"
    ],
    data = [
        ":logs"
    ],
    visibility = ["//visibility:public"],
)
