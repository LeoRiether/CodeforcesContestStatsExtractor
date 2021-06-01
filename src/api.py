import requests
from lxml import html # type: ignore

base_url = "https://codeforces.com"

class Session(requests.Session):
    def get_html(self, url: str):
        content = self.get(url).content
        return html.fromstring(content)

def find_csrf(page):
    tokens = page.xpath('//input[@name="csrf_token"]')
    if len(tokens) == 0:
        raise Exception("No CSRF token found")
    return tokens[0].value

def logged_in_session(handle: str, password: str) -> Session:
    s = Session()

    login_page = s.get_html(base_url + '/enter')

    s.post(base_url + '/enter', data = dict(
        csrf_token = find_csrf(login_page),
        action = 'enter',
        handleOrEmail = handle,
        password = password,
    ))

    return s
