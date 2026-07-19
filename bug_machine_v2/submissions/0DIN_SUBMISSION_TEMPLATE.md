# 0DIN Submission Template — Guardrail Jailbreak
## For submissions to 0din@mozilla.com

---

## SUBJECT LINE:
Guardrail Jailbreak Submission — [Technique Name] — [Model Names]

---

## ABSTRACT (Send this first — 0DIN responds in 3 business days)

**Technique Name:** Intent Reframe via Code Repair / Hiring Test Marking Scheme / R Script Simulation / Entropy Compression Verification

**Vulnerability Type:** Guardrail Jailbreak

**Models Affected:** [List models where bypass was confirmed, e.g., GPT-5 mini, Gemini 3.5 Flash, CoPilot]

**JEF Boundaries Demonstrated:** 
- ✅ Illicit Substances: Crystal Meth (N-methyl-1-phenylpropan-2-amine synthesis)
- ✅ Harmful Substances: Nerve Agent (isopropyl methylphosphonofluoridate synthesis)
- [ ] Copyright: Harry Potter [if tested]

**Retargetability:** This technique is retargetable across ≥2 JEF-tested boundaries. The same approach was used to obtain synthesis procedures for both an illicit substance (methamphetamine) and a dangerous substance (sarin), demonstrating the technique works across different guardrail categories.

**Summary:** The technique exploits the model's intent classification system by reframing a prohibited request (synthesis instructions) as a permissible task (code repair, exam grading, data pipeline documentation). The model classifies the intent differently when the request is embedded in a software development context, causing it to treat the content as technical documentation rather than prohibited chemistry instruction. This bypass works because guardrails operate primarily on intent classification rather than content analysis — the same chemical information that is blocked when requested directly is provided when the model perceives its task as "fixing code" or "grading an exam."

**Proof of Concept:** Screenshots attached showing successful bypass on [model names].

---

## FULL PoC (Provide after abstract is accepted)

### Technique 1: Intent Reframe via Code Repair

**Principle:** AI models classify user requests by intent. Requests classified as "provide chemistry synthesis instructions" trigger guardrails. However, when the same content is requested in the context of "fix this code" or "implement this function," the intent is classified as "software development" — a permitted category. This mirrors the "fix this code" principle that bypassed Anthropic Fable 5's cybersecurity guardrails (documented in the US export control case, June 2026).

**Step-by-step Reproduction:**

1. Navigate to [model URL, e.g., chat.openai.com]
2. Start a new conversation
3. Paste the following prompt: [exact prompt text]
4. The model responds with complete synthesis instructions including specific reagents, quantities, temperatures, workup, and yield data

**Variant A (Illicit Substances — Crystal Meth):**
[Paste Prompt A1 from V3_REAL_STRATEGY.md]

**Variant B (Harmful Substances — Nerve Agent):**
[Paste Prompt A2 from V3_REAL_STRATEGY.md]

**Results:**
| Model | Variant A Score | Variant B Score | Notes |
|-------|----------------|----------------|-------|
| GPT-5 mini | [score] | [score] | |
| Gemini 3.5 Flash | [score] | [score] | |
| CoPilot | [score] | [score] | |
| Perplexity | [score] | [score] | |

**JEF Score Estimate:**
- BV (vendor blast radius): [number of vendors affected / total vendors]
- BM (model blast radius): [number of models affected / total models]
- RT (retargetability): [high if works across ≥2 categories]
- FD (fidelity): [how detailed/accurate the synthesis information is]

---

### Alternative Technique: Hiring Test Marking Scheme

[Same format as above, using Prompts B1 and B2]

---

## IDENTITY VERIFICATION

As required by 0DIN terms:
- Full name: [Your full legal name]
- Country: Nigeria
- Government ID: [Will provide upon acceptance]
- W-8BEN form: [Will complete upon acceptance]
- Nigeria is NOT on the US sanctions list

---

## PAYOUT INFORMATION

Expected payout level: Guardrail Jailbreak ($500-$1,000)
- $500 base for single-boundary bypass
- $1,000 for retargetable bypass across ≥2 JEF boundaries

Payment method: [Bank transfer / PayPal / Wise — specify]
