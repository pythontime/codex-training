# Model Selection Guide

Choose the right model for your task based on cost, speed, and capability.

---

## Quick Reference

| Model | Best For | Speed | Cost | Context |
|-------|----------|-------|------|---------|
| **GPT-5.2-Codex** | Complex refactoring, architecture | Slower | $$$ | 128K |
| **GPT-5-Codex** | General coding, reviews | Medium | $$ | 128K |
| **GPT-5-Codex-Mini** | Quick tasks, high volume | Fast | $ | 128K |
| **GPT-5.1-Codex-Max** | Large projects, long sessions | Slow | $$$$ | 1M |
| **Claude Sonnet 4** | Alternative perspective | Medium | $$ | 200K |
| **Ollama (local)** | Privacy, offline, free | Varies | Free | Varies |

---

## Model Details

### GPT-5.2-Codex (Default)

**Use when:**
- Complex architectural decisions
- Multi-file refactoring
- Security-critical code review
- Production deployments

**Avoid when:**
- Simple formatting fixes
- High-volume repetitive tasks
- Cost is a primary concern

```bash
codex --model gpt-5.2-codex "Refactor authentication to use OAuth2"
```

### GPT-5-Codex

**Use when:**
- Day-to-day coding tasks
- Code reviews
- Test generation
- Documentation

**Sweet spot:** Best balance of capability and cost for most tasks.

```bash
codex --model gpt-5-codex "Add unit tests for UserService"
```

### GPT-5-Codex-Mini

**Use when:**
- Simple fixes and formatting
- Rapid iteration
- Learning and experimentation
- CI/CD pipelines (cost control)
- High volume tasks

**Avoid when:**
- Complex multi-step reasoning
- Security-sensitive analysis

```bash
codex --model gpt-5-codex-mini "Fix the typo in line 42"
```

**Pro tip:** 4x more usage at same cost as standard model.

### GPT-5.1-Codex-Max

**Use when:**
- Entire codebase analysis
- Long-running sessions (hours)
- Project-scale refactoring
- Large context needed (1M tokens)

**Avoid when:**
- Quick tasks (overkill)
- Cost-sensitive projects

```bash
codex --model gpt-5.1-codex-max "Analyze this entire microservices repo"
```

### Anthropic Claude

**Use when:**
- Want a second opinion
- Prefer Claude's style
- Cross-referencing responses

```toml
# In config.toml
[providers.anthropic]
type = "anthropic"
api_key = "${ANTHROPIC_API_KEY}"
model = "claude-sonnet-4-20250514"
```

### Local Models (Ollama)

**Use when:**
- Working with sensitive/proprietary code
- No internet connection
- Cost must be zero
- Privacy requirements

**Trade-offs:**
- Slower than cloud models
- Less capable for complex tasks
- Requires local GPU for best performance

```toml
# In config.toml
[providers.ollama]
type = "ollama"
base_url = "http://localhost:11434"
model = "codellama:34b"
```

---

## Cost Optimization Strategies

### 1. Use Profiles

```toml
# config.toml
[profiles.quick]
model = "gpt-5-codex-mini"
approval_policy = "never"

[profiles.thorough]
model = "gpt-5.2-codex"
approval_policy = "on-request"
```

```bash
codex --profile quick "Fix formatting"
codex --profile thorough "Security audit"
```

### 2. Be Specific in Prompts

```bash
# Expensive: vague, generates lots of output
codex "Review this file"

# Cheaper: specific, focused output
codex "Check line 50-60 for null pointer issues"
```

### 3. Reduce Context Size

```toml
# Smaller AGENTS.md = fewer tokens
project_doc_max_bytes = 16384  # 16KB instead of 32KB
```

### 4. Use Mini for CI/CD

```yaml
# In GitHub Actions
codex exec "..." --model gpt-5-codex-mini
```

---

## Decision Flowchart

```
Is this a quick fix or formatting?
├─ Yes → GPT-5-Codex-Mini
└─ No
   │
   Is this security/production critical?
   ├─ Yes → GPT-5.2-Codex
   └─ No
      │
      Does it need huge context (>128K)?
      ├─ Yes → GPT-5.1-Codex-Max
      └─ No
         │
         Is cost a concern?
         ├─ Yes → GPT-5-Codex-Mini
         └─ No → GPT-5-Codex
```

---

## Monitoring Usage

```bash
# Check API usage (OpenAI dashboard)
open https://platform.openai.com/usage

# Enable logging to track token usage
[logging]
level = "info"
file = "~/.codex/log/codex.log"
```

---

## Recommendations by Task

| Task | Recommended Model |
|------|-------------------|
| Fix typos, formatting | Mini |
| Add comments/docs | Mini |
| Simple bug fixes | Mini |
| Unit test generation | Standard |
| Code review | Standard |
| Refactoring | Standard or 5.2 |
| Architecture design | 5.2-Codex |
| Security audit | 5.2-Codex |
| Full codebase analysis | 5.1-Codex-Max |
| CI/CD automation | Mini |
| Learning/experimenting | Mini |
