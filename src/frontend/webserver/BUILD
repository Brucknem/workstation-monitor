filegroup (
    name = "database",
    srcs = [ "db.sqlite3" ]
)

py_binary (
    name = "webserver",
    srcs = [ "manage.py" ],
    main = "manage.py",
    data = [
        "database"
    ],
    deps = [
        "//src/frontend/webserver/webserver:webserver_internal",
        "//src/frontend/webserver/main:main"
    ],
)