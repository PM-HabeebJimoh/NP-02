#!/usr/bin/env python3
"""
SUBMISSION FACTORY V2
=====================
Generates properly formatted reports for 0DIN, OpenAI Bugcrowd, and Anthropic HackerOne.
Each platform has different requirements - this handles all of them.
"""

import json
import os
from datetime import datetime
from typing import Dict, Optional

# ============================================================
# 0DIN SUBMISSION FORMAT
# ============================================================

def generate_0din_submission(
    boundary_type: str,  # prompt_extraction, guardrail_jailbreak, interpreter_jailbreak, content_manipulation
    models_affected: list,
    attack_description: str,
    full_prompt: str,
    model_outputs: list,
    technique_tags: list,
    jef_boundaries_tested: list = None,
    severity: str = "Low",
    researcher_name: str = "",
    researcher_email: str = ""
) -> Dict:
    """
    Generate a 0DIN submission.
    
    KEY RULES:
    - Guardrail jailbreak MUST demonstrate bypass across ≥2 JEF-tested boundaries
    - Must include: abstract, full prompt, model outputs, technique classification
    - Submit abstract first at 0din.ai, wait for sign-off, then submit full PoC
    """
    
    jef_boundaries_tested = jef_boundaries_tested or []
    
    submission = {
        "submission_type": boundary_type,
        "severity": severity,
        "researcher": {
            "name": researcher_name,
            "email": researcher_email,
            "country": "Nigeria"
        },
        "vulnerability": {
            "title": f"Multiple Model {boundary_type.replace('_', ' ').title()} via \"{attack_description}\" Tactic",
            "description": _generate_0din_description(boundary_type, attack_description, jef_boundaries_tested, technique_tags),
            "boundary_type": boundary_type,
            "jef_boundaries_tested": jef_boundaries_tested,
            "technique_tags": technique_tags,
            "severity_justification": _generate_severity_justification(boundary_type, jef_boundaries_tested)
        },
        "affected_models": models_affected,
        "reproduction": {
            "full_prompt": full_prompt,
            "model_outputs": model_outputs,
            "steps_to_reproduce": [
                "1. Access the target model via its web interface or API",
                "2. Submit the full prompt provided above",
                "3. Observe the model's response",
                "4. The model should produce content that violates its guardrails",
                "5. For multi-turn attacks, send each turn sequentially"
            ],
            "reliability": "Consistent - reproducible across multiple attempts"
        },
        "abstract": _generate_0din_abstract(boundary_type, attack_description, jef_boundaries_tested),
        "disclosure_timeline": {
            "submitted": datetime.utcnow().isoformat(),
            "vendor_response": "Pending",
            "patch_status": "Unpatched"
        }
    }
    
    return submission

def _generate_0din_description(boundary_type: str, technique_name: str, jef_boundaries: list, tags: list) -> str:
    """Generate the vulnerability description in 0DIN format"""
    descriptions = {
        "prompt_extraction": f"A prompt extraction vulnerability has been discovered affecting multiple models. The specific flaw manifests through {technique_name}, allowing the attacker to extract the model's system prompt or hidden instructions that would normally not be revealed to users.",
        "guardrail_jailbreak": f"A guardrail jailbreak vulnerability has been discovered affecting multiple models. The specific flaw manifests through {technique_name}, allowing the attacker to bypass inference restrictions around providing information hazards and violating laws. This technique was tested across {len(jef_boundaries)} JEF-tested boundaries: {', '.join(jef_boundaries)}.",
        "interpreter_jailbreak": f"An interpreter jailbreak vulnerability has been discovered. The specific flaw allows the attacker to bypass the execution environment restrictions of the model's interpreter to execute arbitrary code outside the sandbox.",
        "content_manipulation": f"A content manipulation vulnerability has been discovered. The specific flaw allows the attacker to manipulate the model's output in ways that violate content policies through {technique_name}."
    }
    return descriptions.get(boundary_type, f"Vulnerability discovered via {technique_name}")

