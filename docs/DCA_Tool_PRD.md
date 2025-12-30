# Product Requirements Document (PRD)
## Smart Dollar Cost Averaging (DCA) Investment Tool

---

### Document Information
- **Version:** 1.1
- **Date:** December 30, 2025
- **Author:** Investment Strategy Team
- **Status:** Draft
- **Related Documents:** [DCA_Tool_UX_Design.md](DCA_Tool_UX_Design.md)

---

## 1. Executive Summary

This document outlines the requirements for building a personal Smart DCA Investment Tool inspired by Tom Lee's Dollar Cost Averaging strategy. The tool will help individual investors systematically deploy capital into their stock portfolio by calculating optimal monthly investment amounts and dynamically adjusting contributions based on market conditions.

### Vision Statement
Build an intelligent, automated DCA calculator that takes the emotion out of investing by providing clear, actionable guidance on how much to invest each month and when to increase investments during market corrections.

---

## 2. Problem Statement

### Current Challenges
1. **Emotional Investing:** Investors often panic sell during dips or FOMO buy at peaks
2. **Inconsistent Contributions:** Without a system, investment amounts vary randomly
3. **Missed Opportunities:** Market corrections often go unexploited due to fear
4. **No Clear Guidelines:** Investors don't know when or how much to increase investments
5. **Portfolio Imbalance:** Without tracking, portfolios drift from target allocations

### Target Users
- Individual retail investors managing their own portfolios
- Long-term investors (5+ year horizon)
- Users with regular income who can commit to monthly investments
- Investors who want a disciplined, systematic approach

---

## 3. Tom Lee's DCA Strategy Principles (Core Logic)

### 3.1 Base Monthly Investment Calculation
The foundation of the strategy involves calculating a sustainable base monthly investment:

```
Base Monthly Investment = (Annual Investment Budget) / 12
```

**Factors to Consider:**
- Total investable income (after expenses, emergency fund)
- Risk tolerance level (Conservative: 10-15%, Moderate: 15-25%, Aggressive: 25-35% of income)
- Time horizon to goal

### 3.2 Market Condition Multipliers
Adjust investment amounts based on market conditions:

| Market Condition | Drawdown from ATH | Investment Multiplier |
|------------------|-------------------|----------------------|
| Normal Market | 0% to -5% | 1.0x (Base Amount) |
| Minor Correction | -5% to -10% | 1.25x |
| Correction | -10% to -15% | 1.5x |
| Significant Correction | -15% to -20% | 2.0x |
| Bear Market | -20% to -30% | 2.5x |
| Deep Bear Market | > -30% | 3.0x |

### 3.3 Individual Stock Allocation Rules
For portfolio with multiple stocks:

1. **Equal Weight Strategy:** Divide monthly investment equally among all positions
2. **Target Weight Strategy:** Allocate to bring positions back to target percentages
3. **Momentum-Adjusted:** Overweight positions showing relative strength
4. **Value-Adjusted:** Overweight positions with larger drawdowns from their individual ATH

### 3.4 Rebalancing Triggers
- **Time-Based:** Quarterly rebalancing review
- **Threshold-Based:** Rebalance when any position drifts >5% from target
- **Contribution-Based:** Use new contributions to rebalance naturally

### 3.5 Cash Reserve Management
- Maintain 10-20% cash reserve for opportunistic buying
- Deploy reserves progressively during corrections (not all at once)
- Replenish reserves during normal/elevated markets

---

## 4. Feature Requirements

### 4.1 Portfolio Setup (MVP - Phase 1)

#### 4.1.1 User Inputs
- [ ] **Portfolio Holdings Entry**
  - Stock ticker symbols
  - Current number of shares
  - Purchase price (optional, for tax lot tracking)
  - Target allocation percentage per stock

- [ ] **Investment Parameters**
  - Monthly investment budget (base amount)
  - Total investment goal (optional)
  - Investment time horizon
  - Risk tolerance level (Conservative/Moderate/Aggressive)

- [ ] **Index Selection for Market Condition**
  - Primary benchmark (default: S&P 500)
  - Option to use portfolio-specific benchmark

