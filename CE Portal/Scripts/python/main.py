from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def redirect_to_main():
    return redirect('/main')

@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/endpoint1', methods=['POST'])
def handle_endpoint1():
    # Call script1.py and pass the request data
    result = subprocess.run(['python', 'script1.py'], input=request.data, capture_output=True)
    return result.stdout, result.returncode

@app.route('/endpoint2', methods=['POST'])
def handle_endpoint2():
    # Call script2.py and pass the request data
    result = subprocess.run(['python', 'script2.py'], input=request.data, capture_output=True)
    return result.stdout, result.returncode

# Add more route handlers for other endpoints as needed

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
