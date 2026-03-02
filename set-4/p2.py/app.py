from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

items = []   # Empty list (no default items)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_item", methods=["POST"])
def add_item():
    data = request.get_json()
    item = data.get("item")

    if item and item.strip() != "":
        items.append(item.strip())
        return jsonify({"status": "success", "item": item.strip()})

    return jsonify({"status": "error"})

if __name__ == "__main__":
    app.run(debug=True)