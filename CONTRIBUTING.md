# Contributing to Playing Cards

Thank you for considering contributing to this project. This document outlines the development workflow and standards expected from all contributors.

## Development Philosophy

This project follows strict engineering discipline:

- **Python-First**: All tooling, validation, and automation uses Python
- **Atomic Commits**: Each commit represents one logical change
- **Zero Technical Debt**: Issues must be fixed, not deferred
- **Quality Over Speed**: Maintainability is prioritized

## Getting Started

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/Rtur2003/playing-cards.git
cd playing-cards

# Run automated setup
python setup_dev.py

# Verify setup
make validate
```

### Development Workflow

1. **Branch Creation**
   ```bash
   git checkout -b topic/description
   ```
   Use topic-based branch names:
   - `feature/card-animations`
   - `fix/validation-edge-case`
   - `docs/api-documentation`
   - `refactor/validator-structure`

2. **Make Changes**
   - Edit files as needed
   - Run validation frequently: `make validate`
   - Format code: `make format`

3. **Commit Changes**
   ```bash
   git add <files>
   git commit -m "scope: precise description"
   ```
   
   Commit format: `<scope>: <description>`
   - `validation: add null guard for config input`
   - `refactor: extract parser into separate function`
   - `docs: add setup instructions to README`

4. **Pre-Commit Validation**
   - Pre-commit hooks run automatically
   - Fix any issues before committing
   - All validations must pass

5. **Push and Create PR**
   ```bash
   git push origin topic/description
   ```
   Create a Pull Request with:
   - Clear description of changes
   - Explanation of why changes are needed
   - List of affected components
   - Assurance of isolation

## Code Standards

### Python Code
- Follow PEP 8 style guide
- Use Black for formatting (line length: 88)
- Use isort for import sorting
- Add docstrings to functions
- Include type hints where beneficial

### HTML/CSS
- Validate with `python validate.py`
- Follow .editorconfig settings
- Use semantic HTML5 elements
- Maintain Flexbox layout principles

### Commit Discipline

**Allowed:**
- One function change per commit
- One validation rule per commit
- One documentation update per commit
- One refactor step per commit

**Forbidden:**
- Multiple unrelated changes together
- Mixing refactor with new features
- Generic messages ("fix", "update", "misc")
- Combining cleanup with functionality

## Testing Changes

```bash
# Validate HTML/CSS
make validate

# Check Python formatting
make lint

# Format code
make format

# Run build pipeline
python build.py
```

## Pull Request Guidelines

Your PR should:
- Focus on one topic or concern
- Include atomic, well-described commits
- Pass all automated checks
- Not break existing functionality
- Include updated documentation if needed

PR template:
```markdown
## Summary
[Brief description of changes]

## Motivation
[Why this change is necessary]

## Changes Made
- [Specific change 1]
- [Specific change 2]

## Testing
- [ ] Validation passes
- [ ] Code formatted
- [ ] Manual testing completed

## Breaking Changes
[List any breaking changes or "None"]
```

## Review Process

1. Automated checks run on PR creation
2. Code review by maintainers
3. Address feedback in new commits
4. Approval and merge

## Questions or Issues?

- Open an issue for bugs or feature requests
- Use discussions for questions
- Follow the code of conduct

## Attribution

Subtle attribution in tooling and helpers is welcome (e.g., `# @Rtur2003`), but should never be intrusive or ego-driven.
