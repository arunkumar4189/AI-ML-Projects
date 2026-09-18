#!/usr/bin/env python3
"""Generate the OpenTrain data-labeling resume PDF from structured sections."""

from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).with_name("Arun_Kumar_OpenTrain_Data_Labeling_Resume.pdf")


class ResumePDF(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 8, f"OpenTrain data-labeling resume  |  page {self.page_no()}", align="C")


def h1(pdf: ResumePDF, text: str):
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(20, 20, 20)
    pdf.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")


def h2(pdf: ResumePDF, text: str):
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(25, 70, 120)
    pdf.cell(0, 7, text.upper(), new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(25, 70, 120)
    pdf.set_line_width(0.3)
    y = pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
    pdf.ln(2)
    pdf.set_text_color(30, 30, 30)


def body(pdf: ResumePDF, text: str):
    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


def bullet(pdf: ResumePDF, text: str):
    pdf.set_font("Helvetica", size=10)
    pdf.set_x(pdf.l_margin)
    pdf.cell(5, 5, "-")
    pdf.multi_cell(0, 5, text, new_x="LMARGIN", new_y="NEXT")


def job_head(pdf: ResumePDF, title: str, meta: str):
    pdf.set_font("Helvetica", "B", 10)
    pdf.multi_cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(70, 70, 70)
    pdf.multi_cell(0, 5, meta, new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(30, 30, 30)


def main():
    pdf = ResumePDF(format="Letter")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.add_page()
    pdf.set_margins(16, 14, 16)

    h1(pdf, "Arun Kumar Kumari Arumugam")
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(25, 70, 120)
    pdf.multi_cell(
        0,
        6,
        "AI Trainer  |  LLM Evaluation  |  Medical SFT & NLP Annotation  |  Agentic HITL",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.set_font("Helvetica", size=9)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        5,
        "Chennai, India  |  +91 95669 16623  |  arunkumar4189@gmail.com  |  linkedin.com/in/arunkumar",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.multi_cell(
        0,
        5,
        "OpenTrain: app.opentrain.ai/labeler-profile/arun-k-35  |  GitHub: github.com/arunkumar4189/AI-ML-Projects",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.set_text_color(30, 30, 30)

    h2(pdf, "Profile")
    body(
        pdf,
        "Distinguished Engineer at Verizon (15+ years building distributed platforms) and M.Tech AI/ML "
        "candidate at BITS Pilani (2024AC05045). I create instruction data, score LLM and agent outputs "
        "against rubrics, annotate medical and dialogue text, and run human-in-the-loop gates on production "
        "multi-agent systems. Best fit: LLM evaluation, SFT/preference data, medical or telco NLP, code-aware "
        "review, and agent-trace QA -- not high-volume bounding-box piecework.",
    )

    h2(pdf, "AI training and annotation")
    job_head(
        pdf,
        "Verizon -- GenAI / agentic HITL and LLM evaluation",
        "Chennai  |  2024 -- Present  |  Internal tooling  |  text, code, documents  |  eval, HITL, prompts, safety",
    )
    for line in [
        "HITL validation for Agentic Universe (React, FastAPI, MCP, PostgreSQL): workflow review, tool-call checks, approval gates.",
        "Scored LangGraph SRE triage traces that cite OpenSearch logs, git diffs, Jira issues, and Kubernetes change windows.",
        "Evaluated MCP Agent Companion outputs for planning, tests, and code review across Java, Python, and TypeScript.",
        "Rubrics: factuality, groundedness/citations, instruction-following, and unsafe or unapproved actions.",
    ]:
        bullet(pdf, line)

    pdf.ln(1)
    job_head(
        pdf,
        "BITS Pilani M.Tech -- LLM / Generative AI (Group 101)",
        "2025 -- 2026  |  Hugging Face, PEFT QLoRA, JSONL  |  medical documents  |  SFT, fine-tuning, prompt eval",
    )
    for line in [
        "Built medical instruction-response pairs from a PDF corpus; QLoRA-tuned GPT-2 Medium (4-bit NF4, r=16, alpha=32).",
        "Prompting system with a shared eval harness: zero/few-shot, self-critique, JSON function-calling, CoT/ToT/self-consistency/ReAct, and a strategy router.",
        "Scored answers for domain fidelity, JSON schema validity, token/latency cost, and critique quality.",
    ]:
        bullet(pdf, line)

    pdf.ln(1)
    job_head(
        pdf,
        "BITS Pilani M.Tech -- NLP, IR, conversational AI",
        "2025 -- 2026  |  NLTK, scikit-learn, Hugging Face  |  text, documents  |  NER, classification, QA, dialogue",
    )
    for line in [
        "Medical QA over five clinical sources (diabetes, hypertension, COVID-19, asthma, appendicitis) with retrieval, Flan-T5, BART intent, and a verify-and-correct loop.",
        "University-helpdesk gold set: 12 intents, 80+ utterances, slot/NER gazetteers, multi-turn state, safety escalation.",
        "POS + NER on Airbnb reviews; restaurant sentiment with syntactic negation; news taxonomy (Naive Bayes/Rocchio); clinical IR and spelling correction.",
    ]:
        bullet(pdf, line)

    pdf.ln(1)
    job_head(
        pdf,
        "BITS Pilani M.Tech -- CV, classical ML, RL, LLMOps",
        "2025 -- 2026  |  CNN/MLP, MLflow, Gradio, DistilBERT+LoRA  |  image, text, tabular",
    )
    for line in [
        "Image-level classification (cats vs dogs); Breast Cancer Wisconsin diagnostics; Apache Ant software-defect labels.",
        "SupportSense: Banking77 intent plus sentiment, summary, FAQ QA, image caption/defect, draft reply; telco churn (7,043 rows) reviewed in MLflow/Streamlit.",
        "Bandit and Q-learning policy comparison for preference/reward analysis (coursework, not a vendor RLHF contract).",
    ]:
        bullet(pdf, line)

    h2(pdf, "Professional background (domain context)")
    job_head(pdf, "Verizon -- Distinguished Engineer, Software Development", "Chennai  |  Sep 2025 -- Present")
    body(
        pdf,
        "GenAI and agentic roadmap; launched Agentic Universe; architecture board for B2B View Together; "
        "org-wide Claude Code / Copilot and MCP agent suite.",
    )
    job_head(pdf, "Verizon -- Principal Engineer / Solutions Architect", "Jan 2021 -- Sep 2025")
    body(
        pdf,
        "B2B SMB & NSE ordering (Spring Reactive, GraphQL, Cassandra); SMB Enrollment and Add-A-Line "
        "(OCR ScanID, PEGA); bulk engine 10,000+ orders per payload; 99.99% uptime with New Relic.",
    )
    job_head(pdf, "Earlier roles", "Verizon Lead/Architect 2016--2021; Tech Mahindra 2014--2016; Wipro 2010--2013")
    body(
        pdf,
        "Event-driven REST, Quote-to-Order automation, Oracle ATG commerce, WebLogic, catalog and order repositories.",
    )

    h2(pdf, "Matching skills")
    body(
        pdf,
        "Data: text, documents, code, images, medical.  Tasks: LLM eval/rating, SFT, LoRA/QLoRA, NER, "
        "intent/slots, QA/RAG groundedness, sentiment, classification, prompt/red-team, HITL agent traces, "
        "image-level labels.  Tools: Hugging Face, PEFT, LangGraph, MCP, FastAPI, MLflow, Gradio, Streamlit, "
        "NLTK, scikit-learn, OpenSearch, Jupyter.  Code: Python, Java, TypeScript, JavaScript, SQL.  "
        "Human language: English (fluent).",
    )

    h2(pdf, "Education")
    bullet(pdf, "M.Tech, Artificial Intelligence & Machine Learning -- BITS Pilani -- 2025-2027 (expected) -- ID 2024AC05045")
    bullet(pdf, "B.E., Computer Science & Engineering -- Anna University, Chennai -- 2010 -- 77.06%")

    pdf.output(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
