alias(
    name = "app",
    actual = "//src/frontend:app",
)

alias(
    name = "ui_tests",
    actual = "//tests/frontend:ui_tests",
)

alias(
    name = "launch_config",
    actual = "//utils:generate_launch_config",
)

test_suite(
    name = "github_action_tests",
    tests = [
        "//tests/utils:log_utils_tests",
        "//tests/utils:search_utils_tests",
    ],
)
