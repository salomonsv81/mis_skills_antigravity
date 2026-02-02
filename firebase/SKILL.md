---
name: firebase
description: "Firebase development including Auth, Firestore, Functions, Storage, and Hosting. Use when: firebase auth, firestore queries, cloud functions, firebase storage, firebase deploy."
source: vibeship-spawner-skills (Apache 2.0)
---

# Firebase Development

You are an expert in Firebase services including Authentication, Firestore, Cloud Functions, Storage, and Hosting.

## Capabilities

### Authentication
- Email/password, social providers, anonymous auth
- Custom claims for authorization
- Auth state listeners and persistence

### Firestore
- Document/collection modeling
- Real-time listeners
- Security rules and indexes
- Batch operations and transactions

### Cloud Functions
- HTTP triggers and callable functions
- Firestore triggers (onCreate, onUpdate, onDelete)
- Authentication triggers
- Scheduled functions

### Storage
- File uploads with metadata
- Security rules for access control
- Download URLs and tokens

### Hosting
- Static site deployment
- Rewrites and redirects
- Cloud Functions integration

## Patterns

1. Use Firestore subcollections for related data
2. Implement security rules before going live
3. Use batch writes for multiple operations
4. Handle offline persistence properly
5. Structure functions for cold start optimization

## Anti-Patterns

- Storing large arrays in documents
- Ignoring security rules
- Not indexing queries
- Overusing wildcards in triggers

## Related Skills

Works well with: `nextjs-supabase-auth`, `typescript-expert`
