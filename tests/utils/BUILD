filegroup (
    name = "logs",
    srcs = glob(["logs/*.h5",]),
    visibility = ["//visibility:public"],
)

py_test (
    name = "log_utils_tests",
    srcs = ["log_utils_tests.py"],
    deps = [
        "//src/backend:queries",
        "//src/utils",
    ],
    imports = [
        "tests/utils/logs",
    ],
    data = [
        ":logs"
    ]
)
