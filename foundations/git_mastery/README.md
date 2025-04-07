# Git Mastery & Collaboration Flow

## 1. Branching Strategies

**Theory:**

- Branching allows you to work on different features or bug fixes in isolation.
- **Gitflow:** A strict branching model with `develop`, `release`, and `hotfix` branches.
- **GitHub Flow:** A simpler model with a `main` branch and feature branches.
- **Creating a branch:** `git checkout -b feature/my-feature`
- **Switching branches:** `git checkout main`
- **Deleting a branch:** `git branch -d feature/my-feature`

**Example:**

- Create a `feature/login` branch to implement a login feature.
- Create a `bugfix/issue-123` branch to fix a bug.

**Exercise:**

- Create a repository and experiment with different branching strategies.
- Create a feature branch, make changes, and merge it back into the main branch.
- Create a bugfix branch, fix a bug, and merge it back into the main branch.

## 2. Merging vs. Rebasing:

**Theory:**

- **Merging:** Creates a new commit that combines changes from two branches. Preserves history.
- **Rebasing:** Rewrites the commit history by moving commits from one branch onto another. Creates a linear history.
- **Merging:** `git merge feature/my-feature`
- **Rebasing:** `git rebase main` (while on feature/my-feature branch)

**Example:**

- Merge a feature branch into the main branch.
- Rebase a feature branch onto the main branch to create a cleaner history.

**Exercise:**

- Create a repository with multiple branches and experiment with merging and rebasing.
- Observe the differences in the commit history.
- Practice resolving merge conflicts.

## 3. Pull Requests:

**Theory:**

- Pull requests (PRs) are a way to propose changes to a repository.
- They allow for code reviews and discussions before merging.
- **Creating a PR:** Push your branch to a remote repository and create a PR on GitHub/GitLab.
- **Reviewing a PR:** Provide feedback and approve or reject the changes.

**Example:**

- Create a PR for a feature branch.
- Review a PR from a colleague.

**Exercise:**

- Create a repository on GitHub/GitLab and practice creating and reviewing PRs.
- Use code review tools to provide feedback.
- Practice resolving merge conflicts in a PR.

## 4. Code Reviews:

**Theory:**

- Code reviews help to improve code quality and catch bugs.
- Provide constructive feedback and focus on code quality, not personal preferences.
- Be respectful and open to feedback.

**Example:**

- Review a colleague's code and provide feedback on code style, logic, and potential issues.

**Exercise:**

- Practice performing code reviews on open-source projects or your own code.
- Use code review checklists to ensure thorough reviews.
- Practice giving and receiving constructive feedback.

## 5. GitHub/GitLab:

**Theory:**

- GitHub and GitLab are popular platforms for Git repositories and collaboration.
- They provide features like issue tracking, pull requests, and CI/CD.
- **Managing repositories:** Create, clone, and manage repositories.
- **Using issues:** Track bugs and feature requests.
- **Using pull requests:** Propose and review changes.

**Example:**

- Create a repository on GitHub and collaborate with a colleague.
- Use issues to track bugs and feature requests.
- Create and review pull requests.

**Exercise:**

- Explore the features of GitHub/GitLab and practice using them.
- Contribute to an open-source project.
- Create a project and use GitHub/GitLab for collaboration.
