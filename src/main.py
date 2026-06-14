import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables from .env
load_dotenv()

# Initialize the client (reads ANTHROPIC_API_KEY automatically, but explicit is fine too)
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Make a simple request
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=50,
    messages=[
        {"role": "user", "content": "Say hello and introduce yourself briefly."}
    ]
)

print(message.content[0].text)