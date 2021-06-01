from extractors import status

import api

def extract(session: api.Session, contest_url: str, log=print):
    log_e = lambda name: log(f"Extracting \033[92m{name}\033[0m...")

    log_e("status")
    status_res = status.extract(session, contest_url)

    return {
        'status': list(map(lambda x: x._asdict(), status_res))
    }
