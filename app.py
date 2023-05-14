from flask import Flask, request, jsonify
from bardapi import Bard
import os

app = Flask(__name__)
os.environ['_BARD_API_KEY'] = "WQjHX5HN4ulBXXLzP-EcxKa9geXfIM3q1fxnF0nyrH3dItOH9D7vEIsCexfBZtK8mWApcg."

# Add the custom domain configuration
app.config['SERVER_NAME'] = 'your-custom-domain.com'

@app.route('/api', methods=['POST'])
def get_bard_content():
    input_text = request.form.get('input')
    content = Bard().get_answer(input_text)['content']
    return jsonify({"content": content})

if __name__ == '__main__':
    # Modify the app.run() line to listen on all available IPs
    app.run(host='0.0.0.0')