#### 4.1.2 System Calculations
- [ ] Calculate current portfolio value
- [ ] Calculate current allocation percentages
- [ ] Determine deviation from target allocations
- [ ] Fetch current prices via API

### 4.2 DCA Calculator Engine (MVP - Phase 1)

#### 4.2.1 Monthly Investment Recommendation
The tool should output:
```
===========================================
MONTHLY DCA RECOMMENDATION - January 2025
===========================================

Market Status: CORRECTION (-12.5% from ATH)
Investment Multiplier: 1.5x

Base Monthly Investment:     $1,000.00
Adjusted Monthly Investment: $1,500.00

STOCK-BY-STOCK BREAKDOWN:
-----------------------------------------
| Stock | Target | Current | Invest    |
-----------------------------------------
| AAPL  | 25%    | 22%     | $425.00   |
| MSFT  | 25%    | 27%     | $325.00   |
| GOOGL | 20%    | 18%     | $350.00   |
| AMZN  | 15%    | 16%     | $200.00   |
| NVDA  | 15%    | 17%     | $200.00   |
-----------------------------------------
                   TOTAL:   $1,500.00

Shares to Purchase:
- AAPL: 2.3 shares @ $185.00
- MSFT: 0.8 shares @ $406.25
- GOOGL: 2.5 shares @ $140.00
- AMZN: 1.1 shares @ $182.00
- NVDA: 0.4 shares @ $500.00
```

#### 4.2.2 Alert System
- [ ] Weekly market condition check
- [ ] Alert when multiplier changes (opportunity to invest more)
- [ ] Alert when individual stock drops significantly more than market
- [ ] Monthly reminder to execute DCA

### 4.3 Market Analysis Module (Phase 2)

#### 4.3.1 Market Condition Detection
- [ ] Fetch S&P 500 (or chosen index) current price
- [ ] Calculate All-Time High (ATH) - rolling 52-week or absolute
- [ ] Determine percentage drawdown from ATH
- [ ] Classify market condition and apply multiplier

#### 4.3.2 Individual Stock Analysis
- [ ] Calculate each stock's drawdown from its ATH
- [ ] Compare stock drawdown to market drawdown
- [ ] Flag "oversold" opportunities (stock down more than market)
- [ ] Calculate relative strength indicators

### 4.4 Historical Tracking (Phase 2)

#### 4.4.1 Investment History
- [ ] Log each monthly investment
- [ ] Track actual vs. recommended amounts
- [ ] Record purchase prices and dates
- [ ] Calculate cost basis per position

#### 4.4.2 Performance Analytics
- [ ] Total invested amount
- [ ] Current portfolio value
- [ ] Total return ($ and %)
- [ ] Return vs. benchmark (S&P 500)
- [ ] Visualization of growth over time

### 4.5 Advanced Features (Phase 3)

#### 4.5.1 Tax Optimization
- [ ] Tax lot tracking
- [ ] Tax loss harvesting suggestions
- [ ] Estimated capital gains

#### 4.5.2 Goal Planning
- [ ] Set financial goals (retirement, house, etc.)
- [ ] Project time to goal based on current DCA rate
- [ ] Scenario modeling (what if market returns X%)

#### 4.5.3 Portfolio Suggestions
- [ ] Concentration warnings
- [ ] Sector exposure analysis
- [ ] Correlation analysis
- [ ] Diversification score

---

## 5. Technical Requirements

### 5.1 Technology Stack Options

#### Option A: Simple Desktop/CLI Tool (Recommended for Personal Use)
- **Language:** Python
- **Data Storage:** SQLite or JSON files
- **Price Data:** yfinance library (free)
- **Output:** Terminal/Console or CSV export

#### Option B: Web Application
- **Frontend:** React or Vue.js
- **Backend:** Python Flask/FastAPI or Node.js
- **Database:** PostgreSQL or MongoDB
- **Price Data:** Alpha Vantage, Yahoo Finance API
- **Hosting:** Vercel, Heroku, or self-hosted

#### Option C: Spreadsheet Solution
- **Platform:** Google Sheets or Excel
- **Price Data:** GOOGLEFINANCE() or STOCKHISTORY() functions
- **Automation:** Google Apps Script or VBA

