import sys
import json
import config.credentials as creds
from extract import extract
import api

contest_url = 'https://codeforces.com/group/nituVTsHQX/contest/329742'

def log(*x):
    print(*x, file=sys.stderr)

def main():
    log(f"Hello {creds.handle}! Logging you in...")

    with api.logged_in_session(creds.handle, creds.password) as s:
        log("Logged in!")

        result = extract(s, contest_url, log)
        print(json.dumps(result))

        log("Done!")


if __name__ == '__main__':
    main()
