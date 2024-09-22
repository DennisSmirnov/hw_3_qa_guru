from selene import be, have, browser


def browser_search(data):
    browser.element('[name="q"]').should(be.blank).type(data).press_enter()


def test_successful_search(browser_controller):
    browser_search('yashaka/selene')
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_unsuccessful_search(browser_controller):
    browser_search('OWOINIOQNF(#*(%*#%(@#%')
    browser.element('.card-section').should(be.present).should(
        have.text('Your search - OWOINIOQNF(#*(%*#%(@#% - did not match any documents.'))
