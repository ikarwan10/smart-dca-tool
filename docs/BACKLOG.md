# Product Backlog
## Smart DCA Investment Tool

---

### Backlog Information
- **Last Updated:** December 30, 2025
- **Product Owner:** Project Lead
- **Total Stories:** 32
- **Estimated Total Effort:** ~160 hours

---

## Priority Legend
| Priority | Label | Description |
|----------|-------|-------------|
| P0 | 🔴 Critical | Must have for MVP |
| P1 | 🟠 High | Important for MVP |
| P2 | 🟡 Medium | Nice to have |
| P3 | 🟢 Low | Future enhancement |

## Status Legend
| Status | Label | Description |
|--------|-------|-------------|
| 📋 | Backlog | Not started |
| 🏃 | In Progress | Currently working |
| 👀 | In Review | Code review |
| ✅ | Done | Completed |
| 🚫 | Blocked | Waiting on dependency |

---

## Epic 1: Project Setup & Infrastructure
*Foundation for the entire project*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-001 | **Project Initialization**<br>Set up Git repo, folder structure, virtual environment, and initial dependencies | 🔴 P0 | 📋 Backlog | Sprint 1 | 2h | - |
| DCA-002 | **Flask Application Setup**<br>Create basic Flask app with routing structure and configuration | 🔴 P0 | 📋 Backlog | Sprint 1 | 2h | - |
| DCA-003 | **Database Schema Design**<br>Design SQLite schema for portfolio, holdings, history, and settings | 🔴 P0 | 📋 Backlog | Sprint 1 | 3h | - |
| DCA-004 | **Base HTML Templates**<br>Create base template with navigation, header, footer using Tailwind CSS | 🔴 P0 | 📋 Backlog | Sprint 1 | 3h | - |

**Epic Total: 10 hours**

---

## Epic 2: Portfolio Management
*CRUD operations for portfolio and holdings*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-005 | **Portfolio Data Model**<br>Create SQLAlchemy models for Portfolio and Holding entities | 🔴 P0 | 📋 Backlog | Sprint 1 | 3h | - |
| DCA-006 | **Add Holding Form**<br>UI form to add new stock holding (ticker, shares, target %) | 🔴 P0 | 📋 Backlog | Sprint 2 | 4h | - |
| DCA-007 | **Edit Holding**<br>Allow editing of existing holdings (shares, target allocation) | 🟠 P1 | 📋 Backlog | Sprint 2 | 3h | - |
| DCA-008 | **Delete Holding**<br>Remove holding from portfolio with confirmation | 🟠 P1 | 📋 Backlog | Sprint 2 | 2h | - |
| DCA-009 | **Portfolio Overview Page**<br>Display all holdings with current values and allocations | 🔴 P0 | 📋 Backlog | Sprint 2 | 5h | - |
| DCA-010 | **Allocation Chart**<br>Pie/donut chart showing current vs target allocation | 🟠 P1 | 📋 Backlog | Sprint 2 | 4h | - |

**Epic Total: 21 hours**

---

## Epic 3: Stock Price Service
*Fetching and caching stock data*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-011 | **Price Fetcher Service**<br>Create service to fetch current prices using yfinance | 🔴 P0 | 📋 Backlog | Sprint 1 | 4h | - |
| DCA-012 | **ATH Calculator**<br>Calculate All-Time High (52-week or absolute) for stocks and indices | 🔴 P0 | 📋 Backlog | Sprint 1 | 4h | - |
| DCA-013 | **Price Cache**<br>Cache prices to reduce API calls (refresh every 15 min) | 🟠 P1 | 📋 Backlog | Sprint 1 | 3h | - |
| DCA-014 | **Batch Price Fetch**<br>Fetch all portfolio stock prices in single efficient call | 🟠 P1 | 📋 Backlog | Sprint 1 | 2h | - |
| DCA-015 | **Index Data Fetch**<br>Fetch S&P 500 (or custom benchmark) data for market condition | 🔴 P0 | 📋 Backlog | Sprint 1 | 2h | - |

**Epic Total: 15 hours**

---

## Epic 4: DCA Calculation Engine
*Core business logic*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-016 | **Market Condition Calculator**<br>Calculate drawdown from ATH and determine market status | 🔴 P0 | 📋 Backlog | Sprint 1 | 4h | - |
| DCA-017 | **Multiplier Engine**<br>Apply correct multiplier based on market condition rules | 🔴 P0 | 📋 Backlog | Sprint 1 | 3h | - |
| DCA-018 | **Allocation Calculator**<br>Calculate per-stock investment amounts based on target vs current | 🔴 P0 | 📋 Backlog | Sprint 1 | 5h | - |
| DCA-019 | **Shares Calculator**<br>Convert dollar amounts to share quantities at current prices | 🔴 P0 | 📋 Backlog | Sprint 1 | 2h | - |
| DCA-020 | **Rebalancing Logic**<br>Prioritize underweight stocks, reduce overweight allocations | 🟠 P1 | 📋 Backlog | Sprint 2 | 4h | - |

