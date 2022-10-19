import pytest
from selenium import webdriver

# для запуска тестов добавлены 2 необязательных параметра (browser и language (по умолчанию chrome и en))
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en/ru/es etc")

@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")

    browser = None
    
    # выполняется подготовка и запуск используемого тестом браузера, указанного в параметре browser
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        
        options = webdriver.chrome.options.Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        
        browser = webdriver.Chrome(options=options)
    
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # добавлено явное указание стандартного пути к исполняемому файлу Firefox в ОС Windows
        # если используется другая ОС или файл находится в другом месте, необходимо поправить эту опцию
        options = webdriver.firefox.options.Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp, options=options)
    
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()