### 5.2 Data Requirements

#### External Data Sources
| Data Need | Source Options | Update Frequency |
|-----------|---------------|------------------|
| Stock Prices | Yahoo Finance, Alpha Vantage | Daily |
| Index Values | Same as above | Daily |
| ATH Data | Calculate from historical | Weekly |

#### Internal Data Storage
- User portfolio configuration
- Investment history
- Alert preferences
- Target allocations

### 5.3 Security Considerations
- No brokerage account connections (read-only price data)
- Local storage of portfolio data (privacy)
- Optional: Encryption for stored data

---

## 6. User Interface Mockups

### 6.1 Main Dashboard
```
╔══════════════════════════════════════════════════════════════╗
║              SMART DCA INVESTMENT TOOL                       ║
╠══════════════════════════════════════════════════════════════╣
║  MARKET STATUS: 🟡 CORRECTION (-12.5%)   Multiplier: 1.5x   ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  PORTFOLIO SUMMARY                                           ║
║  ────────────────                                            ║
║  Total Value:     $45,230.00                                ║
║  Total Invested:  $40,000.00                                ║
║  Total Return:    +$5,230.00 (+13.1%)                       ║
║                                                              ║
║  THIS MONTH'S RECOMMENDATION                                 ║
║  ──────────────────────────                                  ║
║  Base Amount:     $1,000.00                                 ║
║  Adjusted Amount: $1,500.00 (1.5x multiplier)               ║
║                                                              ║
║  [View Details]  [Execute DCA]  [History]                   ║
╚══════════════════════════════════════════════════════════════╝
```

