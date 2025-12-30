# Sprint Planning
## Smart DCA Investment Tool

---

### Sprint Information
- **Sprint Duration:** 2 weeks (10 working days)
- **Working Hours:** ~25 hours/week estimated
- **Total Sprints:** 4

---

## Sprint Overview

| Sprint | Duration | Focus | Hours | Status |
|--------|----------|-------|-------|--------|
| Sprint 0 | Dec 30-31, 2025 | Planning & Setup | 10h | ✅ Complete |
| Sprint 1 | Jan 1-14, 2026 | MVP Backend | 42h | ✅ Complete |
| Sprint 2 | Jan 15-28, 2026 | MVP Frontend | 50h | ✅ Complete |
| Sprint 3 | Jan 29 - Feb 11, 2026 | History & Polish | 41h | 🏃 Current |
| Sprint 4 | Feb 12-25, 2026 | Advanced Features | 29h | 📋 Planned |

---

## Sprint 0: Planning & Setup
**Duration:** December 30-31, 2025 (2 days)  
**Goal:** Complete project planning and prepare for development  
**Status:** 🏃 In Progress

### Sprint 0 Backlog

| Task | Priority | Estimate | Status | Notes |
|------|----------|----------|--------|-------|
| Create PRD document | P0 | 2h | ✅ Done | DCA_Tool_PRD.md |
| Create UX Design document | P0 | 2h | ✅ Done | DCA_Tool_UX_Design.md |
| Create Manager guide | P0 | 1h | ✅ Done | docs/MANAGER.md |
| Create Backlog | P0 | 2h | ✅ Done | docs/BACKLOG.md |
| Create Dashboard | P0 | 1h | ✅ Done | docs/DASHBOARD.md |
| Create Sprint plan | P0 | 1h | ✅ Done | docs/SPRINTS.md |
| Install Git | P0 | 0.5h | 📋 Todo | Required for dev |
| Initialize Git repo | P0 | 0.5h | 📋 Todo | After Git install |
| **Total** | | **10h** | | |

### Sprint 0 Definition of Done
- [x] PRD reviewed and complete
- [x] UX Design document complete
- [x] All management docs created
- [ ] Git repository initialized
- [ ] Initial commit with planning docs

---

## Sprint 1: MVP Backend
**Duration:** January 1-14, 2026 (2 weeks)  
**Goal:** Core calculation engine working, can output DCA recommendation via console  
**Status:** 📋 Planned

### Sprint 1 Goal Statement
> By the end of Sprint 1, we can input a portfolio configuration, fetch live stock prices, calculate market conditions, and output a complete DCA recommendation showing how much to invest in each stock.

### Sprint 1 Backlog

| ID | Story | Priority | Estimate | Status |
|----|-------|----------|----------|--------|
| DCA-001 | Project Initialization | 🔴 P0 | 2h | 📋 |
| DCA-002 | Flask Application Setup | 🔴 P0 | 2h | 📋 |
| DCA-003 | Database Schema Design | 🔴 P0 | 3h | 📋 |
| DCA-004 | Base HTML Templates | 🔴 P0 | 3h | 📋 |
| DCA-005 | Portfolio Data Model | 🔴 P0 | 3h | 📋 |
| DCA-011 | Price Fetcher Service | 🔴 P0 | 4h | 📋 |
| DCA-012 | ATH Calculator | 🔴 P0 | 4h | 📋 |
| DCA-013 | Price Cache | 🟠 P1 | 3h | 📋 |
| DCA-014 | Batch Price Fetch | 🟠 P1 | 2h | 📋 |
| DCA-015 | Index Data Fetch | 🔴 P0 | 2h | 📋 |
| DCA-016 | Market Condition Calculator | 🔴 P0 | 4h | 📋 |
| DCA-017 | Multiplier Engine | 🔴 P0 | 3h | 📋 |
| DCA-018 | Allocation Calculator | 🔴 P0 | 5h | 📋 |
| DCA-019 | Shares Calculator | 🔴 P0 | 2h | 📋 |
| **Total** | **14 stories** | | **42h** | |

### Sprint 1 Technical Tasks Breakdown

#### Day 1-2: Project Setup (DCA-001, DCA-002)
```
□ Initialize Git repository
□ Create folder structure:
  /app
    /models
    /services
    /routes
    /templates
    /static
  /tests
  /docs
□ Create requirements.txt
□ Set up virtual environment
□ Create basic Flask app.py
□ Create configuration (config.py)
□ Test Flask runs on localhost:5000
```

#### Day 3-4: Database & Models (DCA-003, DCA-005)
```
□ Design database schema
□ Create SQLAlchemy models:
  - Portfolio
  - Holding
  - Settings
  - InvestmentHistory
□ Create database initialization
□ Write model unit tests
```

#### Day 5-6: Price Service (DCA-011, DCA-012, DCA-013)
```
□ Create price_service.py
□ Implement get_stock_price()
□ Implement get_historical_data()
□ Implement calculate_ath()
□ Add price caching mechanism
□ Write unit tests for price service
```

