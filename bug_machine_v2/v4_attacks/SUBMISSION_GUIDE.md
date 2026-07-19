# 📤 SUBMISSION GUIDE — Step-by-Step for Each Bounty Platform

---

## 1. 0DIN (Mozilla) — 0din.ai

### What 0DIN Pays For:
| Category | Payout | Requirements |
|----------|--------|-------------|
| Prompt Extraction | $100 | Extract verbatim system prompt |
| Guardrail Jailbreak | $500-$1,000 | Must work across ≥2 JEF boundaries |
| Interpreter Jailbreak | $2,500 | Escape code interpreter sandbox |
| Content Manipulation | $5,000 | Inject harmful/misleading content |
| Weights/Layers Disclosure | $15,000 | Extract model parameters |
| Agentic Vulnerability | $2,500-$15,000 | Zero-click data exfil, code exec, etc. |

### Submission Process:

**Step 1: Create Account**
- Go to https://0din.ai
- Sign up with your email
- Complete profile with real name (must match government ID)

**Step 2: Submit Abstract**
- Click "Submit Finding" or email 0din@mozilla.com
- Format:
  ```
  Subject: [Category] - [Brief Title]
  
  Model(s) Affected: [e.g., GPT-5 mini, Gemini 3.5 Flash]
  Category: [Prompt Extraction / Guardrail Jailbreak / Interpreter Jailbreak / Content Manipulation / Agentic Vulnerability]
  
  Abstract: [2-3 sentence description of the vulnerability]
  
  Technique: [Name of your technique]
  
  JEF Boundaries Tested: [e.g., Illicit Substances: Crystal Meth + Dangerous Substances: Nerve Agent]
  
  Reproducibility: [e.g., 4/5 attempts successful at temperature 0.7]
  ```

**Step 3: Wait for Response (3 business days)**
- 0DIN will review and respond
- They may ask for more details

**Step 4: Submit Full PoC**
If your abstract is accepted, submit:
1. Complete prompts used (every turn of multi-turn attacks)
2. Screenshots of model responses
3. JEF scores if you can calculate them
4. Retargetability evidence (same technique on 2+ boundaries)

