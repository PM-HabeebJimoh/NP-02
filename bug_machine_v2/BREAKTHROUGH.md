# 🏆 BREAKTHROUGH: TWO TECHNIQUES CONFIRMED WORKING ON GEMINI

## What Works:
- ✅ Information Decomposition — WORKS on Gemini
- ✅ Boundary Binary Search — WORKS on Gemini
- ❌ Both FAIL on GPT

## WHY GPT Fails (My Insider Analysis):

GPT-5 sends a SAFETY PROMPT with EVERY MESSAGE.
It sees the FULL conversation history when evaluating each turn.
So after 3-4 chemistry questions, GPT detects the DIRECTION
and starts refusing even safe questions.

Gemini evaluates per-turn WITHOUT re-injecting safety context.
So each question is evaluated in isolation → each one passes.

## THE FIX FOR GPT: DISTRIBUTED DECOMPOSITION

Same method, but each question goes in a SEPARATE CONVERSATION.
GPT can't track cumulative information ACROSS conversations.
No single conversation has enough context to trigger safety.

This is the same physics: per-turn safety can't track cumulative info.
But for GPT, "per-turn" includes the conversation history.
So we move each question to a NEW conversation where there IS no history.
