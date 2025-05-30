# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import BasePage


class FirefoxMobileFocusPage(BasePage):
    _URL_TEMPLATE = "/{locale}/browsers/mobile/focus/"

    _get_firefox_header_button_locator = (By.ID, "get-firefox")
    _get_firefox_qr_code_locator = (By.ID, "focus-qr")

    @property
    def is_firefox_qr_code_displayed(self):
        return self.is_element_displayed(*self._get_firefox_qr_code_locator)
