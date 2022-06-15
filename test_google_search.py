from selene.support.shared import browser
from selene import be, have


def test_positive():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_negative():
    browser.element('[id="search"]').should(have.text('Selene is User-oriented Web UI browser tests in Python'))
