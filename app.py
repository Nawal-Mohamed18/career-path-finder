"""Career Path Finder — Flask web app."""

import os

from flask import Flask, jsonify, render_template, request

from careers_data import CAREERS, QUESTIONS, score_answers

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/careers")
def api_careers():
    return jsonify(
        {
            key: {
                "title": c["title"],
                "tagline": c["tagline"],
                "skills": c["skills"],
                "path": c["path"],
            }
            for key, c in CAREERS.items()
        }
    )


@app.route("/api/questions")
def api_questions():
    return jsonify(
        [
            {
                "id": q["id"],
                "text": q["text"],
                "options": [{"label": opt["label"]} for opt in q["options"]],
            }
            for q in QUESTIONS
        ]
    )


@app.route("/api/quiz", methods=["POST"])
def api_quiz():
    data = request.get_json(silent=True) or {}
    answers = data.get("answers", [])
    if not isinstance(answers, list) or len(answers) != len(QUESTIONS):
        return jsonify({"error": "Send answers as a list matching all questions."}), 400

    ranked = score_answers(answers)
    best_key, best_score = ranked[0]
    second_key, second_score = ranked[1]
    return jsonify(
        {
            "best": {"key": best_key, "score": best_score, **CAREERS[best_key]},
            "second": {
                "key": second_key,
                "score": second_score,
                "title": CAREERS[second_key]["title"],
            },
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
