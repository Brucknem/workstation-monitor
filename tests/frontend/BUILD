filegroup (
    name = "logs",
    srcs = glob(["logs/*.csv",]),
    visibility = ["//visibility:public"],
)


py_library (
    name = "ui_tests_base",
    srcs = ["ui_tests_base.py"],
    deps = [
        "//src/utils",
        "//src/frontend:app"
    ],
    data = [
        ":logs"
    ],
    visibility = ["//visibility:public"],
)

py_binary (
    name = "basic_ui_tests",
    srcs = ["basic_ui_tests.py"],
    deps = [
        ":ui_tests_base",
    ],
    data = [
        ":logs"
    ],
    visibility = ["//visibility:public"],
)

py_binary (
    name = "search_ui_tests",
    srcs = ["search_ui_tests.py"],
    deps = [
        ":ui_tests_base",
        "//src/backend:queries"
    ],
    data = [
        ":logs"
    ],
    visibility = ["//visibility:public"],
)

py_binary (
    name = "ui_tests",
    srcs = ["ui_tests.py"],
    deps = [
        ":basic_ui_tests",
        ":search_ui_tests",
    ],
    data = [
        ":logs"
    ],
    visibility = ["//visibility:public"],
)
