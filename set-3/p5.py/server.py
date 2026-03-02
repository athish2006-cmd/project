from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the input form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the submission and show the result page
@app.route('/process', methods=['POST'])
def process():
    user_input = request.form.get('user_input')
    
    if user_input:
        reversed_data = user_input[::-1]
        # Render the separate result file and pass the data to it
        return render_template('result.html', final_output=reversed_data)
    else:
        return "No input provided!", 400

if __name__ == '__main__':
    app.run(debug=True)