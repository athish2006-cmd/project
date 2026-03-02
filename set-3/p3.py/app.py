import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template

app = Flask(__name__)

# CONFIGURATION
# Define the folder where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
# Check if folder exists, if not, create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Limit file size to 16MB (Optional security step)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# --- ROUTES ---

@app.route('/')
def home():
    """Renders the homepage and lists uploaded files."""
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles the file upload logic."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    # If user does not select file, browser submits an empty part without filename
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('home'))

@app.route('/download/<filename>')
def download_file(filename):
    """Allows the user to download a file."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)