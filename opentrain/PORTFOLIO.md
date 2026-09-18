# OpenTrain project portfolio

Use these as labeling-experience write-ups, proposal attachments, or “completed work” log entries. Each item is implemented in this GitHub repo unless marked **production (Verizon)**.

Contributor on BITS submissions: **Arunkumar K A** (`2024AC05045`).

---

## 1. Production HITL and LLM evaluation — Agentic Universe & SRE triage

**Source:** resume (Verizon, 2024–present)  
**OpenTrain tags:** text, code, document · evaluation, HITL, red-teaming, prompt design  
**Tools:** internal platform, FastAPI, LangGraph, MCP, React, PostgreSQL, OpenSearch, Kubernetes

What a reviewer can hire this for:

- Score multi-agent traces: tool selection, argument validity, loop/termination, human-gate compliance
- Groundedness review of RCAs that cite logs, git, Jira, and change windows
- Code-aware LLM review (Java, Python, TypeScript) for planning, tests, and diffs
- Safety: refuse or escalate actions that would mutate production without approval

Evidence of judgment, not just labeling speed: enterprise architecture board, 99.99% uptime systems, B2B ordering domain.

---

## 2. Medical SFT dataset + QLoRA domain adaptation

**Source:** `LLM-Gen-AI/Group_101_Assignment_1B_Medical.ipynb`, `instruction_dataset.jsonl`  
**Tags:** medical, document, text · SFT, fine-tuning, evaluation  
**Tools:** Hugging Face Transformers, PEFT QLoRA, bitsandbytes 4-bit NF4, GPT-2 Medium

Work performed:

- Parsed a medical PDF corpus into instruction–response pairs
- Justified dataset size vs adapter capacity (`r=16`, `alpha=32`, dropout `0.05`, `max_seq_length=512`)
- Trained Adapter B and compared quality/latency/cost vs untuned GPT-2 Medium
- Documented production serving options (4-bit vs bf16 speculative decoding)

Trainer-relevant skills: writing SFT gold, rejecting noisy PDF extractions, scoring domain language vs generic completion.

---

## 3. Prompting as system design (eval harness)

**Source:** `LLM-Gen-AI/Group_101_Assignment_2A_Medical.ipynb`  
**Tags:** text, medical · prompt design, evaluation, JSON tool-calling, red-teaming  
**Tools:** same QLoRA adapter; greedy decode, `max_new_tokens=200`

Implemented a uniform `(query) -> (answer, tokens, latency)` contract for:

- Zero-shot / few-shot / instruction  
- Self-critique  
- JSON function-calling  
- Chain-of-thought, tree-of-thought, self-consistency  
- ReAct  
- A **prompt router** that selects a strategy per query  

Evaluated a shared 10-query medical set for format validity, groundedness, and critique quality. Direct analog to RLHF/SFT vendor tasks: rubric scoring, strategy comparison, and catching overconfident medical answers.

---

## 4. Grounded medical QA with verify-and-correct loop

**Source:** `NLP/Domain-Specific Question Answering System.ipynb`  
**Tags:** medical, document · QA, evaluation, classification  
**Tools:** retrieval over 5 clinical docs, Flan-T5, BART intent, agentic correction loop

Diseases covered: diabetes, hypertension, COVID-19, asthma, appendicitis.

Trainer-relevant skills: citation checking, hallucination flags, intent labels on clinical questions, rewriting answers that drift from source text.

---

## 5. Task-oriented dialogue annotation (university helpdesk)

**Source:** `NLP/Conversational AI and Sentiment.ipynb`  
**Tags:** text · intent classification, NER/slots, dialogue state, safety  
**Tools:** scikit-learn TF-IDF + logistic regression, regex/gazetteer NER, simulated APIs

Gold data created:

- 12 intents, 80+ labelled utterances  
- 10+ multi-turn conversations with dialogue-state tracking  
- ≥10 entity types (courses, fees, exams, hostel, library, scholarships, faculty, …)  
- Safety/escalation policies for ambiguous or out-of-scope turns  