**Step 5: Identity Verification**
Before payout, you need:
- Government-issued photo ID (International Passport, National ID, or Voter's Card)
- W-8BEN form (Certificate of Foreign Status for US tax withholding)
  - Download from IRS: https://www.irs.gov/forms-pubs/about-form-w-8-ben
  - Fill in your Nigerian details
  - Nigeria is NOT on US sanctions list ✅

**Step 6: Payout**
- After agreement: 30 days to payout
- Payment via bank transfer or crypto (check with 0DIN)

---

## 2. Anthropic HackerOne — hackerone.com/anthropic

### What Anthropic Pays For:

**Track 1 — Model Safety:**
- Universal jailbreaks in CBRN + cybersecurity
- Up to $15,000

**Track 2 — Product Security:**
- Claude.ai, Claude API, Claude Code, SDK, MCP
- Up to $15,000
- THIS IS WHERE OUR CLAUDE CODE DISCOVERIES GO

**VDP (No Money):**
- Traditional infra issues (CSRF, XSS, SQLi)
- Recognition only — DON'T submit here

**NEW (July 6, 2026): Claude Fable 5 Cybersecurity Jailbreak**
- Specific bounty for cybersecurity jailbreaks on Claude Fable 5
- Scope EXCLUSIVELY cybersecurity (not bio/drugs/prompt extraction)

### Submission Process:

**Step 1: Create HackerOne Account**
- Go to https://hackerone.com/anthropic
- Sign up or log in

**Step 2: Submit Report**
- Click "Submit Report"
- Select "Anthropic" as the program

**Format:**
```
Title: [Clear, specific title]

Severity: [Low / Medium / High / Critical]

Category: [Model Safety / Product Security]

Description:
[Clear description of the vulnerability]

Steps to Reproduce:
1. [Step 1]
2. [Step 2]
3. [etc.]

Impact:
[What an attacker could do with this vulnerability]

Proof of Concept:
[Screenshots, logs, code snippets]

Affected Versions:
[e.g., Claude Code v2.1.215]
```

**Step 3: Triage**
- Anthropic's security team will review
- They may ask for clarification or additional details
- Typical response time: 1-7 days

**Step 4: Resolution & Bounty**
- If accepted, Anthropic will fix the issue
- Bounty amount determined by severity
- Average payout: ~$1,284 (based on $550,835 across 429 reports)

---

## 3. OpenAI Bugcrowd — bugcrowd.com/openai

### What OpenAI Pays For:

**Security Bug Bounty:**
- XSS, CSRF, SQLi, auth bypass, API key exposure
- Codex sandbox escapes, Code Interpreter escapes
- Up to $100,000

**Safety Bug Bounty:**
- AI agent vulnerabilities
- Prompt injection with REAL-WORLD HARM
- Data exfiltration via agents
- $200-$100,000

**GPT-5.5 Bio Bounty:**
- $25,000 for universal jailbreak clearing 5 bio safety questions
- Application-based (need to apply first)

**OUT OF SCOPE:**
- Model jailbreaks/safety bypasses are STRICTLY OUT OF SCOPE for the security program
- Only submit AGENTIC vulnerabilities, not simple jailbreaks

### What to Submit Here:
- **AG-1** (Markdown Image Exfil from Copilot/ChatGPT)
- **AG-3** (PDF Annotation Injection in ChatGPT file upload)
- **AG-4** (Copilot Zero-Click Email)
- Any data exfiltration from ChatGPT Agent

### Submission Process:
1. Go to https://bugcrowd.com/openai
2. Create Bugcrowd account
3. Submit report with full PoC
4. Wait for triage (1-14 days)

---

## 💰 TOTAL REVENUE POTENTIAL

| Platform | Finding Type | Payout Range | Likelihood |
|----------|-------------|-------------|-----------|
| 0DIN | Prompt Extraction (5-10 models) | $500-$1,000 | HIGH |
| 0DIN | Guardrail Jailbreak | $500-$1,000 | MEDIUM |
| 0DIN | Agentic Vulnerability | $2,500-$15,000 | LOW-MEDIUM |
| Anthropic | Claude Code Product Security | $500-$5,000 | MEDIUM |
| OpenAI | Safety Bug Bounty (agentic) | $200-$100,000 | LOW |

### Realistic Scenario:
- Prompt Extraction: 3-5 successful extractions = $300-$500
- Guardrail Jailbreak: 1 successful technique = $500-$1,000
- Anthropic HackerOne: 1-2 findings = $1,000-$5,000
- **TOTAL: $1,800-$6,500** (most likely outcome)

### Best Case Scenario:
- Prompt Extraction: 10+ models = $1,000+
- Guardrail Jailbreak: 2+ techniques = $1,000-$2,000
- Agentic Vulnerability: 1 zero-click finding = $10,000-$15,000
- Anthropic: 3+ findings = $5,000-$15,000
- **TOTAL: $17,000-$33,000**

---

## 📋 PRE-SUBMISSION CHECKLIST

Before submitting ANY finding, verify:

- [ ] **Is this genuinely new?** Search 0DIN disclosures, HackerOne public reports, and recent research to make sure it hasn't been reported
- [ ] **Is it in scope?** Check the platform's current scope page
- [ ] **Is it reproducible?** Test at least 3 times with consistent results
- [ ] **Do I have evidence?** Screenshots, logs, and full conversation transcripts
- [ ] **Do I have retargetability proof?** (For 0DIN guardrail jailbreaks)
- [ ] **Do I have my identity documents ready?** (Government ID + W-8BEN for 0DIN)
- [ ] **Am I not violating any laws?** Only test on your own accounts and systems

---

## 🕐 TIMELINE

| Week | Focus | Expected Outcome |
|------|-------|-----------------|
| Week 1 | Prompt Extraction testing | 3-10 successful extractions |
| Week 2 | Guardrail Jailbreak testing | 1-2 working techniques |
| Week 3 | Agentic attack testing | 1 working exploit |
| Week 4 | Claude Code + submissions | 1-2 HackerOne findings |
| Week 5-6 | 0DIN response + resubmit | Acceptances/rejections |
| Week 7-8 | Payout processing | Money received |

**IMPORTANT:** 0DIN takes 30 days to pay after agreement. Anthropic HackerOne varies. Plan for 6-8 weeks from first submission to first payout.
