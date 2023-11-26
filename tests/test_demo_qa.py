from selene import browser, by, be, os
import os.path
import pytest
import tests


def test_registration_demo_qa():
    browser.open('/')
    browser.element('#firstName').type('Ruslan')
    browser.element('#lastName').type('Matygullin')
    browser.element('#userEmail').type('ruslan@mail.ru')
    browser.element('.custom-control').click()
    browser.element('#userNumber').type(97700010101)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1992')).click()
    browser.element('.react-datepicker__month-select').click().element(by.text('February')).click()
    browser.element('.react-datepicker__day--021').click()
    browser.element('#subjectsInput').type('Biology').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__), 'resources/rus.png')))
    ...
