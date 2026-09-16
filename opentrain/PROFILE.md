# OpenTrain wizard copy-paste

Fill these fields in **Settings → Profile**. Edit names/dates if the parser already filled them.

## Basic details

| Field | Value |
|---|---|
| Full name | Arun Kumar Kumari Arumugam |
| Display name | Arun Kumar K A |
| City | Chennai |
| Country | India |
| Phone | +91 95669 16623 |
| Email | arunkumar4189@gmail.com |
| LinkedIn | https://www.linkedin.com/in/arunkumar |
| GitHub | https://github.com/arunkumar4189/AI-ML-Projects |
| Languages | English — Fluent; Tamil — Native/Bilingual |
| English level | Fluent |
| Availability | Choose based on your week: **Less than 20 hrs/week** is the conservative default while employed full-time. Switch to **20+ hrs/week** only if you can actually take that load. |
| AI training experience level | **Intermediate (1–3 years)** |
| Hourly rate (USD) | Set after scanning comparable OpenTrain NLP / LLM-eval listings. A reasonable starting band for this profile is **$25–45/hr**; raise if jobs are senior evaluation / domain expert. |

## Public profile

**Profile title** (pick one):

1. **LLM evaluator and domain NLP specialist (healthcare, telecom, software)**
2. NLP / LLM fine-tuning (QLoRA) and evaluation specialist
3. Conversational AI, RAG verification, and production GenAI architect

Recommended: **1**.

**Top industries / subject matter** (rank three):

1. Telecommunications and customer support
2. Healthcare and clinical literature
3. Software engineering and code quality

## Profile overview (min 150 characters)

Paste:

> Distinguished Engineer and M.Tech AI & ML candidate (BITS Pilani) specializing in NLP evaluation, domain LLM adaptation, and production GenAI. I design labeling schemas, train and judge models, and ship agentic systems with human-in-the-loop checks. Coursework implementations cover text classification, NER-style extraction, sentiment via syntax, medical RAG with agentic verification, QLoRA SFT, prompt routing, conversational state tracking, image classification, and RL evaluation. At Verizon I lead Agentic Universe and an SRE triaging multi-agent that correlates logs, Git, Jira, and Kubernetes changes into evidence-backed RCA. Looking for OpenTrain work in LLM evaluation, SFT data quality, domain NLP, and safety/groundedness review.

Character count is well above 150.

---

## Skills (matching engine)

Select only what you can defend in a screen.

### Data type expertise

- Text
- Document
- Code
- Image
- Medical

### Task type expertise

- Classification
- Named entity recognition (NER)
- Sentiment analysis
- Evaluation / rating
- Fine-tuning / SFT
- Instruction data creation
- Prompt engineering
- RAG groundedness / factuality review
- Transcription is **not** claimed
- Bounding box / polygon / 3D / geospatial are **not** claimed

### AI data labeling software

Hands-on, honest list:

- Jupyter / notebook-based annotation and review
- Hugging Face (datasets, Hub, Inference API, PEFT/QLoRA)
- scikit-learn evaluation reports
- MLflow experiment tracking
- Gradio / Streamlit review UIs
- spaCy / NLTK linguistic annotation pipelines
- GitHub (guidelines, PRs, reproducible notebooks)

Leave Scale AI, Labelbox, CVAT, Encord, Roboflow, Appen, Remotasks **unchecked** unless you later add real hours on them.

---

## Labeling experience entries

Add **one entry per tool/theme**. Dates overlap on purpose (M.Tech 2025–2027).

### 1. Hugging Face — medical LLM SFT and prompt evaluation

- **Title:** Medical instruction data, QLoRA SFT, and prompt-pattern evaluation
- **Platform / tool:** Hugging Face (Transformers, PEFT/QLoRA, Hub)
- **Data types:** Text, Document, Medical
- **Label types:** Fine-tuning / SFT, Instruction data, Evaluation / rating, Classification
- **From–to:** 2025 – present (ongoing)
- **Description:** Built a medical PDF corpus and instruction JSONL, QLoRA-fine-tuned GPT-2 Medium, then evaluated zero-shot, few-shot, instruction, self-critique, JSON function-calling, CoT/ToT/self-consistency/ReAct, and a prompt router. Measured tokens, latency, and answer quality under greedy decoding. Repo: `LLM-Gen-AI/`.

### 2. Jupyter + spaCy/NLTK — linguistic annotation and QA

- **Title:** POS, NER, dependency sentiment, and medical QA verification
- **Platform / tool:** Jupyter, NLTK, spaCy-style pipelines, Hugging Face Transformers
- **Data types:** Text, Document, Medical
- **Label types:** NER, Classification, Sentiment, Evaluation / rating
- **From–to:** 2025 – present (ongoing)
- **Description:** POS/HMM tagging on Boston Airbnb reviews; dependency-based negation and intensifier features for restaurant sentiment; news tagging with from-scratch Naïve Bayes and Rocchio; medical search with k-gram/Soundex spelling correction; medical QA with retrieval, generation, and an agentic verify-and-correct loop. Repo: `NLP/`, `IR/`.

