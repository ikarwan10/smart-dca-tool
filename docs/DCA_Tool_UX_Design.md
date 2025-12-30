# UX Design Document
## Smart DCA Investment Tool - Website Design Specification

---

### Document Information
- **Version:** 1.0
- **Date:** December 30, 2025
- **Author:** UX Design Team
- **Related Document:** DCA_Tool_PRD.md

---

## 1. Design Philosophy

### 1.1 Core Principles
- **Clarity First:** Investment decisions need clear, unambiguous information
- **Reduce Anxiety:** Calm, confident design that reduces emotional investing
- **Action-Oriented:** Every screen leads to a clear next step
- **Data-Rich, Not Data-Heavy:** Show what matters, hide complexity

### 1.2 Design Keywords
`Professional` · `Trustworthy` · `Calm` · `Modern` · `Minimal` · `Actionable`

### 1.3 Color Psychology
- **Primary Blue (#2563EB):** Trust, stability, confidence
- **Success Green (#10B981):** Growth, positive returns, buy signals
- **Warning Amber (#F59E0B):** Attention needed, hold signals
- **Alert Red (#EF4444):** Caution, significant drops (but not panic-inducing)
- **Neutral Gray (#6B7280):** Secondary information, backgrounds

---

## 2. Information Architecture

### 2.1 Site Map
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
    ├── DCA Strategy Guide
    ├── FAQ
    └── Glossary
```

### 2.2 User Flow - Primary Journey
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Login/    │────▶│  Dashboard  │────▶│   View      │────▶│  Execute    │
│   Open App  │     │  Overview   │     │  This Month │     │  Purchases  │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Explore   │
                    │   Details   │
                    └─────────────┘
```

---

## 3. Page-by-Page Design

---

### 3.1 DASHBOARD (Home Page)

The dashboard is the command center - users should understand their investment status within 3 seconds.

#### Layout Structure
```
┌────────────────────────────────────────────────────────────────────────────┐
│  🏠 Smart DCA                              [Search] [🔔] [👤 Profile]      │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                    🟡 MARKET STATUS BANNER                          │  │
│  │         "Market in CORRECTION territory (-12.5% from ATH)"          │  │
│  │              Your investment multiplier is now: 1.5x                │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌──────────────────────────┐  ┌──────────────────────────────────────┐  │
│  │   THIS MONTH'S ACTION    │  │      PORTFOLIO SNAPSHOT              │  │
│  │   ━━━━━━━━━━━━━━━━━━━━   │  │      ━━━━━━━━━━━━━━━━━━              │  │
│  │                          │  │                                      │  │
│  │   Recommended:           │  │   Total Value    $45,230.00          │  │
│  │   ┌──────────────────┐   │  │   Total Invested $40,000.00          │  │
│  │   │   $1,500.00      │   │  │   Total Return   +$5,230 (+13.1%)    │  │
│  │   └──────────────────┘   │  │                                      │  │
│  │   (1.5x of $1,000 base)  │  │   ┌────────────────────────────┐     │  │
│  │                          │  │   │ ████████████░░░░  75%      │     │  │
│  │   [View Breakdown →]     │  │   │ To Goal: $60,000           │     │  │
│  │                          │  │   └────────────────────────────┘     │  │
│  └──────────────────────────┘  └──────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   QUICK ACTIONS                                                     │  │
│  │                                                                     │  │
│  │   [ 📋 View Full Plan ]  [ ✅ Log Investment ]  [ 📊 See History ] │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   YOUR HOLDINGS                                           [Edit →]  │  │
│  │   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  │
│  │                                                                     │  │
│  │   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐    │  │
│  │   │  AAPL   │  MSFT   │  GOOGL  │  AMZN   │  NVDA   │  Cash   │    │  │
│  │   │  22%    │  27%    │  18%    │  16%    │  17%    │   0%    │    │  │
│  │   │ +2.3%   │ -1.1%   │ +0.8%   │ +1.5%   │ -3.2%   │         │    │  │
│  │   │ 🟢      │ 🔴      │ 🟢      │ 🟢      │ 🔴      │         │    │  │
│  │   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘    │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

#### Component Specifications

**Market Status Banner**
| State | Color | Icon | Message |
|-------|-------|------|---------|
| Normal (0-5%) | Gray | ⚪ | "Markets stable - Continue regular DCA" |
| Minor Correction (5-10%) | Light Blue | 🔵 | "Minor pullback - Slight opportunity" |
| Correction (10-15%) | Amber | 🟡 | "Correction territory - Good buying opportunity" |
| Significant (15-20%) | Orange | 🟠 | "Significant correction - Strong opportunity" |
| Bear Market (20-30%) | Light Red | 🔴 | "Bear market - Major opportunity" |
| Deep Bear (30%+) | Red | 🔴 | "Deep bear - Exceptional opportunity" |

**Portfolio Snapshot Card**
- Large, bold numbers for value and return
- Return shown in both $ and %
- Color-coded: Green for positive, Red for negative
- Progress bar to investment goal (if set)

---

### 3.2 DCA PLANNER PAGE

The core feature - shows exactly what to buy and how much.

#### Layout Structure
```
┌────────────────────────────────────────────────────────────────────────────┐
│  ← Back to Dashboard          DCA PLANNER                    January 2025  │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   INVESTMENT SUMMARY                                                │  │
│  │   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │  │
│  │                                                                     │  │
│  │   Base Monthly Amount          $1,000.00                           │  │
│  │   Market Multiplier            × 1.5 (Correction)                  │  │
│  │   ─────────────────────────────────────────                        │  │
│  │   THIS MONTH'S INVESTMENT      $1,500.00                           │  │
│  │                                                                     │  │
│  │   [ Adjust Base Amount ]                                           │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   STOCK-BY-STOCK BREAKDOWN                                          │  │
│  │   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  │
│  │                                                                     │  │
│  │   ┌────────────────────────────────────────────────────────────┐   │  │
│  │   │ AAPL - Apple Inc.                                          │   │  │
│  │   │ ──────────────────────────────────────────────────────────│   │  │
│  │   │                                                            │   │  │
│  │   │  Current: 22%  ──────────█████████████░░░░░░░──  Target: 25%│  │  │
│  │   │                          ↑ Underweight by 3%               │   │  │
│  │   │                                                            │   │  │
│  │   │  💰 Invest: $425.00                                        │   │  │
│  │   │  📊 Shares: 2.3 shares @ $185.00                          │   │  │
│  │   │  📈 Stock Status: -8% from ATH (Slight discount)          │   │  │
│  │   │                                                            │   │  │
│  │   │  [Copy Order Details]                                      │   │  │
│  │   └────────────────────────────────────────────────────────────┘   │  │
│  │                                                                     │  │
│  │   ┌────────────────────────────────────────────────────────────┐   │  │
│  │   │ MSFT - Microsoft Corp.                                     │   │  │
│  │   │ ──────────────────────────────────────────────────────────│   │  │
│  │   │                                                            │   │  │
│  │   │  Current: 27%  ──────────████████████████████░──  Target: 25%│ │  │
│  │   │                          ↑ Overweight by 2%                │   │  │
│  │   │                                                            │   │  │
│  │   │  💰 Invest: $325.00 (reduced to rebalance)                 │   │  │
│  │   │  📊 Shares: 0.8 shares @ $406.25                          │   │  │
│  │   │  📈 Stock Status: -5% from ATH                            │   │  │
│  │   │                                                            │   │  │
│  │   │  [Copy Order Details]                                      │   │  │
│  │   └────────────────────────────────────────────────────────────┘   │  │
│  │                                                                     │  │
│  │   ... (More stocks)                                                │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   ORDER SUMMARY                                                     │  │
│  │   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │  │
│  │                                                                     │  │
│  │   AAPL    2.3 shares × $185.00  =  $425.00                        │  │
│  │   MSFT    0.8 shares × $406.25  =  $325.00                        │  │
│  │   GOOGL   2.5 shares × $140.00  =  $350.00                        │  │
│  │   AMZN    1.1 shares × $182.00  =  $200.00                        │  │
│  │   NVDA    0.4 shares × $500.00  =  $200.00                        │  │
│  │   ────────────────────────────────────────                        │  │
│  │   TOTAL                            $1,500.00                       │  │
│  │                                                                     │  │
│  │   [ 📋 Copy All Orders ]    [ ✅ Mark as Completed ]               │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

#### Interaction Details

**Allocation Progress Bar**
```
Underweight (Buy More):
Current: 22%  ████████████░░░░░░░░  Target: 25%
              ←── Green zone ───→

At Target:
Current: 25%  █████████████████████  Target: 25%
              ←── Blue zone ────→

Overweight (Buy Less):
Current: 27%  ██████████████████████████  Target: 25%
              ←── Amber zone ────────→
```

**Copy Order Details Button**
- Copies formatted text for easy paste into brokerage:
```
BUY 2 shares AAPL @ Market
```

---

### 3.3 PORTFOLIO PAGE

View and manage all holdings.

#### Layout Structure
```
┌────────────────────────────────────────────────────────────────────────────┐
│  ← Dashboard                    PORTFOLIO                    [+ Add Stock] │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   PORTFOLIO OVERVIEW                                                │  │
│  │                                                                     │  │
│  │   ┌───────────────┐  ┌───────────────┐  ┌───────────────┐          │  │
│  │   │ Total Value   │  │ Total Cost    │  │ Total Return  │          │  │
│  │   │ $45,230.00    │  │ $40,000.00    │  │ +$5,230.00    │          │  │
│  │   │               │  │               │  │ +13.08%       │          │  │
│  │   └───────────────┘  └───────────────┘  └───────────────┘          │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   ALLOCATION CHART                                                  │  │
│  │                                                                     │  │
│  │           Current Allocation          Target Allocation             │  │
│  │                                                                     │  │
│  │              ┌─────┐                      ┌─────┐                   │  │
│  │         ┌────┤AAPL ├────┐            ┌────┤AAPL ├────┐             │  │
│  │      ┌──┤    │ 22% │    ├──┐      ┌──┤    │ 25% │    ├──┐         │  │
│  │   ┌──┤  │    └─────┘    │  ├──┐┌──┤  │    └─────┘    │  ├──┐      │  │
│  │   │NV│MS│               │GO│AM││NV│MS│               │GO│AM│      │  │
│  │   │DA│FT│               │OG│ZN││DA│FT│               │OG│ZN│      │  │
│  │   │17│27│               │18│16││15│25│               │20│15│      │  │
│  │   └──┴──┴───────────────┴──┴──┘└──┴──┴───────────────┴──┴──┘      │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   HOLDINGS TABLE                                     [Sort ▼] [Filter]│ │
│  │   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  │
│  │                                                                     │  │
│  │   Stock   Shares  Price    Value      Cost     Return    Alloc     │  │
│  │   ──────────────────────────────────────────────────────────────── │  │
│  │   AAPL    50     $185.00  $9,250    $8,000   +$1,250   22% → 25%  │  │
│  │                                               +15.6%    🟢 Buy     │  │
│  │   ──────────────────────────────────────────────────────────────── │  │
│  │   MSFT    30     $406.25  $12,187   $10,500  +$1,687   27% → 25%  │  │
│  │                                               +16.1%    🟡 Hold    │  │
│  │   ──────────────────────────────────────────────────────────────── │  │
│  │   GOOGL   40     $140.00  $5,600    $5,200   +$400     18% → 20%  │  │
│  │                                               +7.7%     🟢 Buy     │  │
│  │   ──────────────────────────────────────────────────────────────── │  │
│  │   AMZN    25     $182.00  $4,550    $4,000   +$550     16% → 15%  │  │
│  │                                               +13.8%    🟡 Hold    │  │
│  │   ──────────────────────────────────────────────────────────────── │  │
│  │   NVDA    10     $500.00  $5,000    $4,500   +$500     17% → 15%  │  │
│  │                                               +11.1%    🟡 Hold    │  │
│  │   ──────────────────────────────────────────────────────────────── │  │
│  │                                                                     │  │
│  │   [Edit Targets]                              [Export CSV]          │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.4 MARKET ANALYSIS PAGE

Deep dive into market conditions and individual stock analysis.

#### Layout Structure
```
┌────────────────────────────────────────────────────────────────────────────┐
│  ← Dashboard                 MARKET ANALYSIS                               │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   MARKET CONDITION METER                                            │  │
│  │                                                                     │  │
│  │   S&P 500 Current: 4,567.23    ATH: 5,221.45    Drawdown: -12.5%   │  │
│  │                                                                     │  │
│  │   ├────────┼────────┼────────┼────────┼────────┼────────┤          │  │
│  │   0%      -5%     -10%     -15%     -20%     -30%                   │  │
│  │   Normal   Minor   Correct  Signif   Bear    Deep                   │  │
│  │            Corr            Correct          Bear                    │  │
│  │                      ▲                                              │  │
│  │                   YOU ARE                                           │  │
│  │                    HERE                                             │  │
│  │                                                                     │  │
│  │   Investment Multiplier: 1.5x                                       │  │
│  │   Invest $1,500 this month (vs. $1,000 base)                       │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   OPPORTUNITY SCANNER                                               │  │
│  │   Stocks trading at bigger discounts than the market                │  │
│  │                                                                     │  │
│  │   ┌──────────────────────────────────────────────────────────────┐ │  │
│  │   │ 🔥 NVDA   Market: -12.5%   Stock: -25.3%   Extra Discount: 12.8%│ │
│  │   │    Consider overweighting this month                         │ │  │
│  │   └──────────────────────────────────────────────────────────────┘ │  │
│  │                                                                     │  │
│  │   ┌──────────────────────────────────────────────────────────────┐ │  │
│  │   │ 📊 GOOGL  Market: -12.5%   Stock: -18.1%   Extra Discount: 5.6%│ │  │
│  │   │    Moderate opportunity                                      │ │  │
│  │   └──────────────────────────────────────────────────────────────┘ │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   HISTORICAL CONTEXT                                                │  │
│  │                                                                     │  │
│  │   Past corrections and recoveries:                                  │  │
│  │                                                                     │  │
│  │   ┌──────────────────────────────────────────────────────────────┐ │  │
│  │   │                           S&P 500                            │ │  │
│  │   │   5200 ┤                    ╭──╮                              │ │  │
│  │   │   5000 ┤               ╭────╯  ╰──╮                          │ │  │
│  │   │   4800 ┤          ╭────╯          ╰────                      │ │  │
│  │   │   4600 ┤     ╭────╯                    ← You are here        │ │  │
│  │   │   4400 ┤╭────╯                                               │ │  │
│  │   │        └┴────┴────┴────┴────┴────┴────┴────┴────┴────┴       │ │  │
│  │   │         Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct     │ │  │
│  │   └──────────────────────────────────────────────────────────────┘ │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.5 HISTORY PAGE

Track all past investments and performance over time.

#### Layout Structure
```
┌────────────────────────────────────────────────────────────────────────────┐
│  ← Dashboard                    HISTORY                    [Export All]    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   PERFORMANCE CHART                          [1M] [3M] [1Y] [ALL]   │  │
│  │                                                                     │  │
│  │   ┌──────────────────────────────────────────────────────────────┐ │  │
│  │   │ $50k ┤                                         ╭────         │ │  │
│  │   │      │                                    ╭────╯             │ │  │
│  │   │ $40k ┤                              ╭─────╯  Portfolio       │ │  │
│  │   │      │                         ╭────╯       ─────────        │ │  │
│  │   │ $30k ┤                    ╭────╯            Total Invested   │ │  │
│  │   │      │               ╭────╯                 ═══════════      │ │  │
│  │   │ $20k ┤          ╭────╯                                       │ │  │
│  │   │      │     ╭────╯                                            │ │  │
│  │   │ $10k ┤╭────╯                                                 │ │  │
│  │   │      └┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴    │ │  │
│  │   │       Jan  Mar  May  Jul  Sep  Nov  Jan  Mar  May  Jul       │ │  │
│  │   │       2024                         2025                      │ │  │
│  │   └──────────────────────────────────────────────────────────────┘ │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   INVESTMENT LOG                                                    │  │
│  │                                                                     │  │
│  │   Date        Market      Multiplier   Invested    Cumulative      │  │
│  │   ─────────────────────────────────────────────────────────────────│  │
│  │   Dec 2025    Correction  1.5x         $1,500.00   $41,500.00      │  │
│  │   Nov 2025    Normal      1.0x         $1,000.00   $40,000.00      │  │
│  │   Oct 2025    Normal      1.0x         $1,000.00   $39,000.00      │  │
│  │   Sep 2025    Minor Corr  1.25x        $1,250.00   $38,000.00      │  │
│  │   Aug 2025    Bear Market 2.5x         $2,500.00   $36,750.00      │  │
│  │   Jul 2025    Bear Market 2.5x         $2,500.00   $34,250.00      │  │
│  │   ...                                                               │  │
│  │                                                                     │  │
│  │   [Load More]                                                       │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   STATISTICS                                                        │  │
│  │                                                                     │  │
│  │   Total Invested:         $41,500.00                               │  │
│  │   Months Invested:        18                                        │  │
│  │   Average Monthly:        $2,305.56                                │  │
│  │   Months Above Base:      8 (44%)                                  │  │
│  │   Max Single Investment:  $3,000.00 (Mar 2024, Deep Bear)          │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.6 SETTINGS PAGE

Configure investment parameters and preferences.

#### Layout Structure
```
┌────────────────────────────────────────────────────────────────────────────┐
│  ← Dashboard                    SETTINGS                                   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   INVESTMENT PARAMETERS                                             │  │
│  │   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  │
│  │                                                                     │  │
│  │   Base Monthly Investment                                           │  │
│  │   ┌────────────────────────────────────────┐                       │  │
│  │   │ $ 1,000.00                             │                       │  │
│  │   └────────────────────────────────────────┘                       │  │
│  │   This is your standard monthly contribution in normal markets     │  │
│  │                                                                     │  │
│  │   Investment Goal (Optional)                                        │  │
│  │   ┌────────────────────────────────────────┐                       │  │
│  │   │ $ 60,000.00                            │                       │  │
│  │   └────────────────────────────────────────┘                       │  │
│  │                                                                     │  │
│  │   Benchmark Index                                                   │  │
│  │   ┌────────────────────────────────────────┐                       │  │
│  │   │ S&P 500 (^GSPC)                    ▼   │                       │  │
│  │   └────────────────────────────────────────┘                       │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   MULTIPLIER RULES                                                  │  │
│  │   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  │
│  │                                                                     │  │
│  │   Customize when to increase investments:                           │  │
│  │                                                                     │  │
│  │   Market Condition     Drawdown Range      Multiplier               │  │
│  │   ─────────────────────────────────────────────────────            │  │
│  │   Normal               0% to -5%           [1.0x  ▼]               │  │
│  │   Minor Correction     -5% to -10%         [1.25x ▼]               │  │
│  │   Correction           -10% to -15%        [1.5x  ▼]               │  │
│  │   Significant          -15% to -20%        [2.0x  ▼]               │  │
│  │   Bear Market          -20% to -30%        [2.5x  ▼]               │  │
│  │   Deep Bear            Below -30%          [3.0x  ▼]               │  │
│  │                                                                     │  │
│  │   Maximum Monthly Cap: ┌──────────────┐                            │  │
│  │                        │ $ 5,000.00   │ (Safety limit)             │  │
│  │                        └──────────────┘                            │  │
│  │                                                                     │  │
│  │   [Reset to Defaults]                                              │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │   NOTIFICATIONS                                                     │  │
│  │   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  │
│  │                                                                     │  │
│  │   [✓] Monthly DCA reminder (1st of each month)                     │  │
│  │   [✓] Market condition change alerts                               │  │
│  │   [✓] Individual stock opportunity alerts                          │  │
│  │   [ ] Weekly portfolio summary                                      │  │
│  │                                                                     │  │
│  │   Email: ┌────────────────────────────────────────┐                │  │
│  │          │ your.email@example.com                 │                │  │
│  │          └────────────────────────────────────────┘                │  │
│  │                                                                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│                                             [Cancel]  [Save Settings]      │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Component Library

### 4.1 Buttons

```
Primary Action (Blue):
┌─────────────────────────┐
│   View Full Plan        │  ← Solid blue background, white text
└─────────────────────────┘

Secondary Action (Outline):
┌─────────────────────────┐
│   Export CSV            │  ← Blue border, blue text, transparent
└─────────────────────────┘

Success Action (Green):
┌─────────────────────────┐
│   ✅ Mark as Completed  │  ← Green background, white text
└─────────────────────────┘

Destructive Action (Red):
┌─────────────────────────┐
│   🗑️ Delete             │  ← Red background, white text
└─────────────────────────┘
```

### 4.2 Cards

```
Standard Card:
┌─────────────────────────────────────────┐
│  Card Title                             │
│  ─────────────────────────────────────  │
│                                         │
│  Card content goes here with padding    │
│  all around for breathing room.         │
│                                         │
│  [Action Button]                        │
└─────────────────────────────────────────┘

Specs:
- Border radius: 8px
- Padding: 24px
- Shadow: 0 1px 3px rgba(0,0,0,0.1)
- Background: White (#FFFFFF)
```

### 4.3 Status Indicators

```
Market Status Pills:
┌──────────────┐
│ ⚪ Normal    │  Gray background
└──────────────┘
┌──────────────┐
│ 🔵 Minor     │  Light blue background
└──────────────┘
┌──────────────┐
│ 🟡 Correction│  Amber background
└──────────────┘
┌──────────────┐
│ 🟠 Significant│ Orange background
└──────────────┘
┌──────────────┐
│ 🔴 Bear      │  Red background
└──────────────┘

Stock Action Indicators:
🟢 BUY   - Stock is underweight, recommend buying
🟡 HOLD  - Stock is at or near target
🔴 SELL  - Stock is significantly overweight (rare)
```

### 4.4 Data Display

```
Large Metric:
┌─────────────────────┐
│ Total Value         │  ← Label (small, gray)
│ $45,230.00          │  ← Value (large, bold, black)
│ +13.1%              │  ← Change (medium, green/red)
└─────────────────────┘

Progress Bar:
Current: 22%  ████████████░░░░░░░░  Target: 25%
              ↑ Filled portion     ↑ Empty portion
```

### 4.5 Tables

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Stock   │  Shares  │  Price   │  Value     │  Return   │  Action      │
├─────────────────────────────────────────────────────────────────────────┤
│  AAPL    │  50      │ $185.00  │ $9,250.00  │ +15.6%    │  🟢 Buy      │
│  MSFT    │  30      │ $406.25  │ $12,187.50 │ +16.1%    │  🟡 Hold     │
│  GOOGL   │  40      │ $140.00  │ $5,600.00  │ +7.7%     │  🟢 Buy      │
└─────────────────────────────────────────────────────────────────────────┘

Specs:
- Header: Bold, slightly darker background
- Rows: Alternating white/light gray
- Hover: Light blue highlight
- Borders: Light gray (#E5E7EB)
```

---

## 5. Responsive Design

### 5.1 Breakpoints

| Breakpoint | Width | Layout |
|------------|-------|--------|
| Mobile | < 640px | Single column, stacked cards |
| Tablet | 640px - 1024px | Two columns where possible |
| Desktop | > 1024px | Full layout with sidebar |

### 5.2 Mobile Adaptations

**Dashboard - Mobile View:**
```
┌─────────────────────────┐
│  🏠 Smart DCA      [≡]  │
├─────────────────────────┤
│                         │
│  ┌───────────────────┐  │
│  │ 🟡 CORRECTION     │  │
│  │ -12.5% from ATH   │  │
│  │ Multiplier: 1.5x  │  │
│  └───────────────────┘  │
│                         │
│  ┌───────────────────┐  │
│  │ THIS MONTH        │  │
│  │ $1,500.00         │  │
│  │ [View Details]    │  │
│  └───────────────────┘  │
│                         │
│  ┌───────────────────┐  │
│  │ PORTFOLIO         │  │
│  │ $45,230.00        │  │
│  │ +$5,230 (+13.1%)  │  │
│  └───────────────────┘  │
│                         │
│  [Holdings ↓]           │
│                         │
└─────────────────────────┘
```

**Key Mobile Considerations:**
- Hamburger menu for navigation
- Cards stack vertically
- Tables become card lists
- Touch-friendly buttons (min 44px)
- Simplified charts

---

## 6. Animations & Micro-interactions

### 6.1 Loading States

```
Skeleton Loading:
┌─────────────────────────────────────────┐
│  ░░░░░░░░░░░░░░░░░░░░                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│                                         │
│  ░░░░░░░░░░░░     ░░░░░░░░░░░░          │
│  ━━━━━━━━━━━      ━━━━━━━━━━━           │
└─────────────────────────────────────────┘
Animated shimmer effect left-to-right
```

### 6.2 Transitions

| Element | Transition | Duration |
|---------|------------|----------|
| Page change | Fade | 200ms |
| Card hover | Lift shadow | 150ms |
| Button hover | Color darken | 100ms |
| Dropdown open | Slide down | 200ms |
| Alert appear | Slide in from top | 300ms |

### 6.3 Feedback

```
Success Toast:
┌─────────────────────────────────────────┐
│ ✅  Investment logged successfully!     │ → Slides in, auto-dismisses
└─────────────────────────────────────────┘

Error Toast:
┌─────────────────────────────────────────┐
│ ❌  Failed to fetch prices. Retry?      │ → Red accent, manual dismiss
└─────────────────────────────────────────┘
```

---

## 7. Accessibility Requirements

### 7.1 WCAG 2.1 AA Compliance

- **Color Contrast:** Minimum 4.5:1 for text
- **Focus Indicators:** Visible focus rings on all interactive elements
- **Screen Readers:** All images have alt text, ARIA labels on icons
- **Keyboard Navigation:** Full functionality without mouse
- **Text Sizing:** Supports 200% zoom without horizontal scroll

### 7.2 Color Blindness Considerations

- Don't rely solely on color to convey information
- Add icons/text labels alongside color indicators:
  - 🟢 Buy (not just green)
  - 🟡 Hold (not just yellow)
  - 🔴 Caution (not just red)

---

## 8. Empty States & Error Handling

### 8.1 Empty States

**No Holdings:**
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                      📊                                     │
│                                                             │
│            No holdings yet                                  │
│                                                             │
│    Add your first stock to get started with                │
│    your personalized DCA plan.                              │
│                                                             │
│              [+ Add Your First Stock]                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**No History:**
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                      📅                                     │
│                                                             │
│            No investment history                            │
│                                                             │
│    Once you log your first DCA investment,                 │
│    you'll see your history here.                            │
│                                                             │
│              [Log First Investment]                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 8.2 Error States

**API Error:**
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                      ⚠️                                      │
│                                                             │
│        Unable to fetch latest prices                        │
│                                                             │
│    We couldn't connect to the market data service.         │
│    Showing last known prices from 2 hours ago.              │
│                                                             │
│              [Try Again]    [Use Cached Data]               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. Typography

### 9.1 Font Stack

```css
Primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif
Monospace (numbers): 'JetBrains Mono', 'Fira Code', monospace
```

### 9.2 Type Scale

| Use | Size | Weight | Line Height |
|-----|------|--------|-------------|
| Page Title | 32px | Bold (700) | 1.2 |
| Section Header | 24px | Semibold (600) | 1.3 |
| Card Title | 18px | Semibold (600) | 1.4 |
| Body Text | 16px | Regular (400) | 1.5 |
| Small/Caption | 14px | Regular (400) | 1.4 |
| Label | 12px | Medium (500) | 1.3 |
| Large Number | 36px | Bold (700) | 1.1 |

---

## 10. Final Design Mockup - High Fidelity

### Desktop Dashboard (Visual Reference)

```
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │  💰 Smart DCA                           🔔 Alerts  👤 John D.        │  ║
║  │  ──────────────────────────────────────────────────────────────────  │  ║
║  │  [Dashboard]  [Portfolio]  [DCA Planner]  [Market]  [History]        │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ╭────────────────────────────────────────────────────────────────────╮   ║
║  │  🟡 MARKET CORRECTION  │  S&P 500 down 12.5% from ATH              │   ║
║  │     Your investment multiplier is now 1.5x — Great time to invest! │   ║
║  ╰────────────────────────────────────────────────────────────────────╯   ║
║                                                                            ║
║  ┌────────────────────────────┐  ┌────────────────────────────────────┐   ║
║  │  📅 THIS MONTH             │  │  📊 PORTFOLIO VALUE                │   ║
║  │  ════════════════════════  │  │  ════════════════════════════════  │   ║
║  │                            │  │                                    │   ║
║  │  Base:        $1,000.00    │  │  Total Value:    $45,230.00       │   ║
║  │  Multiplier:  × 1.5        │  │  Total Invested: $40,000.00       │   ║
║  │  ──────────────────────    │  │  ──────────────────────────────   │   ║
║  │  INVEST:      $1,500.00    │  │  Return: +$5,230.00  (+13.1%)     │   ║
║  │                            │  │          🟢 On track              │   ║
║  │  [📋 View Full Plan →]     │  │                                    │   ║
║  │                            │  │  ████████████████░░░░ 75% to goal │   ║
║  └────────────────────────────┘  └────────────────────────────────────┘   ║
║                                                                            ║
║  ┌────────────────────────────────────────────────────────────────────┐   ║
║  │  💼 YOUR HOLDINGS                                    [Manage →]    │   ║
║  │  ══════════════════════════════════════════════════════════════    │   ║
║  │                                                                    │   ║
║  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐           │   ║
║  │  │  AAPL  │ │  MSFT  │ │ GOOGL  │ │  AMZN  │ │  NVDA  │           │   ║
║  │  │  22%   │ │  27%   │ │  18%   │ │  16%   │ │  17%   │           │   ║
║  │  │ +2.3%  │ │ -1.1%  │ │ +0.8%  │ │ +1.5%  │ │ -3.2%  │           │   ║
║  │  │ 🟢 Buy │ │ 🟡 Hold│ │ 🟢 Buy │ │ 🟡 Hold│ │ 🟡 Hold│           │   ║
║  │  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘           │   ║
║  │                                                                    │   ║
║  └────────────────────────────────────────────────────────────────────┘   ║
║                                                                            ║
║  ┌────────────────────────────────────────────────────────────────────┐   ║
║  │  🎯 QUICK ACTIONS                                                  │   ║
║  │                                                                    │   ║
║  │  [📋 View Full Plan]  [✅ Log Investment]  [📈 Market Analysis]    │   ║
║  │                                                                    │   ║
║  └────────────────────────────────────────────────────────────────────┘   ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

---

## 11. Next Steps for Development

1. **Design System Setup**
   - Create Figma/Sketch component library
   - Define CSS variables for colors, spacing
   - Build reusable React/Vue components

2. **Prototype**
   - Interactive Figma prototype for user testing
   - Test with 3-5 potential users
   - Iterate based on feedback

3. **Development Handoff**
   - Export assets (icons, images)
   - Document component specs
   - Create Storybook for component library

---

*This UX document should be used alongside the PRD for development. All designs prioritize clarity and actionability for investment decisions.*
