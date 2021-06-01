from extractors import status

import api

def extract(session: api.Session, contest_url: str, log=print):
    log("Extracting status...")
    status_res = status.extract(session, contest_url)

    return {
        'status': status_res
    }
