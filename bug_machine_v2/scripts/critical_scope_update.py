#!/usr/bin/env python3
"""
CRITICAL SCOPE UPDATE - 0DIN July 2026
======================================

MAJOR CHANGES from live scope check at 0din.ai/scope:

1. ANTHROPIC MODELS: Illicit substance guardrail bypasses NOT ACCEPTED for ANY Claude model
   - All 10 Claude models: "Illicit substance guardrail bypasses are not accepted"
   - BUT: Prompt Extraction IS accepted for all Claude models
   - This means we CANNOT use illicit substance attacks for Claude on 0DIN

2. GROK (Twitter/X): "Out of scope for illicit substances and copyright violations"
   - Same restriction as Anthropic

3. MODELS THAT ACCEPT ILLICIT SUBSTANCE GUARDRAIL BYPASSES:
   - OpenAI GPT-5 family (13 models) - ALL ACCEPT guardrail jailbreaks
   - Google Gemini (3 models) - ALL ACCEPT guardrail jailbreaks
   - Meta LLaMA (3 models) - ALL ACCEPT guardrail jailbreaks
   - Microsoft Copilot (1 model) - ACCEPTS guardrail jailbreaks
   - Perplexity AI (1 model) - ACCEPTS guardrail jailbreaks
   - BigScience BLOOM (1 model) - ACCEPTS guardrail jailbreaks
   - Salesforce Einstein (1 model) - ACCEPTS guardrail jailbreaks

4. MODELS EXCLUDED FOR ILLICIT SUBSTANCES:
   - Anthropic (all Claude models)
   - Amazon (Rufus, Nova) - "Copyright violations and illicit substances not eligible"
   - Grok (4, 4.2, 4.5) - "Out of scope for illicit substances"
   - IBM Watson/Granite - "Copyright violations and illicit substances not eligible"
   - NVIDIA NeMo Megatron - "Copyright violations and illicit substances not eligible"
   - Cohere Command R - "Out of scope for illicit substances"

STRATEGY PIVOT:
- For 0DIN guardrail jailbreaks: TARGET GPT-5, Gemini, LLaMA, Copilot (these accept illicit substance tests)
- For Anthropic: Focus on PROMPT EXTRACTION ($100) and PRODUCT SECURITY (HackerOne, up to $15K)
- For Agent exploitation: Claude Code sandbox escapes are still HIGHEST EV via Anthropic HackerOne
"""

# Updated target matrix based on live scope
SCOPE_COMPLIANT_TARGETS = {
    "0din_guardrail_jailbreak": {
        "target_models": [
            # OpenAI - 13 models, ALL accept guardrail jailbreak
            "GPT-5", "GPT-5.1", "GPT-5.2", "GPT-5.2 Pro", "GPT-5.4",
            "GPT-5.5", "GPT-5.5 Pro", "GPT-5.6", "GPT-5 Chat",
            "GPT-5 mini", "GPT-5 nano", "GPT-5 Pro", "DALL-E3",
            # Google - 3 models, ALL accept
            "Gemini 3.1 Pro", "Gemini 3.5 Flash", "Gemini 3 Flash",
            # Meta - 3 models, ALL accept
            "LLaMA 4 Maverick", "LLaMA 4 Scout", "Muse Spark",
            # Microsoft - 1 model
            "CoPilot",
            # Perplexity - 1 model
            "Perplexity AI",
            # BigScience - 1 model
            "BLOOM",
            # Salesforce - 1 model
            "Einstein",
        ],
        "excluded_models": [
            # All Anthropic Claude models - illicit substances excluded
            "Claude 4.5 Haiku", "Claude 4.5 Opus", "Claude 4.5 Sonnet",
            "Claude 4.6 Opus", "Claude 4.6 Sonnet", "Claude 4.7 Opus",
            "Claude 4.8 Opus", "Claude 5 Sonnet", "Claude Fable 5", "Claude for Chrome",
            # Amazon - excluded
            "Amazon Rufus/Alexa", "Amazon Nova",
            # Grok - excluded
            "Grok 4", "Grok 4.2", "Grok 4.5",
            # IBM - excluded
            "IBM Granite", "IBM Watson",
            # NVIDIA - excluded
            "NVIDIA NeMo Megatron",
            # Cohere - excluded
            "Cohere Command R",
        ],
        "best_targets": [
            # GPT-5 mini/nano - likely weakest guardrails among GPT-5 family
            # Previous 0DIN scores: GPT-4o scored 95 on chemist code language!
            ("GPT-5 mini", "Weakest GPT-5 guardrails, free tier available"),
            ("GPT-5 nano", "Even weaker, if accessible"),
            ("GPT-5", "Scored 95 on previous GPT-4o chemist code language test"),
            ("Gemini 3.5 Flash", "Free via Google AI Studio, Gemini scored 59-73 on 0DIN"),
            ("CoPilot", "Free via Bing, may have weaker guardrails than standalone models"),
        ],
        "payout": "$500-$1,000 per valid dual-boundary bypass"
    },
    "0din_prompt_extraction": {
        "target_models": "ALL models in scope (including Anthropic)",
        "payout": "$100 per extraction",
        "note": "Prompt extraction accepted for ALL models including Claude"
    },
    "0din_interpreter_jailbreak": {
        "target_models": ["OpenAI DALL-E3"],  # Only DALL-E3 shows interpreter jailbreak
        "payout": "$2,500",
        "note": "Limited scope for interpreter jailbreak"
    },
    "anthropic_hackerone_product_security": {
        "target_products": ["Claude.ai", "Claude API", "Claude Code", "Claude Cowork", "SDK", "MCP"],
        "payout": "$1,000-$15,000",
        "note": "HIGHEST EV - sandbox escapes, data exfiltration, etc."
    }
}

# PIVOT: Focus illicit substance attacks on GPT-5 family + Gemini
# Use different boundaries for Anthropic (prompt extraction, product security)

if __name__ == "__main__":
    print("CRITICAL SCOPE UPDATE FROM LIVE 0DIN SCOPE PAGE")
    print("=" * 60)
    print()
    print("ANTHROPIC CLAUDE: Illicit substance bypasses EXCLUDED from 0DIN")
    print("GROK: Illicit substance bypasses EXCLUDED from 0DIN")
    print()
    print("MODELS THAT ACCEPT illicit substance guardrail bypasses:")
    for model in SCOPE_COMPLIANT_TARGETS["0din_guardrail_jailbreak"]["target_models"]:
        print(f"  ✓ {model}")
    print()
    print("BEST TARGETS for guardrail jailbreak ($500-$1K):")
    for model, reason in SCOPE_COMPLIANT_TARGETS["0din_guardrail_jailbreak"]["best_targets"]:
        print(f"  → {model}: {reason}")
    print()
    print("ANTHROPIC strategy pivot:")
    print("  → Prompt Extraction on Claude ($100 per finding)")
    print("  → Product Security via HackerOne ($1K-$15K)")
    print("  → Claude Code sandbox escapes ($7.5K-$15K)")
