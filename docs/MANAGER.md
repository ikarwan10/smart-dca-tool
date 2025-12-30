# Project Manager Guide
## Smart DCA Investment Tool - Development Management

---

### Document Information
- **Project:** Smart DCA Investment Tool
- **Manager:** Project Lead
- **Created:** December 30, 2025
- **Status:** 🟢 Active Development
- **Repository:** Pending Git Setup (see Setup Instructions below)

---

## 1. Project Overview

### 1.1 Vision
Build a web-based Dollar Cost Averaging tool that helps investors systematically deploy capital based on Tom Lee's DCA strategy principles.

### 1.2 Key Documents
| Document | Location | Purpose |
|----------|----------|---------|
| Product Requirements | [DCA_Tool_PRD.md](../DCA_Tool_PRD.md) | Full product specification |
| UX Design | [DCA_Tool_UX_Design.md](../DCA_Tool_UX_Design.md) | Visual design specification |
| Backlog | [BACKLOG.md](BACKLOG.md) | All user stories and tasks |
| Dashboard | [DASHBOARD.md](DASHBOARD.md) | Progress tracking |
| Sprint Planning | [SPRINTS.md](SPRINTS.md) | Sprint details and goals |

### 1.3 Technology Stack Decision
| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Backend** | Python + Flask | Simple, fast development, excellent finance libraries |
| **Frontend** | HTML/CSS/JavaScript + Jinja2 | Integrated with Flask, no separate build step |
| **Database** | SQLite | Simple, file-based, perfect for personal use |
| **Stock Data** | yfinance | Free, reliable, no API key needed |
| **Charts** | Chart.js | Lightweight, beautiful charts |
| **CSS Framework** | Tailwind CSS (CDN) | Rapid UI development, matches UX spec |

---

## 2. Team Structure

### 2.1 Roles (Solo/Small Team)
```
┌─────────────────────────────────────────────────────────┐
│                    PROJECT MANAGER                       │
│              (Planning, Tracking, Reviews)               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  Backend    │  │  Frontend   │  │    QA       │     │
│  │  Developer  │  │  Developer  │  │   Tester    │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 2.2 Responsibilities Matrix (RACI)
| Task | Manager | Backend | Frontend | QA |
|------|---------|---------|----------|-----|
| Sprint Planning | R/A | C | C | I |
| Architecture | A | R | C | I |
| API Development | I | R/A | I | C |
| UI Development | I | C | R/A | C |
| Testing | A | C | C | R |
| Code Review | R/A | R | R | I |
| Deployment | A | R | C | C |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

---

## 3. Development Workflow

### 3.1 Git Workflow (GitFlow Lite)
```
main (production)
  │
  └── develop (integration)
        │
        ├── feature/DCA-001-portfolio-model
        ├── feature/DCA-002-price-fetcher
        ├── feature/DCA-003-dashboard-ui
        └── bugfix/DCA-010-calculation-error
