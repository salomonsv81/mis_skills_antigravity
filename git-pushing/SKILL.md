---
name: git-pushing
description: "Proper Git staging, commit, and push workflow with conventional commits. Use when: committing code, pushing changes, git workflow, conventional commits."
---

# Git Push Workflow

Standard workflow for staging, committing, and pushing changes to Git repositories.

## Commit Message Format

Use conventional commits:
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `style:` formatting
- `refactor:` code change without feature/fix
- `test:` adding tests
- `chore:` maintenance

## Workflow

```bash
# 1. Stage changes
git add -A

# 2. Commit with conventional message
git commit -m "feat: add user authentication"

# 3. Push to remote
git push origin main
```

## Best Practices

1. Check `git status` before committing
2. Write clear, descriptive commit messages
3. Keep commits focused and atomic
4. Pull before pushing to avoid conflicts
5. Use branches for features
