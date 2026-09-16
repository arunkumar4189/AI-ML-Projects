# Portfolio projects (GitHub evidence)

Source repo: [arunkumar4189/AI-ML-Projects](https://github.com/arunkumar4189/AI-ML-Projects)

Each block is written so you can paste it into an OpenTrain proposal, a job questionnaire (“describe relevant experience”), or a public profile note. Paths are relative to the repo root.

---

## 1. Medical LLM adaptation and prompting system

**OpenTrain tags:** SFT / fine-tuning, instruction data, evaluation, medical text  
**Folder:** `LLM-Gen-AI/`

Collected clinical PDFs, built an instruction JSONL, QLoRA-fine-tuned GPT-2 Medium, then treated prompting as system design: zero/few-shot, instruction, self-critique, JSON function-calling, CoT/ToT/self-consistency/ReAct, and a classifier→router that picks a pattern per query. Tracked tokens, latency, and quality under greedy decoding.

**Why it maps to AI training jobs:** writing instruction pairs, judging model outputs, schema-constrained extraction, and routing policies are the same muscles as SFT data work and LLM eval.

---

## 2. Medical QA with agentic verification

**OpenTrain tags:** RAG groundedness, evaluation/rating, medical documents  
**Folder:** `NLP/Domain-Specific Question Answering System.ipynb`

Five guideline-style documents (diabetes, hypertension, COVID-19, asthma, appendicitis). Retrieves chunks, generates with Flan-T5, classifies intent with BART, then runs an agentic verify-and-correct loop so answers stay cited and explainable.

**Why it maps:** factuality/groundedness review and “reject or revise ungrounded answers” is core LLM evaluation work.

---

## 3. University helpdesk conversational AI

**OpenTrain tags:** intent classification, NER/slots, dialogue evaluation  
**Folder:** `NLP/Conversational AI and Sentiment.ipynb`

Task-oriented helpdesk: 12 intents, 15 entities, TF-IDF + logistic regression, regex/gazetteer extraction, dialogue-state tracking, eight simulated tools, and safety/escalation for out-of-scope or sensitive turns.

**Why it maps:** intent/entity guidelines, multi-turn consistency, and “should we escalate?” judgments.

---

## 4. Linguistic annotation (POS, sentiment, news IR)

**OpenTrain tags:** NER/POS, sentiment, text classification, documents  
**Folders:** `NLP/POS Tagging.ipynb`, `NLP/Sentiment Analys.ipynb`, `IR/`

- Boston Airbnb reviews: cleaning, POS, HMM tagging, NER overlay  
- Restaurant reviews: dependency trees for **negation** and **intensifiers**  
- Newsroom tagging: from-scratch TF-IDF, Naïve Bayes, Rocchio on mixed PDF/DOCX/CSV/TXT  
- Clinical search: inverted index plus k-gram/Levenshtein and Soundex spelling correction

**Why it maps:** guideline-driven linguistic labels and noisy real-world documents.

---

## 5. SupportSense — multimodal support triage

**OpenTrain tags:** classification, sentiment, image caption/defect, customer support  
**Folder:** `API Driven Cloud Native/` (Assignment II)

Orchestrated complaint classification (DistilBERT + LoRA on Banking77), sentiment, summarization, FAQ QA, image defect checks, captions, and empathetic draft replies. Hugging Face APIs + Gradio UI + correlation IDs and quality metrics.

**Why it maps:** ticket labeling, tone/priority, and multimodal review in a single workflow.

---

## 6. Telco churn MLOps

**OpenTrain tags:** classification, telecom, evaluation dashboards  
**Folder:** `API Driven Cloud Native/` (Assignment I)

IBM/Kaggle Telco churn (7,043 customers). DataOps pipeline, Logistic Regression vs Random Forest, MLflow tracking, Streamlit dashboard. Role on the team: API access module and dashboard integration.

**Why it maps:** scoring/review of model outputs and experiment comparison.

---

## 7. Vision-language distillation and CNN classification

**OpenTrain tags:** image, evaluation, retrieval  
**Folders:** `Conversational AI/Knowledge Distillation.ipynb`, `DNN/CNN.ipynb`

CLIP teacher → compact dual-encoder student on Flickr30k; Recall@1/5/10 with vs without KD. Separate CNN cats-vs-dogs classifier.

**Why it maps:** image–text alignment review and retrieval metrics (not bounding-box annotation).

---

## 8. Abstractive summarization Transformer

**OpenTrain tags:** text, evaluation (ROUGE), SFT-style training  
**Folder:** `Conversational AI/Sequence-to-Sequence Transformer.ipynb`

Seq2Seq Transformer from scratch on CNN/DailyMail; BPE, masks, teacher forcing, greedy decode, ROUGE.

**Why it maps:** summary quality rating and preference-style comparison of generations.

---

## 9. Software defect prediction

**OpenTrain tags:** code, classification  
**Folder:** `ML/RandomForestClassifier.ipynb`

Apache Ant 1.3 metrics → bug/no-bug with Logistic Regression, Decision Tree, Random Forest; correlation-aware feature selection.

**Why it maps:** code-quality labeling and binary defect guidelines.

---

## 10. Reinforcement learning evaluations

**OpenTrain tags:** evaluation, ranking policies  
**Folder:** `DRL/`

MiniChess DP (value/policy iteration), multi-armed bandits for product recs (ε-greedy vs UCB), Q-learning/DQN/DDQN on discretized HalfCheetah.

**Why it maps:** comparing policies with plots and regret/reward — similar to ranking model variants.

---

## Proposal one-liner (reuse)

> I am a Distinguished Engineer (Verizon) and BITS Pilani M.Tech AI & ML candidate. My public coursework repo implements medical SFT/QLoRA, RAG verification, intent/NER dialogue systems, sentiment and IR labeling, multimodal support triage, and model-evaluation harnesses. I can write guidelines, produce or judge labels, and evaluate LLM/NLP outputs with documented metrics: https://github.com/arunkumar4189/AI-ML-Projects
