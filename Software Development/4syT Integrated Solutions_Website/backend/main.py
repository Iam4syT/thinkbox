from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from agents.website_agent import WebsiteAgent

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Website Agent
agent = WebsiteAgent()

@app.route('/api/rag', methods=['POST'])
def rag_endpoint():
    data = request.json or {}
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    # Get response from the website assistant agent
    answer = agent.answer_query(query)
    return jsonify({'answer': answer})

@app.route('/api/contact', methods=['POST'])
def contact_endpoint():
    data = request.json or {}
    # Extract fields
    name = data.get('name', '')
    email = data.get('email', '')
    phone = data.get('phone', '')
    service = data.get('service', '')
    message = data.get('message', '')
    
    # Log contact form submission (simulate email notification/db record)
    print(f"NEW CONTACT FORM SUBMISSION:")
    print(f"Name: {name} | Email: {email} | Phone: {phone}")
    print(f"Service: {service}")
    print(f"Message: {message}")
    
    return jsonify({'ok': True, 'message': 'Contact form submitted successfully!'})

@app.route('/api/newsletter', methods=['POST'])
def newsletter_endpoint():
    data = request.json or {}
    email = data.get('email', '')
    if not email:
        return jsonify({'error': 'Email parameter is required'}), 400
        
    print(f"NEW NEWSLETTER SUBSCRIPTION: {email}")
    return jsonify({'ok': True, 'message': 'Subscribed successfully!'})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5002))
    app.run(host='0.0.0.0', port=port, debug=True)
