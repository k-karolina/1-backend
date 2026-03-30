from flask import Flask, jsonify, request
app = Flask(__name__)


databaza = {
    "students": [
        {
            "id": 1,
            "name": "Daniel",
            "surname": "Barta",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 2,
            "name": "Matúš",
            "surname": "Bucko",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 3,
            "name": "Adrian",
            "surname": "Červenka",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 4,
            "name": "Martin",
            "surname": "Deglovič",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 5,
            "name": "Samuel",
            "surname": "Haring",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 6,
            "name": "Matúš",
            "surname": "Holečka",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 7,
            "name": "Martin",
            "surname": "Jelínek",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 8,
            "name": "Tomáš",
            "surname": "Jurčák",
            "nickname": "unknown",
            "image": None,
        },
        {
            "id": 9,
            "name": "Karolína",
            "surname": "Kmeťová",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 10,
            "name": "Milan",
            "surname": "Kokina",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 11,
            "name": "Patrik",
            "surname": "Korba",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 12,
            "name": "Marcus",
            "surname": "Martiš",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 13,
            "name": "Samuel",
            "surname": "Martiš",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 14,
            "name": "Marko",
            "surname": "Mihalička",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 15,
            "name": "Rastislav",
            "surname": "Paták",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 16,
            "name": "Matej",
            "surname": "Randziak",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 17,
            "name": "Dávid",
            "surname": "Škula",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 18,
            "name": "Samuel",
            "surname": "Uhrík",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 19,
            "name": "Janka",
            "surname": "Vargová",
            "nickname": "unknown",
            "image": None,
        },
        {

            "id": 20,
            "name": "Lukáš",
            "surname": "Vindiš",
            "nickname": "unknown",
            "image": None,
        }
    ]
}


@app.route("/")
def home():
    return "Vitaj!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


@app.route("/api")
def api():
    return jsonify(databaza)

@app.route("/api/students/<int:student_id>")
def find_student(student_id):
    student = next((s for s in databaza["students"] if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)