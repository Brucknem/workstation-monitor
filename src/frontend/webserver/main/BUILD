py_library (
    name = "main",
    srcs = glob([ "*.py" ]),
    visibility = ["//visibility:public"],
    data = [
        "//src/frontend/webserver/main/templates/main:templates"
    ],
    deps = [
        "//src/frontend/webserver/main/migrations:main_migrations"
    ]
)