```

### 3.2 Branch Naming Convention
```
feature/DCA-{ticket#}-{short-description}
bugfix/DCA-{ticket#}-{short-description}
hotfix/DCA-{ticket#}-{short-description}
```

### 3.3 Commit Message Format
```
[DCA-{ticket#}] {type}: {short description}

{detailed description if needed}

Types: feat, fix, docs, style, refactor, test, chore
```

**Examples:**
```
[DCA-001] feat: Add portfolio data model
[DCA-005] fix: Correct ATH calculation for split-adjusted prices
[DCA-012] docs: Update API documentation
```

### 3.4 Pull Request Process
1. ✅ Create feature branch from `develop`
2. ✅ Implement feature with tests
3. ✅ Self-review code
4. ✅ Create PR with description template
5. ✅ Request review
6. ✅ Address feedback
7. ✅ Merge to `develop` (squash)
8. ✅ Delete feature branch

### 3.5 PR Description Template
```markdown
## Summary
Brief description of changes

## Related Ticket
DCA-XXX

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Documentation
- [ ] Refactoring

## Testing Done
- [ ] Unit tests added/updated
- [ ] Manual testing completed
- [ ] Edge cases considered

## Screenshots (if UI changes)
[Attach screenshots]

## Checklist
- [ ] Code follows project style guide
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No console errors/warnings
```

---

## 4. Sprint Process

### 4.1 Sprint Cadence
| Event | Frequency | Duration | Participants |
|-------|-----------|----------|--------------|
| Sprint | 1 week | 5 working days | All |
| Planning | Start of sprint | 1 hour | All |
| Daily Standup | Daily | 15 min | All |
| Review | End of sprint | 30 min | All |
| Retrospective | End of sprint | 30 min | All |

### 4.2 Sprint Ceremonies

#### Sprint Planning (Monday)
1. Review backlog priorities
2. Select stories for sprint
3. Break down into tasks
4. Estimate effort (hours)
5. Commit to sprint goal

#### Daily Standup
Three questions:
1. What did I complete yesterday?
2. What will I work on today?
3. Any blockers?

#### Sprint Review (Friday)
1. Demo completed features
2. Gather feedback
3. Update backlog if needed

#### Retrospective (Friday)
1. What went well?
2. What could improve?
3. Action items for next sprint

### 4.3 Definition of Done (DoD)
A story is "Done" when:
- [ ] Code complete and committed
- [ ] Unit tests written and passing
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] No critical bugs
- [ ] Works on local environment
- [ ] Merged to develop branch

---

## 5. Quality Standards

### 5.1 Code Quality
- **Python Style:** PEP 8 compliance
- **Docstrings:** All public functions documented
- **Type Hints:** Use Python type hints
- **Test Coverage:** Minimum 70% for core logic

### 5.2 Code Review Checklist
- [ ] Code is readable and well-organized
- [ ] No hardcoded values (use config)
- [ ] Error handling is appropriate
- [ ] No security vulnerabilities
- [ ] Performance is acceptable
- [ ] Tests cover new functionality

### 5.3 Testing Strategy
| Type | Tool | Coverage |
|------|------|----------|
| Unit Tests | pytest | Core calculation logic |
| Integration | pytest | API endpoints |
| Manual | Checklist | UI/UX flows |

---

## 6. Risk Management

### 6.1 Identified Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| yfinance API changes | Medium | High | Abstract data layer, easy to swap |
| Calculation errors | Low | High | Comprehensive unit tests |
| Scope creep | Medium | Medium | Strict backlog prioritization |
| Data accuracy | Medium | High | Validate against known sources |

### 6.2 Escalation Path
1. **Developer Level:** Try to resolve independently (1 hour)
2. **Team Level:** Discuss in standup or Slack (same day)
3. **Manager Level:** Escalate blockers affecting sprint goal

---

## 7. Communication

### 7.1 Channels
| Channel | Purpose | Response Time |
|---------|---------|---------------|
| GitHub Issues | Task tracking, bugs | Same day |
| GitHub PRs | Code review | Within 24 hours |
| README updates | Documentation | As needed |

### 7.2 Status Reporting
- **Daily:** Update task status in dashboard
- **Weekly:** Sprint review summary
- **Milestone:** Release notes

---

## 8. Release Process

### 8.1 Version Numbering
```
v{MAJOR}.{MINOR}.{PATCH}

MAJOR: Breaking changes
MINOR: New features (backward compatible)
PATCH: Bug fixes
```

### 8.2 Release Checklist
- [ ] All sprint stories complete
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Changelog updated
- [ ] Version number bumped
- [ ] Tag created in Git
- [ ] Release notes published

---

## 9. Environment Setup

### 9.1 Prerequisites
```bash
# Required Software
- Python 3.10+
- Git
- VS Code (recommended)
```

### 9.2 Git Installation (Required First!)
**Windows:**
1. Download from https://git-scm.com/download/win
2. Run installer with default options
3. Restart terminal/VS Code
4. Verify: `git --version`

### 9.3 Project Setup Commands
```bash
# After Git is installed, run these commands:

# 1. Navigate to project
cd "c:\Users\IlanK\OneDrive\Projects\DCA"

# 2. Initialize Git repository
git init

# 3. Create .gitignore
# (Already created in project)

# 4. Initial commit
git add .
git commit -m "[DCA-000] chore: Initial project setup with PRD and UX docs"

# 5. Create develop branch
git checkout -b develop

# 6. Set up Python virtual environment
python -m venv venv
venv\Scripts\activate

# 7. Install dependencies
pip install -r requirements.txt
```

### 9.4 Recommended VS Code Extensions
- Python
- Pylance
- GitLens
- Prettier
- Tailwind CSS IntelliSense

---

## 10. Project Timeline Overview

```
Week 1-2: Sprint 1 (MVP Backend)
├── Portfolio data model
├── Price fetching service
├── DCA calculation engine
└── Basic Flask setup

Week 3-4: Sprint 2 (MVP Frontend)
├── Dashboard page
├── DCA Planner page
├── Portfolio management
└── Settings page

Week 5-6: Sprint 3 (Polish & History)
├── Investment history
├── Performance tracking
├── Charts and visualizations
└── Bug fixes

Week 7-8: Sprint 4 (Advanced Features)
├── Market analysis
├── Alerts system
├── Export functionality
└── Final polish
```

---

## 11. Success Criteria

### 11.1 MVP Success (End of Sprint 2)
- [ ] Can input portfolio holdings
- [ ] Fetches live stock prices
- [ ] Calculates monthly DCA recommendation
- [ ] Shows market condition status
- [ ] Displays stock-by-stock breakdown

### 11.2 Full Release Success (End of Sprint 4)
- [ ] All MVP features working
- [ ] Investment history tracking
- [ ] Performance charts
- [ ] Mobile-responsive design
- [ ] No critical bugs
- [ ] Documentation complete

---

## 12. Quick Reference Commands

```bash
# Git Commands
git status                    # Check current state
git add .                     # Stage all changes
git commit -m "message"       # Commit changes
git checkout develop          # Switch to develop
git checkout -b feature/name  # Create feature branch
git merge feature/name        # Merge branch
git push origin develop       # Push to remote

# Python Commands
python -m venv venv          # Create virtual env
venv\Scripts\activate        # Activate (Windows)
pip install -r requirements.txt  # Install deps
python app.py                # Run Flask app
pytest                       # Run tests

# Flask Commands
flask run                    # Start dev server
flask run --debug            # Start with debug mode
```

---

*This document is the single source of truth for project management. Update as processes evolve.*
