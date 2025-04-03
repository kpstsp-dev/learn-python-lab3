import os
from mistralai import Mistral
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Set your API key (replace with your actual API key)
api_key = os.getenv("API_KEY")

# Initialize the Mistral client
client = Mistral(api_key=api_key)
question="Как пропатчить KDE под FreeBSD?"
# Define the model and input message
model = "mistral-small-latest"  # Free-tier model
messages = [
    {"role": "user", "content": question}
]

# Make a chat completion request
response = client.chat.complete(
    model=model,
    messages=messages,
    max_tokens=300,  # Limit tokens to stay within free-tier restrictions
    temperature=0.7  # Adjust for balanced randomness and focus
)

# Print the response content
print(response.choices[0].message.content)
