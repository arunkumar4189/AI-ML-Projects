# OpenTrain copy-paste fields

## Profile title

```
LLM evaluation, medical SFT & NLP annotation | Agentic HITL | Telco & code domain
```

Shorter alternative if the field is tight:

```
AI trainer: LLM eval, medical SFT, NER & agentic HITL
```

## Experience level

`Intermediate (1–3 years)` of AI training / evaluation / annotation.

(15+ years of software engineering is listed under work history, not as labeling tenure.)

## Profile overview

Paste as a single block (well over the 150-character minimum):

```
Distinguished Engineer (Verizon) and M.Tech AI/ML candidate (BITS Pilani) specializing in LLM evaluation, supervised fine-tuning data, medical/clinical NLP, and human-in-the-loop agent workflows. I design rubrics, write instruction–response pairs, score model outputs for factuality, safety, and instruction-following, and review multi-agent traces (MCP, LangGraph, RAG) before they ship.

Hands-on from this portfolio: QLoRA SFT on medical documents; prompt-system design (CoT, ToT, self-consistency, ReAct, JSON tool-calling, self-critique); grounded medical QA with a verify-and-correct loop; intent/slot/NER annotation for a task-oriented helpdesk; POS + NER; sentiment with syntactic negation; document classification; image classification; and preference-style evaluation for recommendation and RL policies.

I am strongest where labeling needs domain judgment — healthcare text, telecom/order-management software, Python/Java/TypeScript code, and agent tool-use traces — not high-volume commodity boxes. I write clear rationales, keep gold standards consistent, and flag hallucinations, unsafe advice, and ungrounded citations.
```

## Top industries / subject matter (rank 3)

1. Healthcare / medical NLP and clinical document QA  
2. Telecommunications / enterprise software and ordering systems  
3. LLM evaluation, alignment, and AI safety (HITL, red-teaming, rubric scoring)

## Skills to select in the wizard

### Data type expertise

- Text  
- Document  
- Code  
- Image  
- Medical  

### Task type expertise

- Classification  
- Named entity recognition (NER)  
- Evaluation / rating / side-by-side preference  
- Supervised fine-tuning (SFT) / instruction data  
- Fine-tuning (QLoRA / LoRA)  
- RLHF / reward-style preference (course + production HITL; not a full-time RLHF vendor role)  
- Red-teaming / adversarial prompts / safety review  
- Prompt engineering  
- Question answering / RAG groundedness review  
- Dialogue / intent & slot annotation  
- Image classification (not polygon/segmentation unless you later do CVAT work)

### Software (only if the list includes them)

- Internal / proprietary tooling  
- Hugging Face  
- Jupyter / Python  
- MLflow  
- Gradio  
- Streamlit  

## Languages

| Language | Suggested proficiency |
|---|---|
| English | Fluent |
| Tamil | Native/Bilingual — **only if true**; not stated on the career resume |

## Contact (auto-fill check)

- Location: Chennai, India  
- Email: arunkumar4189@gmail.com  
- Phone: +91 95669 16623  
- LinkedIn: linkedin.com/in/arunkumar  

## Labeling experience rows

Add **separate rows**. Paste the short description into the notes/description field if the wizard has one; otherwise keep the long form in applications and in `PORTFOLIO.md`.

### Row 1 — Internal tooling (Verizon)

- Platform: Internal / proprietary (Agentic Universe, MCP agents, LangGraph)  
- Dates: Jan 2024 – Present (adjust if your GenAI work started later)  
- Data types: text, document, code  
- Tasks: evaluation/rating, HITL validation, red-teaming, prompt design, RAG groundedness  
- Description:

```
Production HITL for a self-service multi-agent hosting platform (React, FastAPI, MCP, PostgreSQL): review agent workflows, tool calls, and human-approval gates. Built an SRE triaging agent (FastAPI + LangGraph) that correlates OpenSearch logs, git diffs, Jira, and Kubernetes change windows into evidence-backed RCAs — I score traces for completeness, citation quality, and unsafe actions. Designed MCP Agent Companion flows for feature planning, tests, and code review; evaluated LLM patches for correctness across Java, Python, and TypeScript stacks.
```

