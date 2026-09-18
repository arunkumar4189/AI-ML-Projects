#!/usr/bin/env python3
"""Validate Upwork field lengths and regenerate PORTFOLIO_ITEMS.md."""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).with_name("PORTFOLIO_ITEMS.md")

TITLE, ROLE, DESC, SKILLS = 70, 100, 600, 5

ITEMS = [
    {
        "id": 1,
        "title": "Multi-agent HITL platform (LangGraph, MCP)",
        "role": "Principal architect and engineer — Agentic Universe (Verizon)",
        "skills": ["Python", "FastAPI", "LangChain", "PostgreSQL", "Generative AI"],
        "link": "Text-only card. Do not attach internal screenshots or customer data.",
        "media": "Optional: public architecture sketch you draw yourself (boxes: React UI, FastAPI, MCP tools, Postgres, HITL queue). No Verizon logos or PII.",
        "desc": (
            "Designed and launched a self-service multi-agent hosting platform: React builders, "
            "FastAPI runtime, MCP tool servers, PostgreSQL, and human-in-the-loop approval before "
            "side effects. Reviewers score traces for tool choice, argument validity, loop "
            "termination, and unsafe actions. Companion MCP agents draft feature plans, tests, and "
            "code reviews across Java, Python, and TypeScript. Same patterns I use on client LangGraph "
            "projects: typed tool contracts, audit logs, and a kill switch. Public resume-level "
            "description only; internals stay confidential."
        ),
    },
    {
        "id": 2,
        "title": "LangGraph SRE agent: logs, git, Jira, K8s",
        "role": "Tech lead — intelligent incident triage (Verizon)",
        "skills": ["Python", "LangChain", "Kubernetes", "Prompt Engineering", "REST API"],
        "link": "Text-only. No production logs in screenshots.",
        "media": "Optional diagram: OpenSearch + git + Jira + change windows → LangGraph → RCA draft → human approve.",
        "desc": (
            "Built a FastAPI + LangGraph service that auto-correlates OpenSearch logs, git diffs, "
            "Jira issues, and Kubernetes change windows into evidence-backed RCAs. The graph "
            "retrieves context, drafts a timeline, cites sources, and stops for a human when "
            "confidence is low or a mutating action is proposed. Reduced manual triage by giving "
            "on-call a cited first draft instead of a blank page. Hire this pattern for ops copilots, "
            "ticket routers, or any agent that must not hallucinate citations."
        ),
    },
    {
        "id": 3,
        "title": "Medical QLoRA SFT + prompt-strategy router",
        "role": "ML engineer — BITS M.Tech LLM / GenAI (Group 101)",
        "skills": ["Python", "Machine Learning", "Prompt Engineering", "PyTorch", "Hugging Face"],
        "link": "https://github.com/arunkumar4189/AI-ML-Projects/tree/main/LLM-Gen-AI",
        "media": "Export training-loss chart and the Part A comparison table from the assignment notebooks (HTML already in repo).",
        "desc": (
            "Built a medical instruction dataset from a PDF corpus and QLoRA-tuned GPT-2 Medium "
            "(4-bit NF4, LoRA r=16, alpha=32) with Hugging Face PEFT. Reused the adapter as a "
            "prompting system with one eval contract: zero/few-shot, self-critique, JSON "
            "function-calling, CoT, tree-of-thought, self-consistency, ReAct, and a router that "
            "picks a strategy per query. Scored a shared medical query set for groundedness, JSON "
            "validity, tokens, and latency. Use this when you need domain SFT plus an eval harness, "
            "not a one-off prompt."
        ),
    },
    {
        "id": 4,
        "title": "Grounded medical QA with verify-correct loop",
        "role": "NLP engineer — domain QA system (BITS M.Tech)",
        "skills": ["Natural Language Processing", "Machine Learning", "Python", "Generative AI", "Prompt Engineering"],
        "link": "https://github.com/arunkumar4189/AI-ML-Projects/blob/main/NLP/Domain-Specific%20Question%20Answering%20System.ipynb",
        "media": "Screenshot of a sample Q&A with retrieved snippet and corrected answer (public course text only).",
        "desc": (
            "Knowledge base of five clinical documents (diabetes, hypertension, COVID-19, asthma, "
            "appendicitis). Pipeline: retrieve passages, classify intent (BART), generate with "
            "Flan-T5, then an agentic verify-and-correct loop that rewrites answers which drift "
            "from source. Built for grounded, explainable clinical Q&A rather than open-ended "
            "chat. Same recipe as production RAG: citations, hallucination flags, and a second "
            "pass before the user sees the answer."
        ),
    },
    {
        "id": 5,
        "title": "Task-oriented helpdesk: 12 intents, NER, DST",
        "role": "NLP engineer — conversational AI assignment (BITS M.Tech)",
        "skills": ["Natural Language Processing", "Machine Learning", "Python", "Data Science", "REST API"],
        "link": "https://github.com/arunkumar4189/AI-ML-Projects/blob/main/NLP/Conversational%20AI%20and%20Sentiment.ipynb",
        "media": "Confusion matrix and a multi-turn dialogue-state table from the notebook.",
        "desc": (
            "University helpdesk assistant: 12 intents, 80+ labelled utterances, slot filling, "
            "regex/gazetteer NER, multi-turn dialogue state, simulated APIs, and safety/escalation "
            "for out-of-scope turns. Intent model is TF-IDF + logistic regression with a full "
            "classification report. Gold data was created for the domain (not a generic ATIS dump) "
            "so the bot understands courses, fees, exams, hostel, library, and scholarships. "
            "Template for any task-oriented bot: invent gold, train intent, track slots, call tools, "
            "refuse unsafe asks."
        ),
    },
    {
        "id": 6,
        "title": "SupportSense: LoRA intent, QA, Gradio, MLflow",
        "role": "ML / LLMOps engineer — cloud-native ML coursework",
        "skills": ["Python", "Machine Learning", "Docker", "REST API", "Generative AI"],
        "link": "https://github.com/arunkumar4189/AI-ML-Projects/tree/main/API%20Driven%20Cloud%20Native",
        "media": "Gradio UI screenshot (local/demo) and MLflow run table if you still have it; otherwise the course report PDF without personal emails.",
        "desc": (
            "Customer-support triage combining NLP and vision: Banking77 intent (DistilBERT + LoRA), "
            "sentiment, summarization, FAQ QA, image defect/caption, and a draft reply. Hugging Face "
            "Inference API, Gradio review UI, LLMOps metrics. Sister project: telco churn on 7,043 "
            "Kaggle rows with Logistic Regression vs Random Forest in MLflow and a Streamlit "
            "dashboard. Shows a full path from labeled data → tracked model → human review UI, which "
            "is what most Upwork 'chatbot' jobs are actually missing."
        ),
    },
]


