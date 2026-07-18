# ACCOUNT SETUP GUIDE - Bug Bounty Programs
## Complete Step-by-Step for All 3 Platforms

---

## 1. Mozilla 0DIN (0din.ai) — FREE, HIGHEST PRIORITY

### Why First:
- FREE account (no subscription needed)
- Lowest barrier to entry
- Guardrail jailbreak pays $500-$1,000
- You test against models you already have access to (ChatGPT, Claude, Grok)
- Payout: 30 days after agreement

### Setup Steps:

1. **Go to https://0din.ai**
2. **Click "Sign Up" or "Register"**
3. **Enter:**
   - Full name (use real name for payment)
   - Email address
   - Password
   - Country: Nigeria
4. **Verify email**
5. **Review the Scope page:** https://0din.ai/policy
6. **IMPORTANT RULES:**
   - Guardrail jailbreak MUST work across ≥2 JEF-tested boundaries
   - Submit abstract FIRST → wait 3 business days → submit full PoC
   - Must NOT be employee of Mozilla or target company
   - Must NOT be in US-sanctioned country (Nigeria is NOT sanctioned ✓)
   - Payment requires government ID + W-8 form (non-US)

### Payment Process:
1. After bounty agreement, you'll need:
   - Government-issued photo ID (NIN, passport, or voter's card)
   - W-8BEN form (Certificate of Foreign Status) — 0DIN will provide
   - Bank account or PayPal for receiving payment
2. Payment processed 30 days after agreement

---

## 2. Anthropic HackerOne (hackerone.com/anthropic) — FREE

### Why Second:
- FREE to join
- Public since May 2026 (no invite needed)
- Up to $15,000 per finding
- Average payout: ~$1,284 per report
- Total paid: $550,835 across 429 reports

### Setup Steps:

1. **Go to https://hackerone.com/anthropic**
2. **Click "Join Program" or "Sign Up"**
3. **Create HackerOne account:**
   - Username (handle)
   - Email
   - Password
4. **Join the Anthropic program**
5. **Read the Policy carefully:**
   - Track 1: Model Safety (CBRN + cybersecurity jailbreaks) — Up to $15,000
   - Track 2: Product Security (Claude.ai, API, Code, SDK, MCP) — Up to $15,000
   - VDP (no money): Traditional infra issues (CSRF, XSS, SQLi) — recognition only
6. **Important: Don't waste time on VDP issues — they pay $0**

### Key Rules:
- Model Safety: Must be UNIVERSAL jailbreak (not just one specific prompt)
- Product Security: Must demonstrate actual security impact
- Claude Code exploits are HIGH VALUE (sandbox escapes, symlink following, etc.)
- MCP server vulnerabilities are in scope

### Payment Process:
1. Report accepted → Triaged → Validated
2. Bounty paid after fix is confirmed
3. Payment via HackerOne (supports PayPal, bank transfer, Bitcoin)

---

## 3. OpenAI Bugcrowd (bugcrowd.com/openai) — FREE

### Why Third:
- FREE to join
- Security bugs pay $200-$20,000
- Safety bounty pays $200-$100,000
- BUT: Model jailbreaks are OUT OF SCOPE for security program
- FOCUS ON: Sandbox escapes, auth bypasses, data exfiltration

### Setup Steps:

1. **Go to https://bugcrowd.com/openai**
2. **Click "Join"**
3. **Create Bugcrowd account:**
   - Email
   - Password
   - Handle
4. **Read the Scope carefully:**
   - IN SCOPE: XSS, CSRF, SQLi in ChatGPT, auth bypasses, API key exposure,
     Codex sandbox escapes, Code Interpreter escapes
   - OUT OF SCOPE: Model jailbreaks, DAN prompts, safety bypasses (report at
     openai.com/form/model-behavior-feedback instead)
   - Code Interpreter: Must show RCE OUTSIDE sandbox (kernel ≠ 4.4.0)
5. **GPT-5.5 Bio Bounty:** https://openai.smapply.org/prog/gpt-5-5-safety-bio-bounty-program/
   - $25,000 for universal jailbreak clearing 5 bio safety questions
   - Application-based, rolling acceptance

### Payment Process:
1. Report submitted → Triaged → Validated
2. Bounty per severity: P1 ($500-$6,500), P2 ($100-$3,500), P3 ($50-$500), P4 ($0)
3. Payment via Bugcrowd (PayPal, bank transfer)

---

## ACCOUNT SUMMARY TABLE

| Platform | URL | Cost | Payout Range | Payout Speed | Nigeria OK? |
|----------|-----|------|-------------|-------------|-------------|
| 0DIN | 0din.ai | FREE | $100-$15,000 | 30 days | ✅ YES |
| Anthropic | hackerone.com/anthropic | FREE | $100-$15,000 | Varies | ✅ YES |
| OpenAI | bugcrowd.com/openai | FREE | $200-$100,000 | Varies | ✅ YES |

---

## ACCESS TO AI MODELS

| Model | Access Method | Cost | Best For |
|-------|--------------|------|----------|
| GPT-4o / GPT-5 | ChatGPT Plus ($20/mo) or API | $20/mo | 0DIN guardrail testing |
| GPT-5 mini | ChatGPT Free tier | FREE | 0DIN guardrail testing |
| Claude Sonnet 4 | claude.ai Free tier | FREE | Anthropic model safety |
| Claude Opus 4.5 | claude.ai Pro ($20/mo) | $20/mo | Anthropic model safety |
| Claude Code | Claude Pro/Max | $20-200/mo | Agent exploitation (HIGHEST EV) |
| Grok 3/4 | X Premium ($8/mo) | $8/mo | 0DIN guardrail testing (weakest!) |
| Gemini 2.5 | Google AI Studio | FREE | 0DIN guardrail testing |
| Copilot | bing.com/chat | FREE | 0DIN guardrail testing |

---

## IMMEDIATE ACTION ITEMS

1. ✅ Create 0din.ai account RIGHT NOW
2. ✅ Create HackerOne account and join Anthropic program
3. ✅ Create Bugcrowd account and join OpenAI program
4. ✅ Test G-04 Chemist Code Language on ChatGPT free tier (GPT-4o mini)
5. ✅ Test G-02 Policy Puppetry on all available models
6. ✅ Test on Grok via X Premium (weakest guardrails = easiest $500)