### Row 2 — Hugging Face + custom Python (M.Tech LLM / GenAI)

- Platform: Hugging Face / Jupyter / custom JSONL pipelines  
- Dates: 2025 – 2026  
- Data types: text, document, medical  
- Tasks: SFT, fine-tuning, evaluation, prompt design, classification  
- Description:

```
Built a medical instruction dataset from a PDF corpus and QLoRA-tuned GPT-2 Medium (PEFT, 4-bit NF4). Wrote and QA’d instruction–response pairs (summarization, topic extraction, grounded answers). Reused the adapter as a prompting system: zero/few-shot, instruction, self-critique, JSON function-calling, CoT/ToT/self-consistency/ReAct, plus a router that picks a strategy per query. Evaluated answers for domain fidelity, format validity, and critique quality.
```

### Row 3 — Custom NLP annotation (M.Tech NLP)

- Platform: Custom Python (NLTK, scikit-learn, regex/gazetteer)  
- Dates: 2025 – 2026  
- Data types: text  
- Tasks: NER, classification, sentiment, dialogue annotation  
- Description:

```
Annotated and modeled: POS + NER on Boston Airbnb reviews; restaurant-review sentiment using dependency-parse negation and intensifiers; a five-document medical QA KB (diabetes, hypertension, COVID-19, asthma, appendicitis) with retrieval, Flan-T5 generation, BART intent, and an agentic verify-and-correct loop; a university-helpdesk dialogue corpus (12 intents, 80+ utterances, slot filling, multi-turn state, safety/escalation). Created gold intents, entities, and conversation-quality scores.
```

### Row 4 — Hugging Face Inference + Gradio (cloud-native ML)

- Platform: Hugging Face Inference API / Gradio / MLflow  
- Dates: 2025 – 2026  
- Data types: text, image, document  
- Tasks: classification, sentiment, evaluation, image caption/defect review  
- Description:

```
SupportSense customer-support triage: DistilBERT + LoRA on Banking77 for intent, plus sentiment, summarization, FAQ QA, image defect/caption, and draft-reply generation. Human-review UI in Gradio; LLMOps metrics in MLflow. Separate telco-churn project: labeled churn outcomes on 7,043 Kaggle records, tracked Logistic Regression vs Random Forest in MLflow, Streamlit dashboard for error review.
```

### Row 5 — Computer vision (M.Tech DNN)

- Platform: Custom Python / Keras-style CNN notebooks  
- Dates: 2025 – 2026  
- Data types: image  
- Tasks: image classification  
- Description:

```
Trained and error-analyzed a CNN on Cats vs Dogs. Compared from-scratch logistic regression vs ReLU MLP on Breast Cancer Wisconsin diagnostics (accuracy, precision, recall, F1). Comfortable with image-level class labels, confusion-matrix QA, and medical tabular classification — not claiming polygon or LiDAR annotation.
```

## Work history blurbs (if the parser truncates)

### Verizon — Distinguished Engineer, Software Development (Sep 2025 – Present)

```
Lead enterprise GenAI/agentic roadmap. Launched Agentic Universe (React, FastAPI, MCP, PostgreSQL) with visual builders and HITL validation. Built LangGraph SRE triaging with evidence-backed RCAs. Architecture-board member for B2B “View Together”. Drove Claude Code / Copilot adoption and MCP Agent Companion for planning, testing, and code review.
```

### Verizon — Principal Engineer / Solutions Architect (Jan 2021 – Sep 2025)

```
Principal architect for B2B SMB & NSE ordering migration: Spring Reactive, GraphQL, Cassandra. Delivered SMB Enrollment and Add-A-Line (case management, OCR ScanID, adaptive auth, credit checks, PEGA). Bulk order engine 10,000+ orders/payload (RabbitMQ, Netflix OSS). 99.99% uptime with New Relic and dropout tracking.
```

Keep Senior Technical Architect, Lead Developer, Tech Mahindra, and Wipro as on the general resume.