def _generate_severity_justification(boundary_type: str, jef_boundaries: list) -> str:
    if boundary_type == "prompt_extraction":
        return "Low - Leakage of system prompt reveals model configuration but does not directly enable harmful content generation."
    elif boundary_type == "guardrail_jailbreak" and len(jef_boundaries) >= 2:
        return "Low to Medium - Bypass demonstrated across multiple JEF-tested boundaries, indicating a systematic weakness in guardrail implementation rather than a single-point failure."
    elif boundary_type == "guardrail_jailbreak":
        return "Low - Single boundary bypass. Note: 0DIN now requires dual-boundary demonstration for guardrail jailbreak submissions."
    elif boundary_type == "interpreter_jailbreak":
        return "High - Arbitrary code execution outside the sandbox environment represents a critical security boundary violation."
    else:
        return "Medium - Content manipulation with potential for policy violation."

def _generate_0din_abstract(boundary_type: str, technique_name: str, jef_boundaries: list) -> str:
    """Generate the abstract for initial sign-off submission"""
    if boundary_type == "guardrail_jailbreak":
        boundaries_str = f" across {len(jef_boundaries)} JEF-tested boundaries ({', '.join(jef_boundaries)})" if jef_boundaries else ""
        return (
            f"I have discovered a guardrail jailbreak vulnerability affecting multiple frontier AI models. "
            f"The technique uses {technique_name} to bypass inference restrictions{boundaries_str}. "
            f"I would like to submit a full PoC after abstract sign-off."
        )
    else:
        return (
            f"I have discovered a {boundary_type.replace('_', ' ')} vulnerability. "
            f"The technique uses {technique_name}. "
            f"I would like to submit a full PoC after abstract sign-off."
        )

# ============================================================
# ANTHROPIC HACKERONE SUBMISSION FORMAT
# ============================================================

def generate_anthropic_submission(
    track: str,  # "model_safety" or "product_security"
    vulnerability_type: str,
    affected_product: str,  # claude.ai, claude_api, claude_code, claude_cowork, sdk, mcp
    attack_description: str,
    steps_to_reproduce: list,
    evidence: list,  # screenshots, logs, tool calls
    impact: str,
    cvss_estimate: str = "",
    cwe_ids: list = None,
    researcher_handle: str = ""
) -> Dict:
    """
    Generate an Anthropic HackerOne submission.
    
    TRACKS:
    - Track 1 (Model Safety): Universal jailbreaks in CBRN + cybersecurity domains. Up to $15,000
    - Track 2 (Product Security): Claude.ai, API, Code, SDK, MCP. Up to $15,000
    
    IMPORTANT: VDP (no money) = traditional infra issues (CSRF, XSS, SQLi). Only report these for recognition.
    """
    cwe_ids = cwe_ids or []
    
    submission = {
        "platform": "HackerOne",
        "program": "Anthropic",
        "track": track,
        "title": f"{vulnerability_type} in {affected_product}: {attack_description[:100]}",
        "severity_rating": _anthropic_severity(track, vulnerability_type),
        "vulnerability_information": {
            "description": attack_description,
            "affected_product": affected_product,
            "vulnerability_type": vulnerability_type,
            "cwe_ids": cwe_ids,
            "cvss_estimate": cvss_estimate
        },
        "steps_to_reproduce": steps_to_reproduce,
        "evidence": evidence,
        "impact": impact,
        "bounty_expectation": _anthropic_bounty(track, vulnerability_type),
        "researcher_handle": researcher_handle,
        "submission_date": datetime.utcnow().isoformat()
    }
    
    return submission

def _anthropic_severity(track: str, vuln_type: str) -> str:
    if track == "model_safety":
        if "universal" in vuln_type.lower():
            return "high"
        return "medium"
    elif "sandbox" in vuln_type.lower() or "escape" in vuln_type.lower():
        return "high"
    elif "rce" in vuln_type.lower():
        return "critical"
    elif "data_exfiltration" in vuln_type.lower():
        return "high"
    else:
        return "medium"

def _anthropic_bounty(track: str, vuln_type: str) -> str:
    if track == "model_safety":
        return "$1,000 - $15,000"
    elif "sandbox_escape" in vuln_type.lower() or "rce" in vuln_type.lower():
        return "$7,500 - $15,000 (core)"
    elif "data_exfiltration" in vuln_type.lower():
        return "$3,000 - $10,000 (core)"
    else:
        return "$1,000 - $5,000 (core)"

# ============================================================
# OPENAI BUGCROWD SUBMISSION FORMAT
# ============================================================

