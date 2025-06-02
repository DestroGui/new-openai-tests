# Import necessary libraries for environment variable loading, OpenAI API access, and file handling
from dotenv import load_dotenv
from openai import OpenAI
import openai
import os

# Import custom utility classes for file loading and token analysis
from data_getter import FuncoesArquivos
from token_analyze import PromptAnalyze

# Load environment variables from a .env file (e.g., to securely access the OpenAI API key)
load_dotenv()

# Retrieve the OpenAI API key from environment variables
token = os.environ["OPENAI_API_KEY"]

# Define the custom API endpoint and initial model
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"  # Initial GPT model to use

# Initialize the OpenAI client with the endpoint and API key
client = OpenAI(
    base_url=endpoint,
    api_key=token
)

list_categorize = [
    'Request for data analysis',
    'Request to categorize/classify data',
    'Request for insights from data',
    'Conceptual or theoretical data question',
    'Technical question about data tools or methods',
    'Not related to data analysis'
]

prompt_system_categorize = f"""
    You are an AI that classifies prompts into ONE AND ONLY ONE category from the following list:

    {list_categorize}

    # Instructions:
    - Read the user's prompt carefully.
    - Choose the ONE category that best fits the intent of the prompt.
    - Do NOT explain your answer.
    - Do NOT include any extra text or punctuation.
    - Output ONLY the exact name of the selected category.

    - If the prompt does not clearly match any category, select "Question not involving data analysis".

    # Output:
"""

# Load a CSV file using the custom class `FuncoesArquivos`
file_csv = FuncoesArquivos("dados/MOCK_DATA.csv")

# Create a user prompt with the content of the CSV file for the model to analyze
prompt_user = f"""
    Using the data below, give me Data analysis on it

    {file_csv.load_file()}
"""

# Categorizing the prompt from the user
messages = [
    {"role": "system", "content": prompt_system_categorize},
    {"role": "user", "content": prompt_user}
]

response = client.chat.completions.create(
    model=model, # aqui colocamos um modelo fraco só pra categorizar
    messages=messages,
    temperature=0,
    top_p=1
)

category = response.choices[0].message.content.strip()
print(f"Categoria escolhida: {category}")

match category:
    case 'Request for data analysis':
        prompt_system = """
            Do a data analysis on the file and return some KPIs
        """
    case 'Request to categorize/classify data':
        prompt_system = """
            Categorize the data the user sent and return in bullet points with each quantity
        """
    case 'Request for insights from data':
        prompt_system = """
            Give insights for each main metric
        """


# Combine the system and user prompts using the custom `PromptAnalyze` class
prompts = PromptAnalyze(prompt_system, prompt_user)

# Check the token count to determine if the prompt is too long
if prompts.contadorToken() >= 10:
    model = "openai/gpt-4.1"  # A placeholder for switching to a more powerful model if needed
    print(f"Entrou no if com {prompts.contadorToken()} tokens")

messages = [
    {"role": "system", "content": prompt_system},
    {"role": "user", "content": prompt_user}
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1,
    top_p=1
)

# Print the generated response from the assistant
print(response.choices[0].message.content)