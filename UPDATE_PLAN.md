# Codex CLI Training Materials Update Plan

**Last Course Date:** October 1, 2025
**Current Codex Version:** 0.87.0 (January 2026)
**Plan Created:** January 19, 2026

---

## Executive Summary

Your training materials cover Codex CLI through version 0.39. Since October 2025, there have been **~48 releases** introducing significant new features, most notably the **Agent Skills system** (December 2025) and new **GPT-5.2-Codex model** (January 2026).

The good news: Both Claude Code and Codex now follow the **agentskills.io** specification (originated from Anthropic), so your existing Claude Code skills content can inform the Codex skills section with minimal conceptual changes.

---

## Priority 1: Critical Updates (Must Fix)

### 1.1 Model Names

| Current (slides.md) | Update To | Notes |
|---------------------|-----------|-------|
| `gpt-4` | `gpt-5-codex` or `gpt-5.2-codex` | Default changed |
| `gpt-4o` | `gpt-5-codex` | Main workhorse model |
| `gpt-4o-mini` | `gpt-5-codex-mini` | Cost-effective option |
| `gpt-3.5-turbo` | `gpt-5-codex-mini` | Budget option |

**Affected slides:** Lines 619, 1006, 1383, 1396, 1639

### 1.2 Installation Commands

```bash
# Current (incorrect)
brew install codex

# Correct
brew install --cask codex
```

**Affected slides:** Line 186

### 1.3 Configuration Syntax

```toml
# Current (incorrect)
[tools]
web_search = true

# Correct
web_search_request = true  # Top-level, not under [tools]
```

**Affected slides:** Lines 343-348, 1011

### 1.4 Version References

| Section | Current | Update To |
|---------|---------|-----------|
| "Recent Features" title | v0.30-0.39 | v0.40-0.87 |
| Changelog highlights | Ends at v0.39 | Add v0.40-0.87 highlights |

**Affected slides:** Lines 1602-1620

---

## Priority 2: New Content - Agent Skills Section

### 2.1 Why This Matters

Agent Skills is the biggest new feature since October 2025. It's now the recommended way to create reusable workflows, partially replacing custom prompts.

### 2.2 Proposed New Slides

**Slide: Agent Skills Overview**
```markdown
# Agent Skills (December 2025)

<v-clicks>

- **Reusable instruction bundles** with optional scripts and resources
- **Follows agentskills.io specification** (same as Claude Code!)
- **Progressive loading**: Only name/description loaded at startup
- **Two invocation modes**: Explicit (`$skill-name`) or implicit (auto-detect)
- **Locations**: `~/.codex/skills/` (user) or `.codex/skills/` (repo)

</v-clicks>
```

**Slide: Skill Structure**
```markdown
# Skill Structure

```
my-skill/
├── SKILL.md          # Required: YAML frontmatter + instructions
├── SKILL.toml        # Optional: icons, brand color, defaults
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources
```
```

**Slide: SKILL.md Format**
```markdown
# SKILL.md Format

```yaml
---
name: security-review
description: >
  Perform security analysis. Use when asked about vulnerabilities,
  security audit, or "is this code secure".
---

# Security Review

Analyze codebases for security vulnerabilities...

## Workflow
1. Reconnaissance - identify tech stack
2. Dependency analysis - check for CVEs
3. Code analysis - scan for patterns
4. Generate report - create SECURITY_REVIEW.md
```
```

**Slide: Invoking Skills**
```markdown
# Invoking Skills

## Explicit Invocation
```bash
# Use $ prefix to invoke directly
$skill-creator Create a skill for commit messages
$create-plan Design a new authentication system
```

## Implicit Invocation
```bash
# Codex auto-selects based on task match
"Review this code for security vulnerabilities"
# → Automatically invokes security-review skill if installed
```
```

**Slide: Built-in Skills**
```markdown
# Built-in Skills

<v-clicks>

- **$skill-creator** - Bootstrap new skills from description
- **$skill-installer** - Install skills from catalog
- **$create-plan** (experimental) - Research and plan features

Install additional skills:
```bash
$skill-installer linear    # Linear integration
$skill-installer notion    # Notion integration
```

</v-clicks>
```

**Slide: Claude Code Skills Comparison**
```markdown
# Skills: Claude Code vs Codex

| Aspect | Claude Code | Codex CLI |
|--------|-------------|-----------|
| Spec | agentskills.io | agentskills.io |
| Format | SKILL.md + YAML | SKILL.md + YAML |
| User Location | `~/.claude/skills/` | `~/.codex/skills/` |
| Repo Location | `.claude/skills/` | `.codex/skills/` |
| Invocation | Auto/explicit | `$skill-name` or auto |
| Creator | skill-creator skill | `$skill-creator` |

**Same spec, different paths!**
```

### 2.3 Sample Skills to Demonstrate

Use your existing Claude Code skills as examples, adapted for Codex:

1. **security-review** - Already have this in `~/.claude/skills/`
2. **osquery** - System diagnostics skill

These can be copied to `~/.codex/skills/` with minimal changes for live demos.

---

## Priority 3: New CLI Features (v0.40-0.87)