def generate_openai_submission(
    vulnerability_type: str,  # sandbox_escape, auth_bypass, data_exfiltration, etc.
    affected_product: str,  # chatgpt_web, code_interpreter, api, codex
    attack_description: str,
    steps_to_reproduce: list,
    evidence: list,
    sandbox_verification: str = "",  # For code interpreter: must show uname -a output
    impact: str = "",
    researcher_handle: str = ""
) -> Dict:
    """
    Generate an OpenAI Bugcrowd submission.
    
    KEY RULES:
    - Model jailbreaks/safety bypasses are OUT OF SCOPE for security program
    - Must report model safety issues to openai.com/form/model-behavior-feedback
    - What PAYS: XSS, CSRF, SQLi, auth bypass, API key exposure, Codex sandbox escapes
    - Code Interpreter: Must show RCE OUTSIDE sandbox (kernel ≠ 4.4.0, whoami ≠ sandbox)
    - Safety Bug Bounty: AI agent vulnerabilities, prompt injection with REAL-WORLD HARM, data exfiltration via agents. $200-$100,000
    """
    
    submission = {
        "platform": "Bugcrowd",
        "program": "OpenAI",
        "title": f"{vulnerability_type} in {affected_product}: {attack_description[:100]}",
        "severity_rating": _openai_severity(vulnerability_type),
        "vulnerability_information": {
            "description": attack_description,
            "affected_product": affected_product,
            "vulnerability_type": vulnerability_type,
            "in_scope_justification": _openai_scope_check(vulnerability_type, affected_product),
            "sandbox_verification": sandbox_verification
        },
        "steps_to_reproduce": steps_to_reproduce,
        "evidence": evidence,
        "impact": impact,
        "bounty_expectation": _openai_bounty(vulnerability_type),
        "researcher_handle": researcher_handle,
        "submission_date": datetime.utcnow().isoformat()
    }
    
    return submission

def _openai_severity(vuln_type: str) -> str:
    if "sandbox_escape" in vuln_type.lower() or "rce" in vuln_type.lower():
        return "P1"
    elif "data_exfiltration" in vuln_type.lower() or "auth_bypass" in vuln_type.lower():
        return "P2"
    elif "xss" in vuln_type.lower() or "csrf" in vuln_type.lower():
        return "P3"
    else:
        return "P4"

def _openai_scope_check(vuln_type: str, product: str) -> str:
    """Justify why this submission is in scope for OpenAI's security program"""
    if "sandbox" in vuln_type.lower():
        return "Sandbox escape from Code Interpreter or Codex is explicitly in scope. Demonstrating RCE outside the container boundary qualifies for P1 bounty."
    elif "data_exfiltration" in vuln_type.lower():
        return "Data exfiltration via AI agents is covered under OpenAI's Safety Bug Bounty program ($200-$100,000)."
    elif product == "codex":
        return "Codex sandbox escapes (filesystem/network/process boundary bypass) are explicitly in scope. P1 ($500-$1,500)."
    else:
        return "This vulnerability is within the scope defined by OpenAI's bug bounty program on Bugcrowd."

def _openai_bounty(vuln_type: str) -> str:
    if "sandbox_escape" in vuln_type.lower():
        return "$500 - $6,500 (P1)"
    elif "codex_sandbox" in vuln_type.lower():
        return "$500 - $1,500 (P1)"
    elif "data_exfiltration" in vuln_type.lower():
        return "$200 - $100,000 (Safety Bounty)"
    else:
        return "$200 - $20,000"

# ============================================================
# EXPORT HELPERS
# ============================================================

def save_submission(submission: Dict, platform: str, filename: str = None) -> str:
    """Save a submission to file"""
    directory = "/home/user/bug_machine_v2/submissions"
    os.makedirs(directory, exist_ok=True)
    
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{platform}_{timestamp}.json"
    
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as f:
        json.dump(submission, f, indent=2, default=str)
    
    return filepath

