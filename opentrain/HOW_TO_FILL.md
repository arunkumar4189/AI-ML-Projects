# How to fill the OpenTrain wizard

Path: **Settings → Profile** (or finish onboarding if the wizard is still open).

OpenTrain docs: [Profile setup](https://www.opentrain.ai/docs/trainers/profile-setup/).

## 1. Resume upload

1. **General resume (required):** upload `Arun_Kumar_Resume (1).docx.pdf` (career history).
2. **Data labeling resume (optional):** upload `opentrain/Arun_Kumar_OpenTrain_Data_Labeling_Resume.pdf`.

The parser pre-fills work history and education. Review every auto-filled field; OpenTrain cross-checks later uploads for consistency.

## 2. Professional details

| Field | Value |
|---|---|
| Full name | Arun Kumar Kumari Arumugam |
| Country | India |
| City | Chennai |
| Phone | +91 95669 16623 |
| LinkedIn | https://linkedin.com/in/arunkumar |
| Public profile slug | already live as `arun-k-35` |

## 3. AI training experience

- Level: **Intermediate (1–3 years)**
- Profile overview: paste from `PROFILE_COPY_PASTE.md`
- Add **one labeling-experience row per tool**, even if dates overlap (OpenTrain matching filters by software)

Data types to tick: **text, document, code, image, medical**  
Label / task types to tick: **classification, NER, evaluation/rating, SFT, fine-tuning, RLHF, red-teaming, prompt design / instruction writing** (use the closest wizard labels)

## 4. Software and specializations

Select only tools you have actually used:

- Internal / proprietary tooling (Verizon Agentic Universe, MCP agents)
- Hugging Face (Transformers, PEFT/QLoRA, Datasets, Inference API)
- Jupyter / custom Python annotation pipelines
- MLflow (experiment tracking and model evaluation)
- Gradio / Streamlit (human review UIs)

Do **not** tick Scale AI, Labelbox, CVAT, Appen, Remotasks, or SuperAnnotate unless you later add real work on those platforms.

## 5. Education and languages

- M.Tech, Artificial Intelligence & Machine Learning — BITS Pilani — 2025–2027 (expected)
- B.E., Computer Science & Engineering — Anna University, Chennai — 2010

Languages:

- English — Fluent (or Native/Bilingual if that matches how you work)
- Add Tamil (or others) only if you are comfortable annotating in them

## 6. Work history

Leave Verizon / Tech Mahindra / Wipro as on the general resume. Do not replace engineering roles with invented labeling titles. AI-training work is described in the **labeling experience** section, not by rewriting job titles.

## 7. Rate and availability

Set these yourself. A senior IC/architect doing LLM evaluation (not commodity image boxes) commonly lands in a higher band than high-volume labeling. Typical India OpenTrain public profiles for LLM eval currently span roughly **$18–$40+/hr**; pick a rate you will actually accept and an hours band you can keep (for example **&lt; 20 hrs/week** while employed full-time).

## 8. Public profile

- Photo: a clear professional headshot (PNG/JPG, &lt; 5 MB)
- Title: from `PROFILE_COPY_PASTE.md`
- Top 3 industries: **Healthcare / medical NLP**, **Telecommunications / enterprise software**, **LLM evaluation & AI safety**

## 9. Review and submit

Confirm overview ≥ 150 characters, at least one labeling entry, and that the two resumes do not contradict dates or employers.

Then: **Settings → Profile → Visibility = Public**.