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

## 🧠 Agent Flow & Chaining Architecture
![image](https://github.com/user-attachments/assets/90b1560a-932c-41e8-845b-257b01aa821a)

## 🧪 Sample Input Files

All sample test inputs used in the demo can be found under the `data/` folder:

- `complaint_email.txt` – Escalation case
- `sample_email.txt` – Routine email
- `sample_invoice.pdf` – High-value invoice with GDPR mention
- `sample_webhook_valid.json` – Well-structured webhook
- `sample_webhook_invalid.json` – Invalid fields to trigger anomaly detection

  
## 🧾 Output Logs

The `logs/` directory contains output JSONs for all the sample inputs processed through the system:

- `complaint_email_output.json`
- `sample_email_output.json`
- `sample_invoice_output.json`
- `sample_webhook_valid_output.json`
- `sample_webhook_invalid_output.json`

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
