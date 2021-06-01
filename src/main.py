import sys
import credentials as creds
import session
from extract import extract, Submission

contest_url = 'https://codeforces.com/group/nituVTsHQX/contest/328710/status'

def log(*x):
    print(*x, file=sys.stderr)

def output_csv(result):
    import csv
    w = csv.writer(sys.stdout)

    w.writerow(Submission._fields) # header
    for row in result:
        w.writerow(row)

def main():
    log(f"Hello \033[95m{creds.handle}\033[0m! Logging you in...")

    with session.logged_in(creds.handle, creds.password) as s:
        log("Logged in!")
        log("Extracting...")

        log_page = lambda index: log(f"Processed page \033[91m{index+1}\033[0m")

        result = extract(s, contest_url, log_page)
        output_csv(result)

        log("Done!")


if __name__ == '__main__':
    main()
