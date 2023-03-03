import openai
from models import GPT3, DALLE2, Codex, ChatGPT

class ChatBot:
    def __init__(self):
        self.models = {
            "GPT-3": GPT3(),
            "DALL-E 2": DALLE2(),
            "Codex": Codex(),
            "ChatGPT": ChatGPT()
        }
        openai.api_key = "<your-openai-api-key>"
    
    def generate_response(self, user_input):
        # Preprocess user input
        processed_input = openai.preprocess(user_input)
        # Select a model based on context
        context = openai.get_context(processed_input)
        model = self.models[context]
        # Generate AI response
        response = model.generate_response(processed_input)
        # Decode response
        decoded_response = openai.decode_response(response)
        return decoded_response