### 3. Gradio / Streamlit / MLflow — production-style review UIs

- **Title:** Support ticket triage and telecom churn model review
- **Platform / tool:** Gradio, Streamlit, MLflow, Hugging Face Inference API
- **Data types:** Text, Image, Document
- **Label types:** Classification, Sentiment, Evaluation / rating, Fine-tuning
- **From–to:** 2025 – present (ongoing)
- **Description:** SupportSense orchestrates complaint classification (DistilBERT+LoRA on Banking77), sentiment, summarization, FAQ extractive QA, image defect/caption, and draft replies with logging and metrics. Telco churn pipeline trains Logistic Regression and Random Forest, tracks runs in MLflow, and surfaces results in Streamlit. Repo: `API Driven Cloud Native/`.

### 4. GitHub + custom eval harnesses — model judging

- **Title:** Summarization, retrieval, RL, and vision-language evaluation
- **Platform / tool:** GitHub, PyTorch, CLIP, Gymnasium
- **Data types:** Text, Image, Code
- **Label types:** Evaluation / rating, Classification, Fine-tuning
- **From–to:** 2025 – present (ongoing)
- **Description:** Seq2Seq Transformer summarization with ROUGE; CLIP knowledge distillation with Recall@K; CNN cats-vs-dogs; software-defect classification; MiniChess DP; bandit product recs; Q-learning/DQN/DDQN on HalfCheetah. Emphasis on comparable metrics and ablation (with vs without distillation/KD). Repo: `Conversational AI/`, `DNN/`, `ML/`, `DRL/`.

### 5. Internal / production GenAI (Verizon) — HITL agent evaluation

- **Title:** Multi-agent RCA and self-service agent platform with human-in-the-loop
- **Platform / tool:** Internal tooling (LangGraph, MCP, FastAPI, OpenSearch)
- **Data types:** Text, Document, Code
- **Label types:** Evaluation / rating, Classification, NER-style extraction
- **From–to:** 2025 – present (ongoing)
- **Description:** Designed Agentic Universe (visual workflows, run history, HITL validation) and an SRE triaging service that correlates OpenSearch logs, Git diffs, Jira, and Kubernetes change windows into evidence-backed RCA. Work includes rubric design for agent outputs, groundedness, and escalation — the same skills as LLM-as-judge / RLHF-style review.

---

## Work experience (non-labeling)

Keep parser output, then tighten bullets to this:

### Verizon India — Chennai | Jan 2016 – Present

**Distinguished Engineer, Software Development** | Sep 2025 – Present

- Lead enterprise GenAI and agentic AI roadmaps; launched Agentic Universe (React, FastAPI, MCP, PostgreSQL) with visual workflows, run history, and human-in-the-loop validation.
- Built SRE Triaging Service: LangGraph multi-agent RCA over OpenSearch, Git, Jira, and Kubernetes change windows.
- Architecture board member; secured internet-facing path (Akamai, 42Crunch, APIGEE).
- Org-wide Claude Code / GitHub Copilot adoption; MCP agent companion for planning, tests, and reviews.

**Principal Engineer / Solutions Architect (MTS)** | Jan 2021 – Sep 2025

- Principal architect for B2B SMB/NSE ordering migration (Spring Reactive, GraphQL, Cassandra).
- Led SMB Enrollment and Add-A-Line (case management, OCR ScanID, adaptive auth, credit checks, PEGA).
- Bulk order engine at 10K+ orders per payload (RabbitMQ, Netflix OSS); 99.99% uptime with New Relic.

**Senior Technical Architect (MTS)** | Oct 2018 – Jan 2021

- Event-driven REST APIs for large B2B carts; Quote-to-Order automation; internal API libraries.

**Lead Developer (MTS3)** | Jan 2016 – Oct 2018

- Foundational commerce microservices (Cart, Config, Payment); Retail Flex Flow on Oracle ATG 11.

### Tech Mahindra — Chennai | Associate Tech Specialist | Jan 2014 – Jan 2016

- Transaction-heavy WebLogic commerce apps; catalog, pipeline, and order-repository customization.

### Wipro Technologies — Chennai | Software Engineer | Nov 2010 – Nov 2013

- ATG e-commerce customization; REST services for profile, tax, shipping, promotions.

---

## Education

| School | Degree | Field | Years |
|---|---|---|---|
| BITS Pilani | M.Tech | Artificial Intelligence & Machine Learning | 2025 – 2027 (expected) |
| Adhiparasakthi Engineering College, Anna University | B.E. | Computer Science & Engineering | 2010 (77.06%) |