**Epic Total: 18 hours**

---

## Epic 5: Dashboard & DCA Planner UI
*Main user interface*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-021 | **Dashboard Page**<br>Main page with market status, monthly recommendation, portfolio snapshot | 🔴 P0 | 📋 Backlog | Sprint 2 | 6h | - |
| DCA-022 | **Market Status Banner**<br>Color-coded banner showing current market condition | 🔴 P0 | 📋 Backlog | Sprint 2 | 3h | - |
| DCA-023 | **DCA Planner Page**<br>Detailed stock-by-stock investment breakdown | 🔴 P0 | 📋 Backlog | Sprint 2 | 6h | - |
| DCA-024 | **Holdings Cards**<br>Visual cards for each stock with buy/hold indicator | 🟠 P1 | 📋 Backlog | Sprint 2 | 4h | - |
| DCA-025 | **Order Summary**<br>Copyable order details for easy brokerage entry | 🟠 P1 | 📋 Backlog | Sprint 2 | 3h | - |
| DCA-026 | **Responsive Design**<br>Mobile-friendly layouts for all pages | 🟡 P2 | 📋 Backlog | Sprint 3 | 5h | - |

**Epic Total: 27 hours**

---

## Epic 6: Settings & Configuration
*User preferences*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-027 | **Settings Page**<br>UI for managing investment parameters | 🔴 P0 | 📋 Backlog | Sprint 2 | 4h | - |
| DCA-028 | **Base Amount Config**<br>Set/edit base monthly investment amount | 🔴 P0 | 📋 Backlog | Sprint 2 | 2h | - |
| DCA-029 | **Multiplier Rules Config**<br>Customize multiplier thresholds and values | 🟡 P2 | 📋 Backlog | Sprint 3 | 4h | - |
| DCA-030 | **Investment Goal Setting**<br>Set target portfolio value with progress tracking | 🟡 P2 | 📋 Backlog | Sprint 3 | 3h | - |

**Epic Total: 13 hours**

---

## Epic 7: History & Tracking
*Investment history and performance*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-031 | **Log Investment Action**<br>Record when user completes monthly investment | 🟠 P1 | 📋 Backlog | Sprint 3 | 4h | - |
| DCA-032 | **Investment History Page**<br>Display log of all past investments | 🟠 P1 | 📋 Backlog | Sprint 3 | 5h | - |
| DCA-033 | **Performance Calculator**<br>Calculate total return, vs benchmark, time-weighted | 🟡 P2 | 📋 Backlog | Sprint 3 | 6h | - |
| DCA-034 | **Performance Chart**<br>Line chart showing portfolio growth over time | 🟡 P2 | 📋 Backlog | Sprint 3 | 5h | - |
| DCA-035 | **Export to CSV**<br>Export investment history and performance data | 🟢 P3 | 📋 Backlog | Sprint 4 | 3h | - |

**Epic Total: 23 hours**

---

## Epic 8: Market Analysis
*Advanced market insights*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-036 | **Market Analysis Page**<br>Dedicated page for market condition details | 🟡 P2 | 📋 Backlog | Sprint 4 | 5h | - |
| DCA-037 | **Market Condition Meter**<br>Visual gauge showing position on drawdown scale | 🟡 P2 | 📋 Backlog | Sprint 4 | 4h | - |
| DCA-038 | **Opportunity Scanner**<br>Highlight stocks with larger-than-market discounts | 🟢 P3 | 📋 Backlog | Sprint 4 | 5h | - |
| DCA-039 | **Historical Context Chart**<br>Show current position vs historical corrections | 🟢 P3 | 📋 Backlog | Sprint 4 | 5h | - |

**Epic Total: 19 hours**

---

## Epic 9: Polish & Documentation
*Final touches*

| ID | Story | Priority | Status | Sprint | Estimate | Assigned |
|----|-------|----------|--------|--------|----------|----------|
| DCA-040 | **Error Handling**<br>Graceful error messages for API failures, invalid inputs | 🟠 P1 | 📋 Backlog | Sprint 3 | 4h | - |
| DCA-041 | **Loading States**<br>Skeleton loaders and spinners during data fetch | 🟡 P2 | 📋 Backlog | Sprint 3 | 3h | - |
| DCA-042 | **Empty States**<br>Helpful messages when no data exists | 🟡 P2 | 📋 Backlog | Sprint 3 | 2h | - |
| DCA-043 | **User Documentation**<br>Help page explaining DCA strategy and tool usage | 🟢 P3 | 📋 Backlog | Sprint 4 | 4h | - |
| DCA-044 | **README & Setup Docs**<br>Installation and development documentation | 🟠 P1 | 📋 Backlog | Sprint 4 | 3h | - |

