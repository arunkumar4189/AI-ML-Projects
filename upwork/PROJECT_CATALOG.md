# Project Catalog gigs (optional)

Publish **two or three**, not all five. Catalog titles work well around **70–75** characters. Each gig needs a clear deliverable, a timeline, and what the client must provide.

Pricing below is a **starting band** for India-based senior IC work. Raise after reviews. Always use Upwork milestones, never off-platform payment.

---

## Gig A — primary

**Title**

```
LangGraph + FastAPI agent MVP with tools and HITL
```

**Search tags (5):** Python, LangChain, FastAPI, Generative AI, REST API

**What the client gets (1 week / 1–2 weeks depending on tools):**

- Agent graph (LangGraph) with 2–4 tools
- FastAPI endpoint + simple auth
- Human-approval node for any write/mutating tool
- Trace log (tool name, args, result, decision)
- README and a 15-minute walkthrough

**Client provides:** API keys, tool specs, 10 example tasks, success rubric.

**Not included:** production SSO, multi-tenant billing, training a new base model.

**Suggested packages**

| Package | Scope | Starting price |
|---|---|---|
| Starter | 2 tools, 1 HITL gate, local demo | $800–$1,200 |
| Standard | 4 tools, eval on 20 tasks, Docker | $1,800–$2,800 |
| Plus | Standard + React/admin review queue | $3,500–$5,000 |

---

## Gig B — RAG

**Title**

```
Production-style RAG chatbot with citations and eval
```

**Tags:** Python, Machine Learning, Prompt Engineering, FastAPI, Generative AI

**Deliverable**

- Ingest PDF/DOCX/Markdown
- Chunk + embeddings + vector store
- Answer with citations
- 20-question eval set (faithfulness / refusal)
- FastAPI or Streamlit/Gradio UI

**Suggested packages:** $700 / $1,500 / $2,800 for 1 vs 5 vs 20 document types plus eval.

---

## Gig C — domain SFT

**Title**

```
QLoRA domain fine-tune + instruction data QA
```

**Tags:** Python, Machine Learning, PyTorch, Prompt Engineering, Hugging Face

**Deliverable**

- Instruction JSONL from client docs (with a quality pass)
- QLoRA adapter on a client-chosen small/medium model
- Before/after eval on a held-out set
- Inference snippet (Transformers or FastAPI)

**Not included:** training 70B+ models on your GPU bill without a compute milestone.

**Suggested packages:** $1,000 / $2,000 / $4,000 depending on dataset cleanup hours.

---

## Gig D — NLP bot (only if you want NLU jobs)

**Title**

```
Intent, NER, and dialogue-state prototype in Python
```

**Tags:** Natural Language Processing, Python, Machine Learning, Data Science, REST API

Gold-set design (intents/slots), baseline classifier, confusion matrix, FastAPI parse endpoint. **$600–$1,800**.

---

## Gig E — skip unless asked

Prompt-eval harness only (CoT/ReAct/JSON/router). Easy to underprice; fold it into Gig A or C instead.

---

## Catalog listing body (Gig A — paste)

```
I build multi-agent MVPs the way they run in production: LangGraph (or equivalent), FastAPI, typed tools, and a human-in-the-loop gate before anything can write to a ticket system, repo, or database.

You get a working agent, not a slide deck. We agree on 10 example tasks and a rubric up front. I instrument traces so you can see every tool call. Mutating actions require approval.

I am a Distinguished Engineer who has shipped agent platforms and SRE copilots, plus public coursework in QLoRA, RAG-style medical QA, and task-oriented dialogue. See the portfolio cards on this profile and the public GitHub AI-ML-Projects repo.

To start: send your tool list (or APIs), sample tasks, and whether you need a UI or API-only.
```
