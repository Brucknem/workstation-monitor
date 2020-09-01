py_test (
    name = "hardware_query_tests",
    srcs = ["hardware_query_tests.py"],
    deps = [
        "//src/backend:queries",
    ],
)

py_library (
    name = "hardware_query_write_to_file_tests_base",
    srcs = ["hardware_query_write_to_file_tests_base.py"],
    deps = [
        "//src/backend:queries",
    ],
    imports = [
        "tests/backend/logs"
    ]
)

py_test (
    name = "hardware_query_write_to_h5_file_tests",
    srcs = ["hardware_query_write_to_h5_file_tests.py"],
    deps = [
        ":hardware_query_write_to_file_tests_base",
    ],
)


py_test (
    name = "hardware_query_write_to_json_file_tests",
    srcs = ["hardware_query_write_to_json_file_tests.py"],
    deps = [
        ":hardware_query_write_to_file_tests_base",
    ],
)
