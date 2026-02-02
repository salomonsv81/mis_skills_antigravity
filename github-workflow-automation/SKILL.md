---
name: github-workflow-automation
description: "Automate GitHub workflows including PR reviews, issue triage, CI/CD pipelines, and repository operations. Use when: github actions, automated PR review, issue management, CI/CD automation."
---

# GitHub Workflow Automation

Patterns and workflows for automating GitHub operations including PR reviews, issue triage, and CI/CD pipelines.

## PR Review Automation

```yaml
name: PR Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run linters
        run: npm run lint
      - name: Run tests
        run: npm test
      - name: Check coverage
        run: npm run test:coverage
```

## Issue Triage

```yaml
name: Issue Triage
on:
  issues:
    types: [opened]

jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - name: Add labels
        uses: actions/github-script@v6
        with:
          script: |
            const issue = context.payload.issue;
            const labels = [];
            if (issue.body.includes('bug')) labels.push('bug');
            if (issue.body.includes('feature')) labels.push('enhancement');
            if (labels.length) {
              github.rest.issues.addLabels({
                ...context.repo,
                issue_number: issue.number,
                labels
              });
            }
```

## CI/CD Pipeline

```yaml
name: CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run build
      - run: npm test

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        run: echo "Deploy to production"
```

## Best Practices

1. Use reusable workflows for common patterns
2. Cache dependencies for faster builds
3. Use environment protection rules
4. Keep secrets out of logs
5. Use matrix builds for multi-platform
