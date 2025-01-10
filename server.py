from flask import Flask, jsonify, request
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/')
def home():
    return jsonify("Welcome to the Gaido Backend!")

@app.route('/api/events', methods=['GET'])
def get_events():
    category = request.args.get('category')
    if category:
        response = supabase.table('events').select('*').eq('category', category).execute()
    else:
        response = supabase.table('events').select('*').execute()
    #return response.data
    return jsonify(response.data)

if __name__ == '__main__':
    app.run(debug=False)