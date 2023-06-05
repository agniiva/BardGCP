from flask import Flask, request, jsonify
import os
import bardapi

# set your __Secure-1PSID value to key
token = os.getenv('BARD_API_KEY', 'WQjHX5HN4ulBXXLzP-EcxKa9geXfIM3q1fxnF0nyrH3dItOH9D7vEIsCexfBZtK8mWApcg.')
app = Flask(__name__)

# Add the custom domain configuration
app.config['SERVER_NAME'] = 'your-custom-domain.com'

@app.route('/api', methods=['POST'])
def get_bard_content():
    # set your input text from request
    input_text = request.form.get('input')
    response = bardapi.core.Bard(token).get_answer(input_text)
    return jsonify(response)

if __name__ == '__main__':
    # Modify the app.run() line to listen on all available IPs
    app.run(host='0.0.0.0')