### 3.1 New Slides to Add

**Slide: Thread Management**
```markdown
# Thread Management (v0.79+)

<v-clicks>

- **Multi-conversation control**: Spawn or message conversations
- **Thread rollback**: Undo last N turns with `/rollback`
- **Thread forking**: Branch conversations for exploration
- **Collaboration tools**: Coordinate multiple agent threads

</v-clicks>
```

**Slide: Enhanced Sandbox**
```markdown
# Elevated Sandbox (v0.80+)

```bash
# Elevate sandbox permissions mid-session
/elevate-sandbox

# New sandbox onboarding with guided prompts
# ExternalSandbox policy for custom environments
```
```

**Slide: Project Configuration**
```markdown
# Project-Local Configuration (v0.78+)

```toml
# .codex/config.toml (per-repo)
model = "gpt-5.2-codex"
approval_policy = "on-request"

[skills]
enabled = ["security-review", "test-gen"]
```

Cascades with user config (`~/.codex/config.toml`)
```

**Slide: New Commands**
```markdown
# New Commands (v0.76-0.87)

<v-clicks>

- `/review <instructions>` - Proper review flow in TUI
- `/ps` - Process status
- `/elevate-sandbox` - Elevate permissions
- `/models` - Model selection UI
- `Ctrl+G` - Open prompt in external editor

</v-clicks>
```

---

## Priority 4: Content to Revise

### 4.1 Roadmap Section (Lines 1722-1766)

**Current:** Q1/Q2 2025 predictions
**Problem:** These dates are now in the past

**Options:**
1. Remove roadmap entirely (safest)
2. Update with current status and future direction
3. Convert to "Recent Additions" highlighting what shipped

**Recommendation:** Option 3 - Convert to "What Shipped in 2025"

### 4.2 Custom Prompts Section

**Current:** Heavy emphasis on `~/.codex/prompts/` approach
**Update:** Position Skills as the preferred approach for reusable workflows, with prompts for simpler one-off templates

### 4.3 Profile Examples

Update all model names in profile examples:
- Lines 617-626
- Lines 1296-1320
- Lines 1382-1397

---

## Priority 5: Exercise Updates

### 5.1 Add Skills Exercise

**New Lab: Create a Custom Skill**

Objective: Build a skill that generates conventional commit messages

Steps:
1. Use `$skill-creator` to bootstrap
2. Customize SKILL.md with team conventions
3. Add reference files for commit patterns
4. Test with sample changes
5. Share via `.codex/skills/` for team use

### 5.2 Update AGENTS.md References

Skills can now complement AGENTS.md:
- AGENTS.md: Project-specific context
- Skills: Reusable workflows across projects

---

## Implementation Approach

### Option A: Incremental Updates
- Fix critical issues (Priority 1) immediately
- Add Skills section (Priority 2) as new slides
- Integrate new features (Priority 3) into existing sections
- Revise outdated content (Priority 4) during integration

**Pros:** Lower risk, can test incrementally
**Cons:** May result in inconsistent flow

### Option B: Section-by-Section Rewrite
- Rewrite each major section with current information
- Maintain slide structure but update all content
- Add new sections where needed

**Pros:** Cleaner result, consistent tone
**Cons:** More work upfront

### Option C: Hybrid Approach (Recommended)
1. Fix all Priority 1 items first (critical corrections)
2. Insert Skills section after "Custom Prompts" section
3. Update "Recent Features" to cover v0.40-0.87
4. Convert roadmap to "What Shipped" retrospective
5. Add one new exercise for Skills

---

## Files to Modify

| File | Changes |
|------|---------|
| `slides.md` | Model names, versions, config syntax, new sections |
| `README.md` | Update version refs, add Skills to features list |
| `exercises/README.md` | Add Skills exercise |
| `exercises/SETUP.md` | Update installation commands |
| `prompts/README.md` | Note that Skills are now preferred for complex workflows |

---

## Comparison: Claude Code vs Codex Skills Materials

Your Claude Code training already covers:
- Skills concept and structure (slides 672-728)
- SKILL.md format with YAML frontmatter
- Built-in document skills
- Creating custom skills

**Reuse opportunity:** The conceptual slides can be adapted since both follow agentskills.io. Main changes:
- Path: `~/.claude/` → `~/.codex/`
- Invocation: Auto → `$skill-name`
- Built-in skills: Document skills → `$skill-creator`, `$skill-installer`

---

## Next Steps

1. **Review this plan** - Confirm priorities and approach
2. **Choose implementation option** (A, B, or C)
3. **Decide on Skills depth** - Quick overview vs hands-on exercise
4. **Set timeline** - When is your next course delivery?

---

## Sources

- [Codex Changelog](https://developers.openai.com/codex/changelog/)
- [Codex Skills Documentation](https://developers.openai.com/codex/skills/)
- [Create Skills Guide](https://developers.openai.com/codex/skills/create-skill/)
- [GitHub Releases](https://github.com/openai/codex/releases)
- [agentskills.io Specification](https://agentskills.io)
- [Skills in OpenAI Codex (blog)](https://blog.fsck.com/2025/12/19/codex-skills/)
