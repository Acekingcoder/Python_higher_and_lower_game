# Cloutline — Higher or Lower

A Flask port of the classic "which one has more?" guessing game — instead of
static numbers, it pulls real monthly pageview counts live from the Wikimedia
Pageviews REST API for each round.

## Stack

- Python 3 / Flask
- `requests` for live calls to the Wikimedia Pageviews API
- Server-rendered Jinja templates (no JS framework — logic stays in Python)
- Session-based score tracking (no database needed)

## Run locally

```bash
pip install flask requests
python app.py
```

Then open http://127.0.0.1:5000

## Structure

```
app.py           # routes: / (new game), /guess (POST), /restart (POST)
data.py          # account data (name, description, country, follower_count)
templates/
  index.html     # single-page game view
static/
  style.css      # dark "social exchange" scoreboard theme
```

## Before deploying

Replace `app.secret_key` in `app.py` with a real secret
(e.g. `python -c "import secrets; print(secrets.token_hex(32))"`) and set it
via an environment variable rather than hardcoding it.
