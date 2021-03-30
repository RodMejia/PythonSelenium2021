from pathlib import Path
from selenium import webdriver

def get_project_root() -> Path:
    return Path(__file__).parent.parent

def get_chrome_path() -> Path:
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver')

driver = webdriver.Chrome(executable_path=get_chrome_path())
driver.get('https://www.google.com')
print(f'Current title: {driver.title}')
print(f'Current URL: {driver.current_url}')
driver.get('https:www.mlb.com/es')
print(f'Current title: {driver.title}')
print(f'Current URL: {driver.current_url}')
print(f'Current source: {driver.page_source}')
driver.get('https:www.nytimes.com/es')
driver.refresh()
print(f'Current title: {driver.title}')
print(f'Current URL: {driver.current_url}')
driver.back()
driver.back()
print(f'Current title: {driver.title}')
print(f'Current URL: {driver.current_url}')
print(f'Cookies: {driver.get_cookies()}')
print(f'Cache: {driver.application_cache}')
driver.find_elements_by_link_text('SOCzOAOac8uhByk5ZGU2Zg==')
driver.quit()