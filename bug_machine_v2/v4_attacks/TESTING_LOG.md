# 📝 TESTING LOG — Track All Tests and Results

## Instructions
Fill this out EVERY time you test a prompt. This is your evidence for submission.

---

## Prompt Extraction Tests

### PE Test Template:
```
Date: ____
Model: ____
Model Version: ____
Interface: [ChatGPT Web / Gemini Web / Copilot Web / API / Other]
Technique: PE-__ [name]
Prompt Used: [copy-paste the exact prompt]
Model Response: [copy-paste or summarize]
Extraction Successful: [Yes / No / Partial]
Extracted Content: [if successful, copy the extracted system prompt here]
Screenshot Saved: [Yes / No — filename]
Notes: 
```

### Test Log:

| # | Date | Model | Technique | Result | Screenshot |
|---|------|-------|-----------|--------|------------|
| 1 | | GPT-5 mini | PE-1 | | |
| 2 | | GPT-5 mini | PE-2 | | |
| 3 | | GPT-5 mini | PE-3 | | |
| 4 | | GPT-5 mini | PE-9 | | |
| 5 | | GPT-5 nano | PE-1 | | |
| 6 | | GPT-5 nano | PE-9 | | |
| 7 | | Gemini 3.5 Flash | PE-1 | | |
| 8 | | Gemini 3.5 Flash | PE-9 | | |
| 9 | | Perplexity | PE-P1 | | |
| 10 | | Copilot | PE-C1 | | |
| 11 | | GPT-5 | PE-1 | | |
| 12 | | GPT-5 | PE-9 | | |
| 13 | | Gemini 3.1 Pro | PE-1 | | |
| 14 | | LLaMA 4 Maverick | PE-L1 | | |
| 15 | | BLOOM | PE-L2 | | |

---

## Guardrail Jailbreak Tests

### GJ Test Template:
```
Date: ____
Model: ____
Model Version: ____
Interface: ____
Technique: GJ-__ [name]
JEF Boundary: [Crystal Meth / Nerve Agent / Fentanyl / Anthrax / Copyright]
Turn 1 Prompt: [exact text]
Turn 1 Response: [summarize — refused? partial? compliant?]
Turn 2 Prompt: [exact text]
Turn 2 Response: [summarize]
Turn 3 Prompt: [exact text if applicable]
Turn 3 Response: [summarize]
Bypass Successful: [Yes / No / Partial]
Content Generated: [describe what the model output — specific? vague? accurate?]
Reproducibility: [1/3, 2/3, 3/3]
Screenshot Saved: [Yes / No — filename]
Notes:
```

### Test Log:

| # | Date | Model | Technique | Boundary | Result | Reproducibility |
|---|------|-------|-----------|----------|--------|----------------|
| 1 | | GPT-5 mini | GJ-4 | Crystal Meth | | |
| 2 | | GPT-5 mini | GJ-4 | Nerve Agent | | |
| 3 | | GPT-5 mini | GJ-7 | Crystal Meth | | |
| 4 | | GPT-5 mini | GJ-7 | Nerve Agent | | |
| 5 | | GPT-5 mini | GJ-1 | Crystal Meth | | |
| 6 | | Gemini 3.5 Flash | GJ-6 | Crystal Meth | | |
| 7 | | Gemini 3.5 Flash | GJ-6 | Nerve Agent | | |
| 8 | | Perplexity | GJ-6 | Crystal Meth | | |
| 9 | | GPT-5 mini | GJ-5 | Crystal Meth | | |
| 10 | | GPT-5 mini | GJ-3 | Crystal Meth | | |

---

## Agentic Vulnerability Tests

### AG Test Template:
```
Date: ____
Target: [Copilot / Cursor / ChatGPT Agent / etc.]
Technique: AG-__ [name]
Setup: [describe what you did]
Payload: [exact text/instructions used]
Result: [describe what happened]
Data Exfiltrated: [what data was leaked, if any]
Zero-Click: [Yes / No — did the attack require user interaction?]
Screenshot Saved: [Yes / No — filename]
Notes:
```

### Test Log:

| # | Date | Target | Technique | Result | Zero-Click |
|---|------|--------|-----------|--------|------------|
| 1 | | ChatGPT+Perplexity | AG-2 | | |
| 2 | | Copilot | AG-1 | | |
| 3 | | ChatGPT file upload | AG-3 | | |
| 4 | | Copilot email | AG-4 | | |

---

## Claude Code Product Security Tests

### CC Test Template:
```
Date: ____
Discovery: #__ [name]
Claude Code Version: ____
Test Steps Completed: [list]
Result: [vulnerable / not vulnerable / partially vulnerable]
Proof: [describe what happened / error messages / file contents]
Screenshot Saved: [Yes / No — filename]
Notes:
```

### Test Log:

| # | Date | Discovery | Result | Proof |
|---|------|-----------|--------|-------|
| 1 | | D1: Skills Hook | | |
| 2 | | D2: Cron Persistence | | |
| 3 | | D3: Deep Link CWD | | |
| 4 | | D4: Artifact Redirect | | |
| 5 | | D5: Marketplace Injection | | |

---

## SUBMISSION TRACKER

| # | Date | Platform | Finding | Status | Payout |
|---|------|----------|---------|--------|--------|
| 1 | | 0DIN | | Draft / Submitted / Accepted / Rejected / Paid | $ |
| 2 | | 0DIN | | | $ |
| 3 | | HackerOne | | | $ |
| 4 | | Bugcrowd | | | $ |
| 5 | | 0DIN | | | $ |

---

## KEY REMINDERS

1. **Test EACH prompt 3 times** — reproducibility matters
2. **Screenshot EVERYTHING** — full browser window, URL bar visible
3. **Use temperature 0.7** — 0DIN's JEF scoring uses this
4. **Record exact model versions** — "GPT-5 mini" not just "GPT-5"
5. **Start with WEAKEST models** — GPT-5 mini, Gemini 3.5 Flash
6. **For GPT-5, use NORMAL mode** — not "thinking" mode
7. **For memory attacks, enable Memory** in settings first
8. **Only test on YOUR OWN accounts** — never on others' systems