### 6.2 Stock Breakdown View
```
╔══════════════════════════════════════════════════════════════╗
║  STOCK BREAKDOWN - January 2025                             ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Stock  │ Target │ Current │ Action    │ Amount   │ Shares  ║
║  ───────┼────────┼─────────┼───────────┼──────────┼──────── ║
║  AAPL   │  25%   │  22%    │ 🟢 BUY    │ $425.00  │  2.3    ║
║  MSFT   │  25%   │  27%    │ 🟡 HOLD   │ $325.00  │  0.8    ║
║  GOOGL  │  20%   │  18%    │ 🟢 BUY    │ $350.00  │  2.5    ║
║  AMZN   │  15%   │  16%    │ 🟡 HOLD   │ $200.00  │  1.1    ║
║  NVDA   │  15%   │  17%    │ 🟡 HOLD   │ $200.00  │  0.4    ║
║  ───────┴────────┴─────────┴───────────┴──────────┴──────── ║
║                              TOTAL:     $1,500.00            ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 7. User Experience Design

> 📄 **Full UX Specification:** See [DCA_Tool_UX_Design.md](DCA_Tool_UX_Design.md) for complete design details.

### 7.1 Design Philosophy
- **Clarity First:** Investment decisions need clear, unambiguous information
- **Reduce Anxiety:** Calm, confident design that reduces emotional investing
- **Action-Oriented:** Every screen leads to a clear next step
- **Data-Rich, Not Data-Heavy:** Show what matters, hide complexity

### 7.2 Color System

| Color | Hex Code | Usage |
|-------|----------|-------|
| Primary Blue | #2563EB | Trust, stability, primary actions |
| Success Green | #10B981 | Growth, positive returns, buy signals |
| Warning Amber | #F59E0B | Attention needed, hold signals |
| Alert Red | #EF4444 | Caution, significant drops |
| Neutral Gray | #6B7280 | Secondary information, backgrounds |

### 7.3 Key Pages

| Page | Purpose | Priority |
|------|---------|----------|
| **Dashboard** | Command center - portfolio status at a glance | MVP |
| **DCA Planner** | Monthly investment breakdown by stock | MVP |
| **Portfolio** | Holdings management and allocation view | MVP |
| **Market Analysis** | Market condition meter and opportunities | Phase 2 |
| **History** | Investment log and performance charts | Phase 2 |
| **Settings** | Investment parameters and preferences | MVP |

### 7.4 Site Map
```
🏠 Dashboard (Home)
├── 📊 Portfolio
│   ├── Holdings Overview
│   ├── Add/Edit Holdings
│   └── Performance History
├── 💰 DCA Planner
│   ├── Monthly Recommendation
│   ├── What-If Calculator
│   └── Execution Checklist
├── 📈 Market Analysis
│   ├── Market Status
│   ├── Stock Deep-Dive
│   └── Opportunity Scanner
├── 📅 History
│   ├── Investment Log
│   ├── Performance Charts
│   └── Export Data
├── ⚙️ Settings
│   ├── Investment Parameters
│   ├── Alert Preferences
│   └── Account Settings
└── ❓ Help & Education
```

### 7.5 Market Status Visual Indicators

| State | Color | Icon | Multiplier |
|-------|-------|------|------------|
| Normal (0-5%) | Gray | ⚪ | 1.0x |
| Minor Correction (5-10%) | Light Blue | 🔵 | 1.25x |
| Correction (10-15%) | Amber | 🟡 | 1.5x |
| Significant (15-20%) | Orange | 🟠 | 2.0x |
| Bear Market (20-30%) | Light Red | 🔴 | 2.5x |
| Deep Bear (30%+) | Red | 🔴 | 3.0x |

### 7.6 Stock Action Indicators
- 🟢 **BUY** - Stock is underweight, recommend buying more
- 🟡 **HOLD** - Stock is at or near target allocation
- 🔴 **REDUCE** - Stock is significantly overweight (rare)

### 7.7 Responsive Design Breakpoints

| Breakpoint | Width | Layout |
|------------|-------|--------|
| Mobile | < 640px | Single column, stacked cards |
| Tablet | 640px - 1024px | Two columns where possible |
| Desktop | > 1024px | Full layout with sidebar |

### 7.8 Dashboard Wireframe
```
┌────────────────────────────────────────────────────────────────────────────┐
│  🏠 Smart DCA                              [Search] [🔔] [👤 Profile]      │
├────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  🟡 MARKET CORRECTION (-12.5%)          Multiplier: 1.5x            │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────┐  ┌──────────────────────────────────────┐  │
│  │   THIS MONTH'S ACTION    │  │      PORTFOLIO SNAPSHOT              │  │
│  │   Invest: $1,500.00      │  │      Total Value: $45,230.00         │  │
│  │   (1.5x of $1,000 base)  │  │      Return: +$5,230 (+13.1%)        │  │
│  │   [View Breakdown →]     │  │      ████████████░░░░ 75% to goal    │  │
│  └──────────────────────────┘  └──────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   YOUR HOLDINGS: AAPL(22%) MSFT(27%) GOOGL(18%) AMZN(16%) NVDA(17%) │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  [ 📋 View Full Plan ]  [ ✅ Log Investment ]  [ 📊 See History ]        │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Development Phases & Timeline

### Phase 1: MVP (Weeks 1-2)
**Goal:** Basic functioning DCA calculator

| Task | Priority | Estimate |
|------|----------|----------|
| Portfolio data entry (CLI/JSON) | High | 2 days |
| Price fetching (yfinance) | High | 1 day |
| Market condition calculator | High | 2 days |
| Monthly investment calculator | High | 2 days |
| Basic output/recommendation | High | 1 day |
| Testing & refinement | High | 2 days |

**Deliverable:** Working Python script that takes portfolio input and outputs monthly DCA recommendation

### Phase 2: Enhanced Features (Weeks 3-4)
**Goal:** History tracking and alerts

| Task | Priority | Estimate |
|------|----------|----------|
| Investment history logging | Medium | 2 days |
| Performance tracking | Medium | 2 days |
| Alert system (email/console) | Medium | 2 days |
| Configuration file support | Medium | 1 day |
| Data visualization (charts) | Low | 2 days |

**Deliverable:** Tool with persistent history and basic analytics

### Phase 3: Polish & Advanced (Weeks 5-8)
**Goal:** Production-ready personal tool

