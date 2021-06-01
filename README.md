# Codeforces Contest Stats Extractor
## CCSE for short

Codeforces Contest Stats Extractor is a Python script that extracts statistics from contests in Codeforces.
Currently, the following extractors are built-in:
+ Status

If you create your own extractor and think it could be useful for others, please consider making a pull request
to add it to this repository.

# Running the Script
It is recommended to have virtualenv installed. You can activate it with `source bin/activate` and then install
the dependencies with `python -m pip install -r requirements.txt`.

With the dependencies installed, create `src/config/credentials.py` in the same style as `src/config/credentials.example.py` and input your Codeforces login information. If someone knows a better way to do this, please tell me.

You can now run the script with `python src/main.py > output.json`.

# TODO
+ Make `contest_url` more configurable