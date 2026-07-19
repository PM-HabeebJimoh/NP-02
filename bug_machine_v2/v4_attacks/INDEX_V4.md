# 📂 V4 ATTACK FRAMEWORK — Master Index

## Quick Start
1. Read `MASTER_ATTACK_FRAMEWORK.md` for the full strategy
2. Start testing with `PE_PROMPTS.md` (easiest, $100 per model)
3. Move to `GJ_PROMPTS.md` for guardrail jailbreaks ($500-$1,000)
4. Try `AG_ATTACKS.md` for agentic vulnerabilities ($2,500-$15,000)
5. If you have Claude Code access, try `CLAUDE_CODE_TESTS.md`
6. Track everything in `TESTING_LOG.md`
7. Submit findings using `SUBMISSION_GUIDE.md`

## Files in V4

| File | Purpose | Priority |
|------|---------|----------|
| `MASTER_ATTACK_FRAMEWORK.md` | Complete strategy, intelligence, and revenue projections | READ FIRST |
| `PE_PROMPTS.md` | Prompt Extraction — copy-paste ready prompts for 20+ models | START HERE |
| `GJ_PROMPTS.md` | Guardrail Jailbreak — 7 multi-turn attack sequences | SECOND |
| `AG_ATTACKS.md` | Agentic Vulnerability — 5 exploit PoCs | THIRD |
| `CLAUDE_CODE_TESTS.md` | Claude Code Product Security — 5 test procedures | FOURTH |
| `SUBMISSION_GUIDE.md` | How to submit to 0DIN, HackerOne, and Bugcrowd | AS NEEDED |
| `TESTING_LOG.md` | Track all tests and results | ALWAYS |

## What Changed from V3

### V3 Problems:
- All single-turn prompts → models are hardened against these
- Known techniques (DAN, encoding, etc.) → all patched
- Wrong targets (focused on Anthropic) → out of scope for illicit substances
- No testing infrastructure → theory only, never verified
- No retargetability proof → can't submit to 0DIN

### V4 Solutions:
- ALL multi-turn attacks (3-5 turns minimum)
- Novel techniques based on July 2026 research
- Correct targets (GPT-5 mini, Gemini 3.5 Flash, Perplexity)
- Every technique includes retargetability to 2nd JEF boundary
- Copy-paste ready with exact prompts
- Testing log template for evidence collection
- Submission guide for each platform

## Revenue Targets

| Scenario | Amount | How |
|----------|--------|-----|
| Minimum | $300-$500 | 3-5 prompt extractions |
| Likely | $1,800-$6,500 | Extractions + 1 jailbreak + 1 HackerOne finding |
| Best Case | $17,000-$33,000 | Multiple findings across all platforms |
| Stretch | $50,000+ | Major agentic vulnerability on multiple platforms |

## Previous Files (for reference only)
- `/bug_machine_v2/V3_REAL_STRATEGY.md` — V3 strategy (failed)
- `/bug_machine_v2/GENUINELY_NEW_DISCOVERIES.md` — Claude Code binary analysis findings
- `/bug_machine_v2/QUICK_START_TESTING.md` — V3 testing guide (failed)
- `/bug_machine_v2/VERIFIED_BREAKTHROUGHS.md` — Already-reported issues