Evaluation: classification report, confusion matrix, conversation-quality scores.

---

## 6. Linguistic annotation — POS, NER, sentiment

**Sources:** `NLP/POS Tagging.ipynb`, `NLP/Sentiment Analys.ipynb`  
**Tags:** text · NER, classification, sentiment  
**Tools:** NLTK (POS, HMM tagger, NER), stemming/lemmatization, dependency features

- Boston Airbnb reviews: cleaning, POS, HMM tagging, POS+NER dual analysis  
- Restaurant reviews: polarity from **negation** and **intensifier–adjective** dependency patterns  

Shows guideline-level linguistic care (scope of negation, entity type vs POS).

---

## 7. Document classification and medical IR

**Sources:** `IR/Classifier Implementation.ipynb`, `IR/Preprocess healthcare-related documents.ipynb`  
**Tags:** document, medical, text · classification  
**Tools:** from-scratch Naïve Bayes, Rocchio, manual TF-IDF; inverted index; k-gram Jaccard, Levenshtein, Soundex

- Mixed-format news (PDF, DOCX, CSV, TXT) tagged Sports / Politics / Technology  
- Clinical search plus isolated spelling correction  

Trainer analog: taxonomy tagging, OCR/noisy-document QA, medical query rewriting.

---

## 8. SupportSense + telco churn (LLMOps / human review)

**Source:** `API Driven Cloud Native/` course reports (see repo README)  
**Tags:** text, image, document · classification, sentiment, evaluation  
**Tools:** DistilBERT+LoRA (Banking77), Hugging Face Inference API, Gradio, MLflow, Streamlit

- Multi-task support desk: intent, sentiment, summary, FAQ QA, image defect/caption, draft reply  
- Telco churn on 7,043 records with experiment tracking and dashboard error review  

Domain overlap with Verizon B2B/telco work.

---

## 9. Image and diagnostic classification

**Sources:** `DNN/CNN.ipynb`, `DNN/Comparing Linear Models and Multi-Layer.ipynb`, `ML/RandomForestClassifier.ipynb`  
**Tags:** image, medical · classification  
**Tools:** CNN (cats vs dogs); from-scratch logistic regression + ReLU MLP (Breast Cancer Wisconsin); Random Forest on Apache Ant 1.3 defect metrics

Honest scope: **image-level labels and tabular medical/software metrics**, not instance segmentation or 3D LiDAR.

---

## 10. Preference, reward, and policy evaluation (RL coursework)

**Source:** `DRL/` reports listed in repo README  
**Tags:** text / structured logs · evaluation, RLHF-adjacent  
**Tools:** custom MiniChess MDP; multi-armed bandits; Gymnasium HalfCheetah-v4 Q-learning / DQN / DDQN

- Ranked recommendation policies (random, greedy, ε-greedy, UCB) on 498 users × 6 products by cumulative profit  
- Compared tabular vs deep Q methods and discussed failure modes  

This is **reward-model thinking**, not a claim of shipping Anthropic/OpenAI RLHF pipelines.

---

## 11. Seq2Seq summarization and VLM distillation eval

**Sources:** `Conversational AI/Sequence-to-Sequence Transformer.ipynb`, `Conversational AI/Knowledge Distillation.ipynb`  
**Tags:** text, image · evaluation, summarization  
**Tools:** Transformer from scratch (CNN/DailyMail, BPE, ROUGE); CLIP ViT-B/32 teacher → compact dual-encoder student on Flickr30k (Recall@K)

Trainer analog: summary quality (faithfulness vs fluency) and image–caption alignment rating.

---

## How to talk about this in applications

Lead with **domain + eval rigor**, then link artefacts:

1. Verizon HITL / agent traces (production judgment)  
2. Medical SFT + prompting eval (this repo)  
3. Dialogue/NER gold (this repo)  

Link the GitHub repo and the public profile  
https://app.opentrain.ai/labeler-profile/arun-k-35  
in every proposal.