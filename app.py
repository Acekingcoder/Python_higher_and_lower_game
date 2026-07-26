import os
import random
from flask import Flask, render_template, request, session, redirect, url_for

from data import topics, get_pageviews

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-fallback-do-not-use-in-production")


def find_valid_topic(exclude_slugs):
    """Try random topics (skipping ones in exclude_slugs) until one returns
    usable pageview data, or every topic has been tried and failed."""
    candidates = [t for t in topics if t["slug"] not in exclude_slugs]
    random.shuffle(candidates)
    for topic in candidates:
        views = get_pageviews(topic["slug"])
        if views is not None:
            return topic, views
    return None, None


def pick_new_topic(exclude_slug):
    """Pick a random topic that isn't the one currently shown."""
    choice = random.choice(topics)
    while choice["slug"] == exclude_slug:
        choice = random.choice(topics)
    return choice


def start_round(carry_over_topic=None, carry_over_views=None):
    """Load a fresh blind pair into the session. If a topic is carried over
    from the previous round, it becomes A; otherwise A is picked fresh.
    Falls back to an error state if the Wikipedia API is unreachable for
    every topic tried."""
    if carry_over_topic is not None and carry_over_views is not None:
        topic_a, views_a = carry_over_topic, carry_over_views
    else:
        topic_a, views_a = find_valid_topic(exclude_slugs=set())
        if topic_a is None:
            session["state"] = "error"
            return

    topic_b, views_b = find_valid_topic(exclude_slugs={topic_a["slug"]})
    if topic_b is None:
        session["state"] = "error"
        return

    session["topic_a"] = topic_a
    session["views_a"] = views_a
    session["topic_b"] = topic_b
    session["views_b"] = views_b
    session["state"] = "guessing"


@app.route("/")
def index():
    if "score" not in session or "state" not in session:
        session["score"] = 0
        start_round()

    state = session.get("state", "guessing")

    if state == "error":
        return render_template("index.html", state="error", score=session.get("score", 0))

    if state == "reveal":
        return render_template(
            "index.html",
            state="reveal",
            topic_a=session["topic_a"],
            topic_b=session["topic_b"],
            views_a=session["views_a"],
            views_b=session["views_b"],
            was_correct=session.get("was_correct", False),
            score=session["score"],
        )

    if state == "game_over":
        return render_template(
            "index.html",
            state="game_over",
            topic_a=session["topic_a"],
            topic_b=session["topic_b"],
            views_a=session["views_a"],
            views_b=session["views_b"],
            score=session["score"],
        )

    return render_template(
        "index.html",
        state="guessing",
        topic_a=session["topic_a"],
        topic_b=session["topic_b"],
        score=session["score"],
    )


@app.route("/guess", methods=["POST"])
def guess():
    guess_value = request.form.get("guess")
    topic_a = session.get("topic_a")
    topic_b = session.get("topic_b")
    views_a = session.get("views_a")
    views_b = session.get("views_b")

    if not topic_a or not topic_b or views_a is None or views_b is None:
        return redirect(url_for("index"))

    correct_choice = "a" if views_a > views_b else "b"
    is_correct = guess_value == correct_choice

    if is_correct:
        session["score"] = session.get("score", 0) + 1
        session["state"] = "reveal"
        session["was_correct"] = True
    else:
        session["state"] = "game_over"

    return redirect(url_for("index"))


@app.route("/next", methods=["POST"])
def next_round():
    # The winning topic (B, since it was compared against and wins ties too)
    # slides into the A slot for the next round.
    carry_topic = session.get("topic_b")
    carry_views = session.get("views_b")
    start_round(carry_over_topic=carry_topic, carry_over_views=carry_views)
    return redirect(url_for("index"))


@app.route("/restart", methods=["POST"])
def restart():
    session["score"] = 0
    start_round()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)