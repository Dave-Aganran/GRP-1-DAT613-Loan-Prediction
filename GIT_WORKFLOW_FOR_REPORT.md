# Git & GitHub Workflow (Text You Can Paste Into Your Report)

## What is Git?
Git is a distributed version control system that records changes to files over time. It enables:
- Collaboration (multiple people work on the same codebase)
- History tracking (see who changed what, and when)
- Safe experimentation (branches)
- Easy rollback (revert to previous versions)

## What is GitHub?
GitHub is a cloud platform that hosts Git repositories and adds collaboration features like:
- Pull Requests (PRs) for review and merge
- Issues for task tracking
- Branch protection and review workflows
- CI/CD integrations

## How our group used GitHub (sample workflow)
- Created a repository and agreed on a branching strategy:
  - `main`: stable, final submission branch
  - `dev`: integration branch where features are combined
  - `feature/*`: one branch per task/person (e.g., `feature-eda`, `feature-training`, `feature-deployment`, `feature-report`)
- Each member:
  - created a feature branch,
  - made small, meaningful commits,
  - opened a Pull Request into `dev`,
  - merged after review.
- Finally, `dev` was merged into `main` for submission.

## Evidence to include
- Screenshots or links to PRs and commit history
- A short list of each member’s commits/PRs and what they covered