#### Day 7-8: Index & Market Data (DCA-014, DCA-015, DCA-016)
```
□ Implement batch price fetching
□ Create market_service.py
□ Implement get_market_condition()
□ Test with S&P 500 data
□ Handle API errors gracefully
```

#### Day 9-10: DCA Engine (DCA-017, DCA-018, DCA-019, DCA-004)
```
□ Create dca_engine.py
□ Implement multiplier logic
□ Implement allocation calculator
□ Implement shares calculator
□ Create base HTML templates
□ Integration testing
□ Sprint review preparation
```

### Sprint 1 Deliverables
- [ ] Flask app running on localhost
- [ ] Database with portfolio/holdings tables
- [ ] Working price fetch service
- [ ] Market condition calculator
- [ ] DCA calculation engine
- [ ] Console/debug output of recommendation
- [ ] Basic test suite (>70% coverage on core)

### Sprint 1 Risks
| Risk | Mitigation |
|------|------------|
| yfinance API issues | Test early, have mock data ready |
| Complex calculation bugs | Write unit tests first (TDD) |
| Scope creep | Stick to backlog, no new features |

---

## Sprint 2: MVP Frontend
**Duration:** January 15-28, 2026 (2 weeks)  
**Goal:** Fully usable web interface for viewing and managing DCA  
**Status:** 📋 Planned

### Sprint 2 Goal Statement
> By the end of Sprint 2, users can interact with the tool through a web browser: view dashboard, see DCA recommendations, manage portfolio holdings, and configure settings.

### Sprint 2 Backlog

| ID | Story | Priority | Estimate | Status |
|----|-------|----------|----------|--------|
| DCA-006 | Add Holding Form | 🔴 P0 | 4h | 📋 |
| DCA-007 | Edit Holding | 🟠 P1 | 3h | 📋 |
| DCA-008 | Delete Holding | 🟠 P1 | 2h | 📋 |
| DCA-009 | Portfolio Overview Page | 🔴 P0 | 5h | 📋 |
| DCA-010 | Allocation Chart | 🟠 P1 | 4h | 📋 |
| DCA-020 | Rebalancing Logic | 🟠 P1 | 4h | 📋 |
| DCA-021 | Dashboard Page | 🔴 P0 | 6h | 📋 |
| DCA-022 | Market Status Banner | 🔴 P0 | 3h | 📋 |
| DCA-023 | DCA Planner Page | 🔴 P0 | 6h | 📋 |
| DCA-024 | Holdings Cards | 🟠 P1 | 4h | 📋 |
| DCA-025 | Order Summary | 🟠 P1 | 3h | 📋 |
| DCA-027 | Settings Page | 🔴 P0 | 4h | 📋 |
| DCA-028 | Base Amount Config | 🔴 P0 | 2h | 📋 |
| **Total** | **13 stories** | | **50h** | |

### Sprint 2 Technical Tasks Breakdown

#### Day 1-2: Portfolio CRUD UI (DCA-006, DCA-007, DCA-008)
```
□ Create add holding form template
□ Create edit holding form template
□ Implement delete with confirmation
□ Add form validation (client + server)
□ Flash messages for success/error
```

#### Day 3-4: Portfolio Page (DCA-009, DCA-010)
```
□ Create portfolio.html template
□ Display holdings table
□ Show current vs target allocation
□ Implement Chart.js pie chart
□ Style with Tailwind CSS
```

#### Day 5-6: Dashboard (DCA-021, DCA-022)
```
□ Create dashboard.html template
□ Implement market status banner component
□ Portfolio snapshot card
□ This month's recommendation card
□ Quick action buttons
□ Holdings overview grid
```

#### Day 7-8: DCA Planner (DCA-023, DCA-024, DCA-025, DCA-020)
```
□ Create planner.html template
□ Stock-by-stock breakdown cards
□ Allocation progress bars
□ Order summary section
□ Copy-to-clipboard functionality
□ Implement rebalancing in allocation
```

#### Day 9-10: Settings & Polish (DCA-027, DCA-028)
```
□ Create settings.html template
□ Base amount input form
□ Save settings functionality
□ Navigation between pages
□ Consistent styling throughout
□ Sprint review preparation
```

### Sprint 2 Deliverables
- [ ] Dashboard page working
- [ ] DCA Planner page working
- [ ] Portfolio management (add/edit/delete)
- [ ] Settings page (base amount)
- [ ] All pages styled with Tailwind
- [ ] Charts implemented with Chart.js
- [ ] Fully navigable web app

### Sprint 2 Risks
| Risk | Mitigation |
|------|------------|
| UI takes longer than estimated | Prioritize function over polish |
| Chart.js learning curve | Use simple examples first |
| Scope creep on design | Follow UX doc strictly |

---

## Sprint 3: History & Polish
**Duration:** January 29 - February 11, 2026 (2 weeks)  
**Goal:** Investment tracking, performance history, and UI polish  
**Status:** 📋 Planned

