filegroup (
    name = "logs",
    srcs = glob(["logs/*.csv",]),
    visibility = ["//visibility:public"],
)

py_test (
    name = "load_logs_test",
    srcs = ["load_logs_test.py"],
    deps = [
        "//src/utils:load_logs",
    ],
    data = [
        ":logs"
    ]
)