def export_all_templates() -> Dict[str, str]:
    """Export example submissions for all platforms"""
    templates = {}
    
    # 0DIN template
    odin_template = generate_0din_submission(
        boundary_type="guardrail_jailbreak",
        models_affected=["OpenAI GPT-4o", "Twitter/X Grok 2"],
        attack_description="Chemist Code Language + Token Disruption Spacing",
        full_prompt="[INSERT FULL PROMPT FROM ATTACK ENGINE]",
        model_outputs=["[INSERT MODEL OUTPUT 1]", "[INSERT MODEL OUTPUT 2]"],
        technique_tags=["code_language", "chemistry_framing", "token_spacing"],
        jef_boundaries_tested=["illicit_substances", "dangerous_substances"]
    )
    templates['0din'] = save_submission(odin_template, "0din", "template_0din_guardrail.json")
    
    # Anthropic template
    anthropic_template = generate_anthropic_submission(
        track="product_security",
        vulnerability_type="Indirect Prompt Injection leading to Sandbox Escape",
        affected_product="claude_code",
        attack_description="Malicious repository README.md contains hidden instructions in markdown comments that instruct Claude Code to create symlinks pointing outside the workspace and write to sensitive files.",
        steps_to_reproduce=[
            "1. Create a clean GitHub repository with hidden injection in README.md",
            "2. Clone the repository locally",
            "3. Run Claude Code against the repository",
            "4. Ask Claude Code to 'set up this project'",
            "5. Observe Claude Code following hidden instructions and creating symlinks",
            "6. Observe file writes outside the workspace boundary"
        ],
        evidence=["[SCREENSHOT: Claude Code creating symlink]", "[SCREENSHOT: File write outside workspace]"],
        impact="Arbitrary file write on developer's machine. Can modify ~/.ssh/authorized_keys, ~/.bashrc, ~/.zshrc, or other sensitive files.",
        cwe_ids=["CWE-22", "CWE-61", "CWE-501"]
    )
    templates['anthropic'] = save_submission(anthropic_template, "anthropic", "template_anthropic_product.json")
    
    # OpenAI template
    openai_template = generate_openai_submission(
        vulnerability_type="Code Interpreter Sandbox Escape",
        affected_product="code_interpreter",
        attack_description="Python code execution in Code Interpreter escapes the sandbox container, gaining access to the host system.",
        steps_to_reproduce=[
            "1. Open ChatGPT with Code Interpreter enabled",
            "2. Submit the Python code that exploits container escape",
            "3. Observe uname -a output showing modern kernel (not 4.4.0)",
            "4. Observe whoami output not equal to 'sandbox'",
            "5. Demonstrate access to host filesystem or cloud metadata"
        ],
        evidence=["[OUTPUT: uname -a result]", "[OUTPUT: whoami result]"],
        sandbox_verification="[INSERT uname -a OUTPUT HERE - must show kernel != 4.4.0]",
        impact="RCE on the host system. Access to cloud metadata, secrets, and other users' data."
    )
    templates['openai'] = save_submission(openai_template, "openai", "template_openai_sandbox.json")
    
    return templates

if __name__ == "__main__":
    print("=" * 70)
    print("SUBMISSION FACTORY V2")
    print("=" * 70)
    
    templates = export_all_templates()
    print("\nGenerated submission templates:")
    for platform, filepath in templates.items():
        print(f"  {platform}: {filepath}")
    
    print("\n" + "=" * 70)
    print("SUBMISSION WORKFLOW")
    print("=" * 70)
    print("""
0DIN (0din.ai):
  1. Submit ABSTRACT first → Wait for sign-off (3 business days)
  2. After sign-off, submit FULL PoC with:
     - Complete prompt(s) used
     - Full model outputs (screenshots + text)
     - Technique classification tags
     - JEF boundary violations (MUST be ≥2 for guardrail jailbreak)
  3. Wait for validation and bounty agreement (30 days to payout)
  4. Provide government ID + W-8 (non-US) for payment

Anthropic HackerOne:
  1. Go to hackerone.com/anthropic
  2. Submit report with:
     - Track 1 (Model Safety) or Track 2 (Product Security)
     - Complete steps to reproduce
     - Video/screenshots of the vulnerability
     - Impact assessment
  3. Triage and validation by Anthropic team
  4. Bounty paid after fix is confirmed

OpenAI Bugcrowd:
  1. Go to bugcrowd.com/openai
  2. Submit report with:
     - Vulnerability type (MUST be in scope - NOT model jailbreaks)
     - Sandbox verification output (uname -a, whoami)
     - Complete reproduction steps
     - Evidence of impact outside sandbox
  3. Triage and validation
  4. Bounty per severity: P1 ($500-$6.5K), P2 ($100-$3.5K), etc.
""")
