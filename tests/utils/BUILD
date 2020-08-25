filegroup (
    name = "logs",
    srcs = glob(["logs/*.h5",]),
    visibility = ["//visibility:public"],
)

py_test (
    name = "load_logs_test",
    srcs = ["load_logs_test.py"],
    deps = [
        "//src/backend:queries",
        "//src/utils:load_logs",
    ],
    imports = [
        "tests/utils/logs",
    ],
    data = [
        ":logs"
    ]
)
