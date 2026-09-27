# OpalGross2 — Multimodal AI Engineering & Creation Agent

General-purpose, tool-using AI engineering agent scaffold built around supervised capability data.

## Architecture
- `agent/`: planning, policy, verification, state, tool registry
- `skills/`: web, 3D, motion, full-stack, programming, AI research, multimodal, design
- `training/`: dataset normalization and supervised-data preparation
- `evals/`: regression tests
- `api/`: provider-neutral inference API
- `docs/`: architecture and runbooks

The runtime is provider-neutral and verification-first. Consequential external actions require explicit authorization and security controls are never bypassed.