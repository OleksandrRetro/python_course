def pytest_report_header() -> str:
    return "This message prints before all tests executed."


def pytest_html_report_title(report):
    report.title = "Test report title from HOOK."
