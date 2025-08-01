import os
from dotenv import load_dotenv

def get_openai_api_key():
    # Load environment variables from .env file if it exists
    load_dotenv()
    
    # Try to get API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        # If not found in environment, prompt user
        api_key = input("Please enter your OpenAI API key: ").strip()
        
        if not api_key:
            raise ValueError("OpenAI API key is required to run this application.")
    
    return api_key 