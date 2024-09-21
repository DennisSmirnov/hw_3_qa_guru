from selene import browser, have, be


def test_successful_search(browser_controller):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_unsuccessful_search(browser_controller):
    browser.element('[name="q"]').should(be.blank).type('OWOINIOQNF(#*(%*#%(@#%').press_enter()
    browser.element('.card-section').should(be.present)
