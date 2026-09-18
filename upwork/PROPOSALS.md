# Upwork proposal templates

Keep each proposal **150–250 words**. Open with their problem, not your biography. Attach **one** matching portfolio card.

Replace bracketed text. Do not include email, phone, or WhatsApp — Upwork will flag it.

---

## Template 1 — LangGraph / agent job

```
Hi [Name] — you need a [LangGraph / multi-agent] flow that can [use tools X, Y] and must not [take irreversible actions] without a person in the loop.

I would ship this in three steps:
1. Tool contracts + 10 gold tasks and a pass/fail rubric
2. LangGraph + FastAPI with a HITL node on every write tool and full traces
3. Eval on your 10 tasks, then a Dockerized handoff

I lead GenAI at Verizon (agent hosting platform + LangGraph SRE triage) and have public notebooks for medical SFT, RAG-style QA, and dialogue agents: github.com/arunkumar4189/AI-ML-Projects

One question so I can sequence the work: which tool is allowed to mutate state in v1, and which must stay read-only?

Happy to start with a paid discovery milestone ([N] hours) if the tool list is still fluid.
```

---

## Template 2 — RAG / chatbot job

```
Hi [Name] — the core risk in this job is uncited or stale answers, not the UI.

Plan:
1. Ingest the [N] document types you listed; chunk with an overlap you can tune
2. Retrieve + generate with mandatory citations; refuse when retrieval is empty
3. Freeze a 20-question eval (faithfulness, refusal, latency) before we talk “chat personality”

I have a public medical QA project with retrieve → Flan-T5 → verify-and-correct, plus QLoRA domain adaptation if you later want a custom model. Portfolio card: “Grounded medical QA with verify-correct loop”.

What is the worst wrong answer this bot could give a user? I will put that case in the eval set first.
```

---

## Template 3 — fine-tune / QLoRA job

```
Hi [Name] — I would not fine-tune until we know the base model is failing a labeled eval. Many “fine-tune” briefs are actually prompt + RAG jobs.

If we still need SFT:
1. QA your docs into instruction JSONL (I drop noisy PDF extracts)
2. QLoRA on a size that fits your serving budget (I have a public GPT-2 Medium medical adapter pipeline you can inspect)
3. Before/after scores on a held-out set; adapter + inference script as the handoff

Compute should be a separate milestone (your GPU or a cloud budget we agree in writing).

Do you already have a gold eval set, or should that be part of week one?
```

---

## Template 4 — LLM evaluation / AI trainer job

```
Hi [Name] — I score model and agent outputs with a written rubric: factuality, citation, instruction-following, and safety/HITL violations. I write the rationale, not just a 1–5 star.

Relevant work: production HITL on a multi-agent platform, SRE-trace review, medical SFT gold, 12-intent dialogue annotation, and a prompting eval harness (CoT, ReAct, JSON tools, self-critique).

I can start on a calibration batch of [20] items so we lock the guideline before volume.

Which failure matters more for you: hallucination, policy violation, or format/schema breaks?
```

---

## Template 5 — decline / redirect (use often)

```
Thanks for considering me. This looks like [high-volume bounding boxes / an overnight ChatGPT clone with no eval]. That is not the work I take.

If you later need an agent with tool traces, RAG with citations, or a domain fine-tune with an eval set, I can help. Wishing you a good hire.
```

---

## First-week operating rules

- Never go off Upwork chat for the deal
- One milestone before any training-GPU spend
- Do not reuse Verizon code, prompts, or data
- If the job is labeling-only, point them at your OpenTrain profile instead of underbidding engineering rates
