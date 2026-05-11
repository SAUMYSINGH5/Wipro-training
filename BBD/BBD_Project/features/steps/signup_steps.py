from behave import given, when, then
from pages.signup_page import SignupPage
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil
import time

logger = LogGen.loggen()


@given('User launches Demoblaze application')
def step_impl(context):
    logger.info("Launching Demoblaze application")

    context.signup_page = SignupPage(context.driver)


@when('User clicks on Sign up menu')
def step_impl(context):
    logger.info("Clicking Sign up menu")

    context.signup_page.click_signup_menu()


@when('User enters signup username "{username}"')
def step_impl(context, username):
    # 🔥 FIX: unique username every run
    unique_username = username + str(int(time.time()))

    logger.info(f"Entering username: {unique_username}")

    context.signup_page.enter_username(unique_username)


@when('User enters signup password "{password}"')
def step_impl(context, password):
    logger.info(f"Entering password: {password}")

    context.signup_page.enter_password(password)


@when('User clicks Signup button')
def step_impl(context):
    logger.info("Clicking Signup button")

    context.signup_page.click_signup_button()


@then('User should see signup success message')
def step_impl(context):
    logger.info("Verifying signup success message")

    alert_text = context.signup_page.verify_signup_success()

    # Screenshot
    ScreenshotUtil.capture_screenshot(
        context.driver,
        "signup_success"
    )

    logger.info(f"Alert received: {alert_text}")

    # ✅ FIXED ASSERT
    assert "successful" in alert_text.lower(), \
        f"Unexpected alert message: {alert_text}"