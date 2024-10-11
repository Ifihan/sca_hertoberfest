from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for notes (replace with a database in a real application)
notes = []


# Implement the main route to render the index.html template
@app.route("/")
def index():
    return render_template("index.html")


# Implement a GET endpoint to retrieve all notes
@app.route("/api/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)


# Implement a GET endpoint to retrieve a single note by ID


# Implement a POST endpoint to create a new note
@app.route("/api/notes", methods=["POST"])
def create_note():
    data = request.json
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Title and content are required"}), 400

    new_note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"],
    }
    notes.append(new_note)
    return jsonify(new_note), 201


# Implement a PUT endpoint to update an existing note

# Implement a DELETE endpoint to remove a note

if __name__ == "__main__":
    app.run(debug=True)
