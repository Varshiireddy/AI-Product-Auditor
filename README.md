# 🤖 AI Product Auditor

AI Product Auditor is a modular framework for evaluating Large Language Models (LLMs). It generates model responses, evaluates them using multiple evaluation strategies, and produces detailed JSON and HTML reports to help analyze model performance.

---

## ✨ Features

- ✅ Run evaluation datasets against LLMs
- ✅ Keyword-based evaluation
- ✅ Exact match evaluation
- ✅ Semantic similarity evaluation using embeddings
- ✅ LLM-as-a-Judge evaluation
- ✅ JSON report generation
- ✅ Interactive HTML report generation
- ✅ Modular architecture for easily adding new evaluators
- ✅ Command-line interface (CLI)
- ✅ Local inference using Ollama

---

## 🏗️ Architecture

```text
                   +----------------------+
                   |    Evaluation JSON   |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   |    Dataset Loader    |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   |     Audit Runner     |
                   +----------+-----------+
                              |
               +--------------+--------------+
               |                             |
               v                             v
     +-------------------+         +----------------------+
     | Ollama Connector  |         | Embedding Provider   |
     +-------------------+         +----------------------+
               |                             |
               +-------------+---------------+
                             |
                             v
                 +--------------------------+
                 |      Evaluators          |
                 |--------------------------|
                 | • Keyword               |
                 | • Exact Match           |
                 | • Semantic Similarity   |
                 | • LLM Judge             |
                 +-------------+------------+
                               |
                               v
                   +-----------------------+
                   |   Evaluation Report   |
                   +-----------+-----------+
                               |
                +--------------+--------------+
                |                             |
                v                             v
          JSON Report                 HTML Report
```

---

# 📂 Project Structure

```text
AI_Product_Auditor/

├── app/
│   ├── cli.py
│   │
│   ├── connectors/
│   │   ├── base_connector.py
│   │   └── ollama_connector.py
│   │
│   ├── core/
│   │   ├── audit_runner.py
│   │   └── dataset_loader.py
│   │
│   ├── embeddings/
│   │   ├── base_embedding_provider.py
│   │   └── ollama_embedding_provider.py
│   │
│   ├── evaluators/
│   │   ├── base_evaluator.py
│   │   ├── keyword_evaluator.py
│   │   ├── exact_match_evaluator.py
│   │   ├── semantic_similarity_evaluator.py
│   │   └── llm_judge_evaluator.py
│   │
│   ├── models/
│   │
│   ├── reports/
│   │   ├── json_report_generator.py
│   │   └── html_report_generator.py
│   │
│   ├── utils/
│   │   └── math_utils.py
│   │
│   └── main.py
│
├── data/
│   ├── test_sets/
│   └── generated_reports/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Product_Auditor.git

cd AI_Product_Auditor
```

---

## 2. Create a virtual environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama from

https://ollama.com/download

---

## 5. Pull the required models

```bash
ollama pull qwen2.5:3b

ollama pull embeddinggemma
```

---

# 🚀 Usage

Run the auditor

```bash
python -m app.main --dataset factuality --model qwen2.5:3b
```

Example

```bash
python -m app.main \
    --dataset factuality \
    --model qwen2.5:3b
```

---

# 📊 Evaluation Pipeline

For every test case, the framework performs the following steps:

1. Load the evaluation dataset.
2. Generate a response using the selected LLM.
3. Run all configured evaluators.
4. Aggregate the evaluation results.
5. Generate a JSON report.
6. Generate an interactive HTML report.
7. Automatically open the HTML report in the browser.

---

# 📈 Evaluation Metrics

### Keyword Evaluator

Checks whether the expected keyword appears in the generated response.

---

### Exact Match Evaluator

Compares the generated response with the reference answer after normalization.

---

### Semantic Similarity Evaluator

Uses embedding vectors and cosine similarity to measure semantic similarity between the generated response and the reference answer.

---

### LLM Judge Evaluator

Uses an LLM to evaluate:

- Correctness
- Relevance
- Clarity

The judge returns a normalized score and explanation.

---

# 📄 Reports

The framework automatically generates:

## JSON Report

Contains

- Individual test results
- Evaluator scores
- Latency
- Overall summary

---

## HTML Report

Interactive dashboard containing

- Summary statistics
- Individual test cards
- Evaluator scores
- Pass/Fail indicators
- Model responses

---

# 📌 Example Dataset

```json
[
  {
    "name": "Capital Question",
    "prompt": "What is the capital of France?",
    "category": "Geography",
    "expected_keyword": "Paris",
    "reference_answer": "The capital of France is Paris."
  }
]
```

---

# 🔮 Future Improvements

- Support additional LLM providers
- Add more evaluation metrics
- Support larger benchmark datasets
- Export reports in additional formats
- Add configurable evaluation thresholds

---

# 🛠️ Technologies Used

- Python
- Ollama
- Qwen 2.5
- EmbeddingGemma
- HTML
- JSON
- argparse

---

# 📷 Screenshots

Add screenshots of the generated HTML report here.

Example

```
screenshots/report.png
```

---

# 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Varshitha**
LinkedIn:https://www.linkedin.com/in/varshitha-kondeti-vr2002/
GitHub:https://github.com/Varshiireddy

Aspiring AI Engineer passionate about building AI systems, LLM evaluation frameworks, and applied AI solutions.