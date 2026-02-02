---
name: systematic-debugging
description: "Methodical debugging approach focusing on root cause analysis instead of random fixes. Use when: debugging errors, finding root cause, fixing bugs systematically."
---

# Systematic Debugging

A structured approach to debugging that finds root causes instead of applying random fixes.

## Phase 1: Root Cause Investigation

1. **Reproduce the issue** consistently
2. **Isolate the problem** - identify exact component/function
3. **Gather evidence** - logs, stack traces, state
4. **Form hypothesis** about the cause

## Phase 2: Pattern Analysis

1. When does it fail? (timing, input, state)
2. What changed recently?
3. Are there related issues?
4. What does the error message actually say?

## Phase 3: Hypothesis Testing

1. **Test ONE change at a time**
2. Verify hypothesis with minimal reproduction
3. Document what you learned
4. If wrong, revert and try next hypothesis

## Phase 4: Implementation

1. Apply minimal fix to root cause
2. Add tests to prevent regression
3. Document the fix
4. Verify in all affected scenarios

## Anti-Patterns to Avoid

- ❌ Changing multiple things at once
- ❌ Fixing symptoms instead of causes
- ❌ Ignoring error messages
- ❌ Not testing after fixing
- ❌ Assuming without evidence

## Key Principles

> "If repeated fixes fail, question the architecture."

1. Understand before fixing
2. Evidence over assumptions
3. One change at a time
4. Root cause over symptoms
5. Prevent future occurrences
