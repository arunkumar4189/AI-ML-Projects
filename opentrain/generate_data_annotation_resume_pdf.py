#!/usr/bin/env python3
"""Generate PDF resume for DataAnnotation / AI coding contributor applications."""

from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).with_name("Arun_Kumar_DataAnnotation_Resume.pdf")


class ResumePDF(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 8, f"Resume - AI coding & evaluation  |  page {self.page_no()}", align="C")


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
    pdf.set_font("Helvetica", size=9.5)
    pdf.multi_cell(0, 4.5, text, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.5)


def bullet(pdf: ResumePDF, text: str):
    pdf.set_font("Helvetica", size=9.5)
    pdf.set_x(pdf.l_margin)
    pdf.cell(5, 4.5, "-")
    pdf.multi_cell(0, 4.5, text, new_x="LMARGIN", new_y="NEXT")


def job_head(pdf: ResumePDF, title: str, meta: str):
    pdf.set_font("Helvetica", "B", 10)
    pdf.multi_cell(0, 4.5, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(70, 70, 70)
    pdf.multi_cell(0, 4.5, meta, new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(30, 30, 30)


def main():
    pdf = ResumePDF(format="Letter")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()
    pdf.set_margins(14, 12, 14)

    h1(pdf, "Arun Kumar Kumari Arumugam")
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(25, 70, 120)
    pdf.multi_cell(
        0,
        5,
        "Software Engineer  |  AI Model Training & Code Evaluation  |  Python / Java / TypeScript",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.set_font("Helvetica", size=8.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        4.5,
        "Chennai, India  |  +91 95669 16623  |  arunkumar4189@gmail.com",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.multi_cell(
        0,
        4.5,
        "linkedin.com/in/arun-kumar-kumari-arumugam-87178b8b  |  github.com/arunkumar4189/AI-ML-Projects",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.set_text_color(30, 30, 30)

    h2(pdf, "Professional summary")
    body(
        pdf,
        "Distinguished Engineer with 15+ years designing, implementing, and reviewing production code on "
        "high-throughput distributed systems. Fluent English technical writing; proficient in Python, Java, "
        "JavaScript, TypeScript, and SQL. Daily work evaluating AI-generated code and plans (Claude Code, "
        "GitHub Copilot, MCP agents), debugging complex workflows, and explaining trade-offs clearly. "
        "M.Tech AI/ML candidate (BITS Pilani) with hands-on instruction data, QLoRA fine-tuning, prompt "
        "evaluation harnesses, and rubric-based LLM scoring -- aligned with coding tasks, quality snippets, "
        "and reviewing model outputs for correctness, performance, and clarity.",
    )

    h2(pdf, "Core skills")
    body(
        pdf,
        "Programming: Python, Java, TypeScript, JavaScript, SQL; algorithms, data structures, debugging, testing.  "
        "AI training: instruction datasets, SFT/QLoRA, prompt design (CoT, ReAct, JSON tools), rubric scoring.  "
        "Tools: Hugging Face, PEFT, LangGraph, MCP, FastAPI, Spring Boot, NLTK, scikit-learn, Jupyter, MLflow.",
    )

    h2(pdf, "AI-focused engineering & evaluation")
    job_head(
        pdf,
        "Verizon -- Distinguished Engineer, Software Development",
        "Chennai  |  Sep 2025 -- Present",
    )
    for line in [
        "Lead GenAI roadmap; Agentic Universe (React, FastAPI, MCP, PostgreSQL) with human-in-the-loop agent validation.",
        "SRE Triaging Service (FastAPI, LangGraph): review multi-agent RCA outputs citing logs, git, Jira, and K8s context.",
        "Org-wide Claude Code / Copilot and MCP Agent Companion for planning, tests, and code review (Java, Python, TS).",
        "Enterprise architecture board; API security and quality bars for production AI and ordering platforms.",
    ]:
        bullet(pdf, line)

    pdf.ln(1)
    job_head(
        pdf,
        "Verizon -- GenAI evaluation focus",
        "Chennai  |  2024 -- Present",
    )
    for line in [
        "Score agent traces and LLM outputs: groundedness, citations, instruction-following, unsafe actions.",
        "99.99% uptime B2B systems; mentor teams on reactive services, observability, and incident debugging.",
    ]:
        bullet(pdf, line)

    h2(pdf, "M.Tech AI/ML projects (BITS Pilani)")
    pdf.set_font("Helvetica", "I", 8.5)
    pdf.multi_cell(
        0,
        4,
        "Portfolio: github.com/arunkumar4189/AI-ML-Projects  |  ID 2024AC05045",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.set_font("Helvetica", size=9.5)
    pdf.ln(1)

    job_head(pdf, "LLM / Generative AI (Group 101)", "2025 -- 2026")
    for line in [
        "Medical instruction-response JSONL; QLoRA fine-tuned GPT-2 Medium (4-bit NF4, PEFT).",
        "Prompt eval harness: zero/few-shot, self-critique, JSON function-calling, CoT/ToT/ReAct, strategy router.",
    ]:
        bullet(pdf, line)

    job_head(pdf, "NLP, IR, conversational AI", "2025 -- 2026")
    for line in [
        "Medical QA (5 clinical docs): retrieval, Flan-T5, BART intent, verify-and-correct loop.",
        "Dialogue gold: 12 intents, slots/NER, multi-turn state; news/clinical IR and spelling correction.",
    ]:
        bullet(pdf, line)

    job_head(pdf, "ML, deep learning, LLMOps", "2025 -- 2026")
    for line in [
        "SupportSense: DistilBERT+LoRA, sentiment, summary, FAQ QA, image caption/defect (Gradio).",
        "Defect prediction (Random Forest); CNN; Seq2Seq summarization; bandit/Q-learning policy comparison.",
    ]:
        bullet(pdf, line)

    h2(pdf, "Software engineering experience")
    job_head(pdf, "Verizon -- Principal Engineer / Solutions Architect", "Jan 2021 -- Sep 2025")
    body(
        pdf,
        "B2B ordering (Spring Reactive, GraphQL, Cassandra); bulk engine 10,000+ orders/payload; "
        "SMB Enrollment, Add-A-Line, OCR ScanID, PEGA.",
    )
    job_head(pdf, "Verizon -- Senior Architect / Lead Developer", "Jan 2016 -- Jan 2021")
    body(pdf, "Event-driven APIs, Quote-to-Order automation, Cart/Config/Payment microservices, Oracle ATG.")
    job_head(pdf, "Tech Mahindra / Wipro", "2010 -- 2016")
    body(pdf, "WebLogic commerce; ATG e-commerce REST (profile, tax, shipping, promotions).")

    h2(pdf, "Education")
    bullet(pdf, "M.Tech, AI & Machine Learning -- BITS Pilani -- 2025-2027 (expected) -- 2024AC05045")
    bullet(pdf, "B.E., Computer Science -- Anna University, Chennai -- 2010")
    bullet(pdf, "Languages: English (fluent), Tamil")

    pdf.output(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
