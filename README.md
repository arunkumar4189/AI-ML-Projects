# AI-ML-Projects

Portfolio of M.Tech **Artificial Intelligence and Machine Learning** coursework (BITS). Notebooks, reports, and supporting artefacts are grouped by course.

Contributor on these submissions: **Arunkumar K A** (`2024AC05045`), typically with Groups 11, 15, 101, or 103.

**OpenTrain AI:** copy-paste profile fields, labeling-experience entries, and an AI-training resume are in [`opentrain/`](opentrain/).

## Repository layout

| Folder | Course focus |
|---|---|
| [ML](ML/) | Classical machine learning |
| [DNN](DNN/) | Deep neural networks |
| [NLP](NLP/) | Natural language processing applications |
| [IR](IR/) | Information retrieval |
| [Conversational AI](Conversational%20AI/) | Seq2Seq transformers and vision–language distillation |
| [LLM-Gen-AI](LLM-Gen-AI/) | Domain LLMs, QLoRA, and prompting systems |
| [DRL](DRL/) | Deep reinforcement learning |
| [API Driven Cloud Native](API%20Driven%20Cloud%20Native/) | Cloud-native ML/LLM applications |

---

## Machine Learning (`ML/`)

**Software defect prediction (Apache Ant 1.3)**  
Binary classification of defective vs clean modules using 20 software metrics (`wmc`, `cbo`, `loc`, and related CK/QMOOD features). The notebook covers EDA, correlation and multicollinearity, then trains **Logistic Regression**, **Decision Tree**, and **Random Forest**, with feature importance and confusion matrices.

- Notebook: `RandomForestClassifier.ipynb`

## Deep Neural Networks (`DNN/`)

**Linear model vs multi-layer perceptron (from scratch)**  
Breast Cancer Wisconsin (Diagnostic). Logistic regression and a ReLU MLP are implemented with gradient descent (no sklearn estimators) and compared on accuracy, precision, recall, F1, and training time.

**CNN for Cats vs Dogs**  
Convolutional image classification on the cats-vs-dogs dataset.

- Notebooks: `Comparing Linear Models and Multi-Layer.ipynb`, `CNN.ipynb`

## Natural Language Processing (`NLP/`)

**POS tagging on Boston Airbnb reviews**  
Cleaning, stemming/lemmatization, NLTK POS tags, HMM tagging, visualizations, and POS + NER analysis.

**Sentiment analysis via dependency parsing**  
Restaurant reviews. Syntactic trees supply **negation** and **intensifier–adjective** features for polarity.

**Domain-specific medical QA**  
Knowledge base of five clinical documents (diabetes, hypertension, COVID-19, asthma, appendicitis). Retrieval, Flan-T5 generation, BART intent classification, and an agentic verify-and-correct loop for grounded, explainable answers.

**University helpdesk conversational AI**  
Task-oriented assistant: 12 intents, slot filling, multi-turn dialogue state, TF-IDF + logistic regression, regex/gazetteer NER, simulated APIs, and safety/escalation.

- Notebooks: `POS Tagging.ipynb`, `Sentiment Analys.ipynb`, `Domain-Specific Question Answering System.ipynb`, `Conversational AI and Sentiment.ipynb`

## Information Retrieval (`IR/`)

**Newsroom article tagging**  
Naïve Bayes and Rocchio from scratch, plus manual TF-IDF, on mixed-format news (PDF, DOCX, CSV, TXT) for Sports / Politics / Technology.

**Medical search and isolated spelling correction**  
Non-positional inverted index on clinical text, then k-gram Jaccard + Levenshtein and Soundex for spelling correction.

- Notebooks: `Classifier Implementation.ipynb`, `Preprocess healthcare-related documents.ipynb`

## Conversational AI (`Conversational AI/`)

**Seq2Seq Transformer for abstractive summarization**  
Encoder–decoder Transformer built from scratch on CNN/DailyMail: cleaning, BPE, causal/padding masks, teacher forcing, greedy decode, and ROUGE.

**Knowledge distillation for edge-ready VLMs**  
Frozen CLIP (ViT-B/32) teacher distills into a compact dual-encoder student on Flickr30k (MSE/cosine + InfoNCE). Evaluation compares teacher, student without KD, and student with KD using Recall@K and deployment metrics.

- Notebooks: `Sequence-to-Sequence Transformer.ipynb`, `Knowledge Distillation.ipynb`

## LLM / Generative AI (`LLM-Gen-AI/`)

**Assignment 1B — medical domain adaptation**  
Medical PDF corpus, instruction-dataset construction, **QLoRA** fine-tuning of GPT-2 Medium, plus inference optimization and production cost analysis (GPT-2 as draft model).

**Assignment 2A — prompting as system design**  
The 1B adapter is reused for zero-shot, few-shot, instruction, self-critique, JSON function-calling, CoT / ToT / self-consistency / ReAct, and a prompt router that selects a strategy per query.

- Notebooks: `Group_101_Assignment_1B_Medical.ipynb`, `Group_101_Assignment_2A_Medical.ipynb`
- Data: `instruction_dataset.jsonl`

## Deep Reinforcement Learning (`DRL/`)

**MiniChess with dynamic programming**  
Custom 4×4 MiniChess MDP (White king + pawn vs Black king). Value iteration and policy iteration, state-value heatmaps, and a discussion of the curse of dimensionality.

**Multi-armed bandits for product recommendation**  
498 users × 6 products. Net reward, random / greedy / ε-greedy / UCB policies, and cumulative-profit comparison.

**Q-learning, DQN, and DDQN**  
Gymnasium HalfCheetah-v4 with discretized continuous actions; tabular and deep Q-learning variants are compared.

- Reports: `DP_MiniChess_Solution.pdf`, `MAB_Product_Recommendation_Solution.pdf`, `Q-learning, DQN, and DDQN Methods.pdf`

## API-driven Cloud Native (`API Driven Cloud Native/`)

**Assignment I — telco churn**  
Kaggle Telco Customer Churn (7,043 records). DataOps ingestion/preprocessing, Logistic Regression + Random Forest with MLflow tracking, and a Streamlit dashboard. API access uses the MLflow REST API.

**Assignment II — SupportSense**  
Customer-support triage combining NLP and computer vision: classify, sentiment, summarize, FAQ QA, image defect/caption, and draft reply. DistilBERT + LoRA on Banking77, Hugging Face Inference API, Gradio UI, and LLMOps logging/metrics.

- Reports: `Group_11.pdf`, `Group_11_Assignment_2.docx` / PDF

---

## Notes

These artefacts are course submissions (notebooks, HTML exports, PDFs/DOCX). They are not packaged as a single runnable application. Open a notebook or report in its folder for dataset links, libraries, and run instructions for that assignment.
