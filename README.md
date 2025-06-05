# 🧠 Multi-Format Autonomous AI System

## 🚀 Overview
An AI system that classifies input format and business intent from uploaded Email, JSON, or PDF, processes the content through specialized agents, and routes contextual follow-up actions automatically.

## 🧩 Architecture

- **Classifier Agent**: Detects input type and business intent.
- **Email Agent**: Extracts sender, tone, urgency, and takes action.
- **JSON Agent**: Validates schema, flags anomalies.
- **PDF Agent**: Extracts invoice data, detects flags.
- **Router**: Chains actions based on agent outputs.
- **Memory Store**: Shared context for trace logging.

## 🛠️ Tech Stack

- Python, FastAPI
- LangChain (optional), Tika, TextBlob
- Redis or SQLite (for memory) – (optional in this build)
- Uvicorn server
- PDF & JSON parsers

## 🧪 Sample Inputs

- 📧 `data/sample_email.txt`
- 📄 `data/invoice_sample.pdf`
- 🟦 `data/sample_webhook.json`

## 🧑‍💻 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/multi_agent_ai.git
cd multi_agent_ai

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI app
uvicorn app.main:app --reload
