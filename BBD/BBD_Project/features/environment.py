from utils.logger import LogGen
from utils.config_reader import ConfigReader
from utils.screenshot_util import ScreenshotUtil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions

logger = LogGen.loggen()


def before_scenario(context, scenario):
    logger.info("========================================")
    logger.info(f"STARTING SCENARIO : {scenario.name}")

    browser = ConfigReader.get_browser()
    base_url = ConfigReader.get_base_url()
    implicit_wait = ConfigReader.get_implicit_wait()
    headless = ConfigReader.get_headless()

    if browser.lower() == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        if headless:
            chrome_options.add_argument("--headless")

        context.driver = webdriver.Chrome(options=chrome_options)

    elif browser.lower() == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-extensions")

        if headless:
            edge_options.add_argument("--headless")

        context.driver = webdriver.Edge(options=edge_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(implicit_wait)
    context.driver.get(base_url)

    logger.info("Browser launched successfully")


def after_scenario(context, scenario):
    logger.info(f"Scenario Status : {scenario.status}")

    if scenario.status == "failed":
        logger.error(f"FAILED: {scenario.name}")

        ScreenshotUtil.capture_screenshot(
            context.driver,
            scenario.name
        )
    else:
        logger.info(f"PASSED: {scenario.name}")

    context.driver.quit()