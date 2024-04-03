from flask import Flask, jsonify, request ,render_template

app = Flask(__name__)

GAMES = [
    {
        "id": 1,
        "title": "Game 1",
        "platform": "PC",
        "completion_status": "In Progress",
        "hours_played": 10,
        "levels_completed": 5
    },
    {
        "id": 2,
        "title": "Game 2",
        "platform": "PS4",
        "completion_status": "Completed",
        "hours_played": 20,
        "levels_completed": 10
    }
]

@app.route('/')
def home():
    return render_template('thirdtest.html')


@app.route("/games", methods=["GET"])
def get_games():
    return jsonify(GAMES)

@app.route("/games/<int:game_id>", methods=["GET"])
def get_game(game_id):
    game = next((g for g in GAMES if g["id"] == game_id), None)
    if game:
        return jsonify(game)
    else:
        return jsonify({"error": "Game not found"})

@app.route("/games", methods=["POST"])
def add_game():
    data = request.get_json()
    new_game = {
        "id": len(GAMES) + 1,
        "title": data["title"],
        "platform": data["platform"],
        "completion_status": "In Progress",
        "hours_played": 0,
        "levels_completed": 0
    }
    GAMES.append(new_game)
    return jsonify(new_game)

@app.route("/games/<int:game_id>", methods=["PUT"])
def update_game(game_id):
    game = next((g for g in GAMES if g["id"] == game_id), None)
    if game:
        data = request.get_json()
        game.update(data)
        return jsonify(game)
    else:
        return jsonify({"error": "Game not found"})
    

if __name__ == '__main__':
    app.run(debug=True)

