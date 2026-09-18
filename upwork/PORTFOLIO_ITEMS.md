# Upwork portfolio items (publish these six)

Limits from Upwork Help: **title 70**, **role 100**, **description 600**, **5 skill tags**.
No email, phone, or LinkedIn in any field or screenshot.

Add cards in this order (best first in the grid).

## 1. Multi-agent HITL platform (LangGraph, MCP)

| Field | Limit | Count |
|---|---:|---:|
| Title | 70 | 42 |
| Role | 100 | 61 |
| Description | 600 | 551 |
| Skills | 5 | 5 |

**Title**

```
Multi-agent HITL platform (LangGraph, MCP)
```

**Role**

```
Principal architect and engineer — Agentic Universe (Verizon)
```

**Skills & deliverables** (exactly five)

Python, FastAPI, LangChain, PostgreSQL, Generative AI

**Project description**

```
Designed and launched a self-service multi-agent hosting platform: React builders, FastAPI runtime, MCP tool servers, PostgreSQL, and human-in-the-loop approval before side effects. Reviewers score traces for tool choice, argument validity, loop termination, and unsafe actions. Companion MCP agents draft feature plans, tests, and code reviews across Java, Python, and TypeScript. Same patterns I use on client LangGraph projects: typed tool contracts, audit logs, and a kill switch. Public resume-level description only; internals stay confidential.
```

**Link:** Text-only card. Do not attach internal screenshots or customer data.

**Media:** Optional: public architecture sketch you draw yourself (boxes: React UI, FastAPI, MCP tools, Postgres, HITL queue). No Verizon logos or PII.

---

## 2. LangGraph SRE agent: logs, git, Jira, K8s

| Field | Limit | Count |
|---|---:|---:|
| Title | 70 | 41 |
| Role | 100 | 49 |
| Description | 600 | 483 |
| Skills | 5 | 5 |

**Title**

```
LangGraph SRE agent: logs, git, Jira, K8s
```

**Role**

```
Tech lead — intelligent incident triage (Verizon)
```

**Skills & deliverables** (exactly five)

Python, LangChain, Kubernetes, Prompt Engineering, REST API

**Project description**

```
Built a FastAPI + LangGraph service that auto-correlates OpenSearch logs, git diffs, Jira issues, and Kubernetes change windows into evidence-backed RCAs. The graph retrieves context, drafts a timeline, cites sources, and stops for a human when confidence is low or a mutating action is proposed. Reduced manual triage by giving on-call a cited first draft instead of a blank page. Hire this pattern for ops copilots, ticket routers, or any agent that must not hallucinate citations.
```

**Link:** Text-only. No production logs in screenshots.

**Media:** Optional diagram: OpenSearch + git + Jira + change windows → LangGraph → RCA draft → human approve.

---

## 3. Medical QLoRA SFT + prompt-strategy router

| Field | Limit | Count |
|---|---:|---:|
| Title | 70 | 42 |
| Role | 100 | 49 |
| Description | 600 | 516 |
| Skills | 5 | 5 |

**Title**

```
Medical QLoRA SFT + prompt-strategy router
```

**Role**

```
ML engineer — BITS M.Tech LLM / GenAI (Group 101)
```

**Skills & deliverables** (exactly five)

Python, Machine Learning, Prompt Engineering, PyTorch, Hugging Face

**Project description**

```
Built a medical instruction dataset from a PDF corpus and QLoRA-tuned GPT-2 Medium (4-bit NF4, LoRA r=16, alpha=32) with Hugging Face PEFT. Reused the adapter as a prompting system with one eval contract: zero/few-shot, self-critique, JSON function-calling, CoT, tree-of-thought, self-consistency, ReAct, and a router that picks a strategy per query. Scored a shared medical query set for groundedness, JSON validity, tokens, and latency. Use this when you need domain SFT plus an eval harness, not a one-off prompt.
```

**Link:** https://github.com/arunkumar4189/AI-ML-Projects/tree/main/LLM-Gen-AI

**Media:** Export training-loss chart and the Part A comparison table from the assignment notebooks (HTML already in repo).

---

## 4. Grounded medical QA with verify-correct loop

