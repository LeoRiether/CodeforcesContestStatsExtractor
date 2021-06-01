from typing import List, Iterator
from collections import namedtuple
import doctest
import api

Submission = namedtuple('Verdict', ['when', 'who', 'problem', 'lang', 'verdict', 'test', 'time', 'memory'])

def status_pages(session: api.Session, contest_url: str):
    """ Returns an iterator over all status pages """

    first_page = session.get_html(contest_url + '/status')
    yield first_page

    last_index = int(first_page.xpath('//span[@pageindex]')[-1].get('pageindex'))
    for index in range(2, last_index):
        yield session.get_html(f'{contest_url}/status/page/{index}')

def parse_verdict(text: str):
    """
        Parses a verdict status into a pair (verdict abbreviation, test number)

        >>> parse_verdict("Accepted")
        ("AC", 0)

        >>> parse_verdict("Wrong answer on test 10")
        ("WA", 10)

        >>> parse_verdict("Memory limit exceeded on test 110")
        ("MLE", 110)
    """

    split = text.split(' on test ')
    status = split[0].lower()
    test = 0 if len(split) <= 1 else int(split[1].strip())

    abbr = {
        'accepted': 'AC',
        'pretests passed': 'pAC',
        'wrong answer': 'WA',
        'runtime error': 'RTE',
        'time limit exceeded': 'TLE',
        'compilation error': 'CE',
        'presentation error': 'PE',
        'idleness limit exceeded': 'ILE',
        'denial of judgement': 'DOJ',
        'memory limit exceeded': 'MLE',
        'skipped': 'SKIP',
        'rejected': 'REJ',
        'hacked': 'HACK',
        'running': 'RUN',
    }

    return abbr.get(status, '???'), test

def submissions(page) -> Iterator[Submission]:
    rows = page.xpath('//table[@class="status-frame-datatable"]/tr[@data-submission-id]')

    def make_submission(row):
        content = lambda element: element.text_content().strip().replace('\xa0', '')
        xcontent = lambda xpath: content(row.xpath(xpath)[0])

        verdict, test = parse_verdict(xcontent('td[@submissionid]'))

        return Submission(
            when = content(row[1]),
            who = xcontent('td[@data-participantid]'),
            problem = xcontent('td[@data-problemid]'),
            lang = content(row[4]),
            verdict = verdict,
            test = test,
            time = int(xcontent('td[@class="time-consumed-cell"]')[:-2]), # in ms
            memory = int(xcontent('td[@class="memory-consumed-cell"]')[:-2]), # in KB
        )

    return (
        make_submission(row)
        for row in rows
    )

def extract(session: api.Session, contest_url: str) -> List[Submission]:
    """
        Extracts all of the submissions of the status pages of a given contest
    """

    return [
        submission
        for page in status_pages(session, contest_url)
        for submission in submissions(page)
    ]