| Task | Priority | Estimate |
|------|----------|----------|
| Web UI (optional) | Low | 5 days |
| Tax lot tracking | Low | 3 days |
| Goal projections | Low | 2 days |
| Mobile notifications | Low | 2 days |
| Documentation | Medium | 2 days |

**Deliverable:** Full-featured personal DCA tool

---

## 9. Success Metrics

### 9.1 Tool Effectiveness
- Consistent monthly DCA execution
- Increased investment during corrections
- Portfolio aligned with target allocations
- Reduced emotional decision-making

### 9.2 User Engagement
- Monthly active usage
- Recommendations followed
- Time saved vs. manual calculations

### 9.3 Financial Outcomes (Long-term)
- Portfolio return vs. lump-sum investing
- Risk-adjusted returns
- Adherence to investment plan

---

## 10. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| API rate limits | Medium | Cache data, use multiple sources |
| Incorrect ATH calculation | High | Validate against known values |
| Over-investing during corrections | High | Set maximum multiplier caps |
| Data source discontinued | Medium | Abstract data layer, multiple providers |
| User doesn't follow recommendations | Medium | Reminder system, automation options |

---

## 11. Future Considerations

### 11.1 Potential Enhancements
- **Brokerage Integration:** Auto-execute trades (requires careful security)
- **AI/ML Enhancements:** Sentiment analysis, predictive adjustments
- **Social Features:** Compare strategies with other users
- **Multi-Currency Support:** For international portfolios
- **Crypto Support:** Extend to cryptocurrency portfolios

### 11.2 Monetization (If Productized)
- Freemium model with basic features free
- Premium: Advanced analytics, multiple portfolios, priority data
- Affiliate links to brokerages

---

## 12. Appendix

### A. Glossary
- **DCA (Dollar Cost Averaging):** Investing fixed amounts at regular intervals
- **ATH (All-Time High):** Highest price ever reached by an asset
- **Drawdown:** Percentage decline from the most recent peak
- **Rebalancing:** Adjusting portfolio to maintain target allocations

### B. Tom Lee Strategy Reference
Tom Lee (Fundstrat Global Advisors) advocates for:
1. Staying invested during volatility
2. Buying more during fear/corrections
3. Systematic, emotion-free approach
4. Long-term perspective (years, not months)
5. Focus on quality growth stocks

### C. Sample Portfolio Configuration (JSON)
```json
{
  "portfolio_name": "Growth Portfolio",
  "base_monthly_investment": 1000,
  "risk_tolerance": "moderate",
  "benchmark": "^GSPC",
  "holdings": [
    {"ticker": "AAPL", "shares": 50, "target_pct": 25},
    {"ticker": "MSFT", "shares": 30, "target_pct": 25},
    {"ticker": "GOOGL", "shares": 40, "target_pct": 20},
    {"ticker": "AMZN", "shares": 25, "target_pct": 15},
    {"ticker": "NVDA", "shares": 10, "target_pct": 15}
  ],
  "multiplier_rules": {
    "normal": {"min_drawdown": 0, "max_drawdown": 5, "multiplier": 1.0},
    "minor_correction": {"min_drawdown": 5, "max_drawdown": 10, "multiplier": 1.25},
    "correction": {"min_drawdown": 10, "max_drawdown": 15, "multiplier": 1.5},
    "significant": {"min_drawdown": 15, "max_drawdown": 20, "multiplier": 2.0},
    "bear": {"min_drawdown": 20, "max_drawdown": 30, "multiplier": 2.5},
    "deep_bear": {"min_drawdown": 30, "max_drawdown": 100, "multiplier": 3.0}
  }
}
```

---

## 13. Next Steps

1. **Review this PRD** - Confirm requirements match expectations
2. **Review UX Design** - See [DCA_Tool_UX_Design.md](DCA_Tool_UX_Design.md) for visual specifications
3. **Choose Technology Stack** - Decide on Python CLI vs. Web App vs. Spreadsheet
4. **Start Phase 1 Development** - Begin with MVP features
5. **Test with Real Portfolio** - Use actual holdings for validation
6. **Iterate Based on Usage** - Refine based on monthly use

---

*Document prepared for personal use. Investment decisions are your own responsibility. Past performance does not guarantee future results.*
