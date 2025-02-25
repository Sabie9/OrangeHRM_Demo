import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver= webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    return driver

def pytest_addoption(parser):       #this will get the value from CLI/ hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):               #this will return the browser value to the setup method
    return request.config.getoption("--browser")


###########Pytest - HTML Report #########

#this is a hook to add environment informations in the HTML Report before the test run starts
def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "Orange-HRM-Demo"
    config.stash[metadata_key]["Module"] = "HRM"
    config.stash[metadata_key]["Environment"] = "QA"
    config.stash[metadata_key]["Tester"] = "Saayan"



#this is a hook to modify/delete environment informations from the HTML Report before the test run starts
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Python", None)

#this is a hook to update the html report title with a custom name
def pytest_html_report_title(report):
    report.title="OrangeHRM-Demo-Test-Execution"

#this is a hook to modify environment section of the HTML report after test run is over
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["Platform"] = "Windows 11"

#this is a hook to modify the summary section of the HTML report after the test run is over
def pytest_html_results_summary(prefix,summary,postfix):
    prefix.extend(["<h1> This is the updated Prefix </h1>"])
    summary.extend(["<h1> This is the updated Summary </h1>"])
    postfix.extend(["<h1> This is the updated Postfix </h1>"])