**Epic Total: 16 hours**

---

## Backlog Summary by Sprint

### Sprint 1: MVP Backend (Week 1-2)
| Epic | Stories | Hours |
|------|---------|-------|
| Project Setup | DCA-001 to DCA-004 | 10h |
| Portfolio Management | DCA-005 | 3h |
| Stock Price Service | DCA-011 to DCA-015 | 15h |
| DCA Calculation Engine | DCA-016 to DCA-019 | 14h |
| **Sprint 1 Total** | **13 stories** | **42h** |

### Sprint 2: MVP Frontend (Week 3-4)
| Epic | Stories | Hours |
|------|---------|-------|
| Portfolio Management | DCA-006 to DCA-010 | 18h |
| DCA Calculation Engine | DCA-020 | 4h |
| Dashboard & UI | DCA-021 to DCA-025 | 22h |
| Settings | DCA-027, DCA-028 | 6h |
| **Sprint 2 Total** | **12 stories** | **50h** |

### Sprint 3: History & Polish (Week 5-6)
| Epic | Stories | Hours |
|------|---------|-------|
| Dashboard & UI | DCA-026 | 5h |
| Settings | DCA-029, DCA-030 | 7h |
| History & Tracking | DCA-031 to DCA-034 | 20h |
| Polish | DCA-040 to DCA-042 | 9h |
| **Sprint 3 Total** | **9 stories** | **41h** |

### Sprint 4: Advanced Features (Week 7-8)
| Epic | Stories | Hours |
|------|---------|-------|
| History & Tracking | DCA-035 | 3h |
| Market Analysis | DCA-036 to DCA-039 | 19h |
| Documentation | DCA-043, DCA-044 | 7h |
| **Sprint 4 Total** | **6 stories** | **29h** |

---

## User Story Details

### DCA-001: Project Initialization
**As a** developer  
**I want** the project properly initialized with Git, folder structure, and dependencies  
**So that** I can start development with best practices

**Acceptance Criteria:**
- [ ] Git repository initialized
- [ ] .gitignore configured for Python/Flask
- [ ] Folder structure created (app/, templates/, static/, tests/)
- [ ] requirements.txt with initial dependencies
- [ ] Virtual environment setup instructions in README
- [ ] Initial commit with all PRD/UX documents

**Technical Notes:**
```
Dependencies:
- flask
- flask-sqlalchemy
- yfinance
- pytest
- python-dotenv
```

---

### DCA-016: Market Condition Calculator
**As a** user  
**I want** the system to automatically detect current market conditions  
**So that** I know when to invest more

**Acceptance Criteria:**
- [ ] Fetches current S&P 500 price
- [ ] Calculates 52-week high (or absolute ATH)
- [ ] Computes percentage drawdown
- [ ] Returns market condition classification
- [ ] Handles API errors gracefully

**Technical Notes:**
```python
def get_market_condition(benchmark="^GSPC"):
    # Returns: {
    #   "current_price": 4567.23,
    #   "ath": 5221.45,
    #   "drawdown_pct": 12.5,
    #   "condition": "correction",
    #   "multiplier": 1.5
    # }
```

---

### DCA-021: Dashboard Page
**As a** user  
**I want** to see my investment status at a glance on the dashboard  
**So that** I can quickly understand what action to take

**Acceptance Criteria:**
- [ ] Market status banner with color coding
- [ ] This month's recommended investment amount
- [ ] Portfolio value and return summary
- [ ] Progress toward investment goal
- [ ] Holdings overview with allocation percentages
- [ ] Quick action buttons (View Plan, Log Investment, History)
- [ ] Responsive on mobile devices

**Wireframe Reference:** See [DCA_Tool_UX_Design.md](../DCA_Tool_UX_Design.md) Section 3.1

---

## Icebox (Future Consideration)
*Items not scheduled but captured for future*

| ID | Story | Notes |
|----|-------|-------|
| ICE-001 | Brokerage API Integration | Security concerns, needs research |
| ICE-002 | Email Notifications | Requires email service setup |
| ICE-003 | Multiple Portfolios | Support for different accounts |
| ICE-004 | Crypto Support | Different data sources needed |
| ICE-005 | AI Recommendations | ML for optimal allocation |
| ICE-006 | Tax Lot Tracking | Complex, phase 2 consideration |

---

*Backlog is reviewed and re-prioritized at the start of each sprint.*
