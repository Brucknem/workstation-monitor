filegroup (
    name = "logs",
    srcs = glob(["logs/*.h5",]),
    visibility = ["//visibility:public"],
)

filegroup (
    name = "test_dir",
    srcs = glob(["test_dir/**",]),
    visibility = ["//visibility:public"],
)

py_test (
    name = "log_utils_tests",
    srcs = ["log_utils_tests.py"],
    deps = [
        "//src/backend:queries",
        "//src/backend:mock_query",
        "//src/utils",
    ],
    imports = [
        "tests/utils/logs",
    ],
    data = [
        ":logs"
    ]
)

py_test (
    name = "search_utils_tests",
    srcs = ["search_utils_tests.py"],
    deps = [
        "//src/backend:queries",
        "//src/utils",
    ],
    imports = [
        "tests/utils/test_dir",
    ],
    data = [
        ":test_dir"
    ]
)
