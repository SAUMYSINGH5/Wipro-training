

def enter_username(self, username):
    logger.info(
        f"Entering Username : {username}"
    )
    element = WaitUtils.wait_for_element_visible(
        self.driver,
        SignupLocators.USERNAME
    )
    element.clear()
    element.send_keys(username)


def enter_password(self, password):
    logger.info("Entering Password")
    element = WaitUtils.wait_for_element_visible(
        self.driver,
        SignupLocators.PASSWORD
    )
    element.clear()
    element.send_keys(password)


def click_signup_button(self):
    logger.info("Clicking Sign up Button")
    WaitUtils.wait_for_element_clickable(
        self.driver,
        SignupLocators.SIGNUP_BUTTON
    ).click()