### Sprint 3 Goal Statement
> By the end of Sprint 3, users can log investments, view history, see performance charts, and enjoy a polished, mobile-responsive interface.

### Sprint 3 Backlog

| ID | Story | Priority | Estimate | Status |
|----|-------|----------|----------|--------|
| DCA-026 | Responsive Design | 🟡 P2 | 5h | 📋 |
| DCA-029 | Multiplier Rules Config | 🟡 P2 | 4h | 📋 |
| DCA-030 | Investment Goal Setting | 🟡 P2 | 3h | 📋 |
| DCA-031 | Log Investment Action | 🟠 P1 | 4h | 📋 |
| DCA-032 | Investment History Page | 🟠 P1 | 5h | 📋 |
| DCA-033 | Performance Calculator | 🟡 P2 | 6h | 📋 |
| DCA-034 | Performance Chart | 🟡 P2 | 5h | 📋 |
| DCA-040 | Error Handling | 🟠 P1 | 4h | 📋 |
| DCA-041 | Loading States | 🟡 P2 | 3h | 📋 |
| DCA-042 | Empty States | 🟡 P2 | 2h | 📋 |
| **Total** | **10 stories** | | **41h** | |

### Sprint 3 Deliverables
- [ ] Log investment functionality
- [ ] History page with table
- [ ] Performance line chart
- [ ] Goal progress tracking
- [ ] Mobile responsive design
- [ ] Error handling throughout
- [ ] Loading and empty states

---

## Sprint 4: Advanced Features
**Duration:** February 12-25, 2026 (2 weeks)  
**Goal:** Market analysis, export, documentation, release prep  
**Status:** 📋 Planned

### Sprint 4 Goal Statement
> By the end of Sprint 4, the tool is feature-complete with market analysis, data export, full documentation, and ready for v1.0 release.

### Sprint 4 Backlog

| ID | Story | Priority | Estimate | Status |
|----|-------|----------|----------|--------|
| DCA-035 | Export to CSV | 🟢 P3 | 3h | 📋 |
| DCA-036 | Market Analysis Page | 🟡 P2 | 5h | 📋 |
| DCA-037 | Market Condition Meter | 🟡 P2 | 4h | 📋 |
| DCA-038 | Opportunity Scanner | 🟢 P3 | 5h | 📋 |
| DCA-039 | Historical Context Chart | 🟢 P3 | 5h | 📋 |
| DCA-043 | User Documentation | 🟢 P3 | 4h | 📋 |
| DCA-044 | README & Setup Docs | 🟠 P1 | 3h | 📋 |
| **Total** | **7 stories** | | **29h** | |

### Sprint 4 Deliverables
- [ ] Market analysis page
- [ ] Opportunity scanner
- [ ] CSV export functionality
- [ ] Complete README
- [ ] User help documentation
- [ ] Release v1.0 tagged

---

## Sprint Ceremonies Schedule

### Daily Standup
- **Time:** 9:00 AM (5 min)
- **Format:** What I did, what I'll do, blockers

### Sprint Planning (Day 1)
- **Time:** 9:00 AM (1 hour)
- **Activities:**
  1. Review sprint goal
  2. Confirm backlog items
  3. Break into tasks
  4. Estimate and assign

### Sprint Review (Day 10)
- **Time:** 2:00 PM (30 min)
- **Activities:**
  1. Demo completed features
  2. Gather feedback
  3. Update backlog

### Sprint Retrospective (Day 10)
- **Time:** 3:00 PM (30 min)
- **Format:**
  1. What went well? ✅
  2. What could improve? 🔄
  3. Action items for next sprint 📝

---

## Definition of Done (All Sprints)

A story is considered "Done" when:

- [ ] Code is complete and follows style guide
- [ ] Unit tests written and passing
- [ ] No linting errors
- [ ] Code reviewed (self-review for solo)
- [ ] Feature works in browser
- [ ] Documentation updated if needed
- [ ] Committed to develop branch
- [ ] Story updated in dashboard

---

## Estimation Guidelines

| Points | Hours | Complexity |
|--------|-------|------------|
| 1 | 1-2h | Trivial change |
| 2 | 2-4h | Simple feature |
| 3 | 4-6h | Medium feature |
| 5 | 6-10h | Complex feature |
| 8 | 10-16h | Very complex, consider splitting |

---

## Sprint Velocity Tracking

| Sprint | Planned | Completed | Velocity | Notes |
|--------|---------|-----------|----------|-------|
| Sprint 0 | 10h | - | - | Planning |
| Sprint 1 | 42h | - | - | - |
| Sprint 2 | 50h | - | - | - |
| Sprint 3 | 41h | - | - | - |
| Sprint 4 | 29h | - | - | - |

**Average Velocity:** *Calculated after Sprint 1*

---

*Sprint plans are reviewed and adjusted at the start of each sprint based on velocity and priorities.*
