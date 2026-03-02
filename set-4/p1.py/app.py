from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    user_name = "Alice"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    fruits = [
        {"name": "Apple", "price": 1.20, "color": "red"},
        {"name": "Banana", "price": 0.50, "color": "yellow"},
        {"name": "Cherry", "price": 2.00, "color": "red"}
    ]

    return render_template(
        "index.html",
        name=user_name,
        time=current_time,
        fruits=fruits
    )

if __name__ == "__main__":
    app.run(debug=True)