| Field | Limit | Count |
|---|---:|---:|
| Title | 70 | 44 |
| Role | 100 | 45 |
| Description | 600 | 450 |
| Skills | 5 | 5 |

**Title**

```
Grounded medical QA with verify-correct loop
```

**Role**

```
NLP engineer — domain QA system (BITS M.Tech)
```

**Skills & deliverables** (exactly five)

Natural Language Processing, Machine Learning, Python, Generative AI, Prompt Engineering

**Project description**

```
Knowledge base of five clinical documents (diabetes, hypertension, COVID-19, asthma, appendicitis). Pipeline: retrieve passages, classify intent (BART), generate with Flan-T5, then an agentic verify-and-correct loop that rewrites answers which drift from source. Built for grounded, explainable clinical Q&A rather than open-ended chat. Same recipe as production RAG: citations, hallucination flags, and a second pass before the user sees the answer.
```

**Link:** https://github.com/arunkumar4189/AI-ML-Projects/blob/main/NLP/Domain-Specific%20Question%20Answering%20System.ipynb

**Media:** Screenshot of a sample Q&A with retrieved snippet and corrected answer (public course text only).

---

## 5. Task-oriented helpdesk: 12 intents, NER, DST

| Field | Limit | Count |
|---|---:|---:|
| Title | 70 | 44 |
| Role | 100 | 57 |
| Description | 600 | 522 |
| Skills | 5 | 5 |

**Title**

```
Task-oriented helpdesk: 12 intents, NER, DST
```

**Role**

```
NLP engineer — conversational AI assignment (BITS M.Tech)
```

**Skills & deliverables** (exactly five)

Natural Language Processing, Machine Learning, Python, Data Science, REST API

**Project description**

```
University helpdesk assistant: 12 intents, 80+ labelled utterances, slot filling, regex/gazetteer NER, multi-turn dialogue state, simulated APIs, and safety/escalation for out-of-scope turns. Intent model is TF-IDF + logistic regression with a full classification report. Gold data was created for the domain (not a generic ATIS dump) so the bot understands courses, fees, exams, hostel, library, and scholarships. Template for any task-oriented bot: invent gold, train intent, track slots, call tools, refuse unsafe asks.
```

**Link:** https://github.com/arunkumar4189/AI-ML-Projects/blob/main/NLP/Conversational%20AI%20and%20Sentiment.ipynb

**Media:** Confusion matrix and a multi-turn dialogue-state table from the notebook.

---

## 6. SupportSense: LoRA intent, QA, Gradio, MLflow

| Field | Limit | Count |
|---|---:|---:|
| Title | 70 | 45 |
| Role | 100 | 49 |
| Description | 600 | 486 |
| Skills | 5 | 5 |

**Title**

```
SupportSense: LoRA intent, QA, Gradio, MLflow
```

**Role**

```
ML / LLMOps engineer — cloud-native ML coursework
```

**Skills & deliverables** (exactly five)

Python, Machine Learning, Docker, REST API, Generative AI

**Project description**

```
Customer-support triage combining NLP and vision: Banking77 intent (DistilBERT + LoRA), sentiment, summarization, FAQ QA, image defect/caption, and a draft reply. Hugging Face Inference API, Gradio review UI, LLMOps metrics. Sister project: telco churn on 7,043 Kaggle rows with Logistic Regression vs Random Forest in MLflow and a Streamlit dashboard. Shows a full path from labeled data → tracked model → human review UI, which is what most Upwork 'chatbot' jobs are actually missing.
```

**Link:** https://github.com/arunkumar4189/AI-ML-Projects/tree/main/API%20Driven%20Cloud%20Native

**Media:** Gradio UI screenshot (local/demo) and MLflow run table if you still have it; otherwise the course report PDF without personal emails.

---

## Optional extras (only if a client asks for CV / RL)

Keep these off the main grid so the profile stays on-agent/RAG/NLP:

- CNN cats-vs-dogs + from-scratch MLP (`DNN/`)
- Seq2Seq Transformer summarization (`Conversational AI/Sequence-to-Sequence Transformer.ipynb`)
- CLIP knowledge distillation on Flickr30k (`Conversational AI/Knowledge Distillation.ipynb`)

If you add one extra, prefer the **CLIP distillation** card for multimodal jobs.
