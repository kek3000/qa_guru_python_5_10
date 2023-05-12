import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_github_selene(browser_start):
    browser.open('/')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('kek3000/qa_guru_python_5_10')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('kek3000/qa_guru_python_5_10')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text("#1")).should(be.visible)


def test_github_dynamic_steps(browser_start):
    with allure.step('Открываем главную страницу'):
        browser.open('/')

    with allure.step('Ищем нужный репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type('kek3000/qa_guru_python_5_10')
        browser.element('.header-search-input').submit()

    with allure.step('Заходим в нужный репозиторий'):
        browser.element(by.link_text('kek3000/qa_guru_python_5_10')).click()

    with allure.step('Переходим в issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие нужного issue'):
        browser.element(by.partial_text("#1")).should(be.visible)


def test_github_decorator_steps(browser_start):
    open_main_page()
    search_repository('kek3000/qa_guru_python_5_10')
    go_to_repository('kek3000/qa_guru_python_5_10')
    go_to_issues()
    search_issues('#1')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Ищем нужный репозиторий {repo}')
def search_repository(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repo)
    browser.element('.header-search-input').submit()


@allure.step('Заходим в нужный репозиторий {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Переходим в issues')
def go_to_issues():
    browser.element('#issues-tab').click()


@allure.step('Ищем нужный issues {number}')
def search_issues(number):
    browser.element(by.partial_text(number)).should(be.visible)


def test_github_dynamic_labels(browser_start):
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.feature('Задача в репозитории')
    allure.dynamic.story('Пользователь с правами админа производит поиск репозитория')
    allure.dynamic.link('https://github.com', name='Auto QA test')

    browser.open('/')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('kek3000/qa_guru_python_5_10')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('kek3000/qa_guru_python_5_10')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text("#1")).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('Owner', 'n.alekseev')
@allure.feature('Задача в репозитории')
@allure.story('Пользователь с правами юзера производит поиск репозитория')
@allure.link('https://github.com', name='Testing')
def test_github_decorator_labels(browser_start):
    browser.open('/')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('kek3000/qa_guru_python_5_10')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('kek3000/qa_guru_python_5_10')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text("#1")).should(be.visible)
