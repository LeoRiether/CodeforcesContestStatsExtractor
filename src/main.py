import config.credentials as creds
from extract import extract
import api

contest_url = 'https://codeforces.com/group/nituVTsHQX/contest/329742'

def main():
    print(f"Hello {creds.handle}! Logging you in...")

    with api.logged_in_session(creds.handle, creds.password) as s:
        print("Logged in!")

        result = extract(s, contest_url)
        print(result)

        print("Done!")


if __name__ == '__main__':
    main()
