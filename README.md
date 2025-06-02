# OpenAI Requests Service

This project uses the OpenAI API to perform analysis and classification tasks through a Python script. It includes a virtual environment setup, modular structure, and easy-to-use CLI functionality.

---

## 🚀 Features

- Modular Python code (`main.py`, `data_getter.py`, `token_analyzer.py`)
- OpenAI API integration
- Virtual environment support with `requirements.txt`
- Data input via CSV file

---

## 🔑 Get an OpenAI API Key on GitHub

> **Important**: Never share your API key publicly. Do not upload it to GitHub.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/DestroGui/openai-requests-service.git
cd openai-requests-service
```

## 2. Create and Activate a Virtual Environment

🔵 Windows:

```bash
python -m venv venv
venv\Scripts\activate
```
🟣 macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Required Packages

```bash
pip install -r requirements.txt
```

## 4. Create a .env File

Duplicate the .env file:

```bash
cp .env.example .env  # or just create a new .env manually
```

Open .env and add your OpenAI API key:

```OPENAI_API_KEY=sk-your_api_key_here```

📁 Project Structure

├── main.py

├── data_getter.py

├── token_analyzer.py

├── requirements.txt

├── .env

├── dados/

│   └── MOCK_DATA.csv

├── venv/


✅ Run the Script

```
python main.py
```