def check(items: list[dict]) -> list[str]:
    errors = []
    for it in items:
        t, r, d, s = it["title"], it["role"], it["desc"], it["skills"]
        if len(t) > TITLE:
            errors.append(f"#{it['id']} title {len(t)}>{TITLE}: {t}")
        if len(r) > ROLE:
            errors.append(f"#{it['id']} role {len(r)}>{ROLE}")
        if len(d) > DESC:
            errors.append(f"#{it['id']} desc {len(d)}>{DESC}")
        if len(s) != SKILLS:
            errors.append(f"#{it['id']} skills {len(s)}!={SKILLS}")
    return errors


def render(items: list[dict]) -> str:
    lines = [
        "# Upwork portfolio items (publish these six)",
        "",
        "Limits from Upwork Help: **title 70**, **role 100**, **description 600**, **5 skill tags**.",
        "No email, phone, or LinkedIn in any field or screenshot.",
        "",
        "Add cards in this order (best first in the grid).",
        "",
    ]
    for it in items:
        lines += [
            f"## {it['id']}. {it['title']}",
            "",
            f"| Field | Limit | Count |",
            f"|---|---:|---:|",
            f"| Title | {TITLE} | {len(it['title'])} |",
            f"| Role | {ROLE} | {len(it['role'])} |",
            f"| Description | {DESC} | {len(it['desc'])} |",
            f"| Skills | {SKILLS} | {len(it['skills'])} |",
            "",
            "**Title**",
            "",
            "```",
            it["title"],
            "```",
            "",
            "**Role**",
            "",
            "```",
            it["role"],
            "```",
            "",
            "**Skills & deliverables** (exactly five)",
            "",
            ", ".join(it["skills"]),
            "",
            "**Project description**",
            "",
            "```",
            it["desc"],
            "```",
            "",
            f"**Link:** {it['link']}",
            "",
            f"**Media:** {it['media']}",
            "",
            "---",
            "",
        ]
    lines += [
        "## Optional extras (only if a client asks for CV / RL)",
        "",
        "Keep these off the main grid so the profile stays on-agent/RAG/NLP:",
        "",
        "- CNN cats-vs-dogs + from-scratch MLP (`DNN/`)",
        "- Seq2Seq Transformer summarization (`Conversational AI/Sequence-to-Sequence Transformer.ipynb`)",
        "- CLIP knowledge distillation on Flickr30k (`Conversational AI/Knowledge Distillation.ipynb`)",
        "",
        "If you add one extra, prefer the **CLIP distillation** card for multimodal jobs.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    errors = check(ITEMS)
    if errors:
        raise SystemExit("Limit errors:\n" + "\n".join(errors))
    OUT.write_text(render(ITEMS), encoding="utf-8")
    print(f"Wrote {OUT} ({len(ITEMS)} items, all within limits)")


if __name__ == "__main__":
    main()
