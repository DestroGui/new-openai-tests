# Import the tiktoken library, which is used to count tokens in prompts
import tiktoken

# Define a class to analyze prompt size in terms of token count
class PromptAnalyze:
    
    # Constructor method: stores the system and user prompts as instance variables
    def __init__(self, prompt_sistema, prompt_usuario):
        self.prompt_sistema = prompt_sistema
        self.prompt_usuario = prompt_usuario

    # Method to count the total number of tokens in the combined prompt
    def contadorToken(self):
        try:
            # Try to get the token encoder for the cl100k_base encoding (used by GPT-4/3.5-turbo)
            codificador = tiktoken.get_encoding("cl100k_base")
        except Exception:
            # If the specific encoding isn't available, use the model-specific fallback
            codificador = tiktoken.encoding_for_model("gpt-4")  # Fallback to GPT-4 model tokenizer

        # Encode the combined system and user prompt into tokens
        tokens = codificador.encode(self.prompt_sistema + self.prompt_usuario)

        # Return the total number of tokens
        return len(tokens)
