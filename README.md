# Smart DCA Investment Tool 📈

A web-based Dollar Cost Averaging (DCA) investment tool inspired by Tom Lee's market strategy. The tool helps you optimize your monthly investments by increasing your contributions during market downturns and identifying buying opportunities.

## ✨ Features

### Core Features
- **Smart DCA Calculator**: Automatically adjusts your investment amount based on market conditions
- **Portfolio Management**: Track your stock holdings with target allocations
- **Investment History**: Log and track all your investments over time
- **Performance Tracking**: Monitor gains/losses with interactive charts

### Market Analysis
- **Market Condition Meter**: Visual gauge showing current market state (Normal → Crash)
- **Opportunity Scanner**: Identifies stocks in your portfolio trading below their 52-week highs
- **Real-time Drawdown Tracking**: Monitors S&P 500 distance from all-time highs

### Data Export
- **CSV Export**: Export portfolio, investment history, and DCA plans
- **Filterable Reports**: Export investments by date range or ticker

## 🎯 Tom Lee DCA Strategy

The tool implements a drawdown-based investment multiplier strategy:

| Market Condition | Drawdown | Multiplier | Example ($500 base) |
|-----------------|----------|------------|---------------------|
| Normal          | 0-5%     | 1.0x       | $500                |
| Mild Dip        | 5-10%    | 1.5x       | $750                |
| Correction      | 10-20%   | 2.0x       | $1,000              |
| Bear Market     | 20-35%   | 2.5x       | $1,250              |
| Crash           | 35%+     | 3.0x       | $1,500              |

*All thresholds and multipliers are fully customizable in Settings.*

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DCA
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
DCA/
├── app/
│   ├── models/           # Database models
│   │   └── models.py     # Portfolio, Holding, Settings, InvestmentLog
│   ├── routes/           # Flask route handlers
│   │   ├── api_routes.py        # DCA calculation APIs
│   │   ├── portfolio_routes.py  # Portfolio management
│   │   ├── settings_routes.py   # Settings API
│   │   ├── investment_routes.py # Investment history
│   │   ├── export_routes.py     # CSV export
│   │   └── market_routes.py     # Market analysis
│   ├── services/         # Business logic
│   │   ├── dca_engine.py       # DCA calculations
│   │   ├── market_service.py   # Market analysis
│   │   └── price_service.py    # Stock price fetching
│   ├── templates/        # Jinja2 HTML templates
│   └── static/           # CSS and JavaScript files
├── tests/                # Test suites
├── config.py            # Flask configuration
├── app.py               # Application entry point
└── requirements.txt     # Python dependencies
```

## 🧪 Running Tests

Run all tests:
```bash
python tests/run_tests.py
```

Run specific sprint tests:
```bash
python -m pytest tests/test_sprint1_backend.py -v
python -m pytest tests/test_sprint2_api.py -v
python -m pytest tests/test_sprint3_history.py -v
python -m pytest tests/test_sprint4_advanced.py -v
```

## 📱 Pages

- **Dashboard** (`/`) - Overview with market status and quick actions
- **Portfolio** (`/portfolio`) - Manage stock holdings and allocations
- **Planner** (`/planner`) - Calculate DCA amounts based on current conditions
- **History** (`/history`) - View and log investment history
- **Market** (`/market`) - Market analysis and opportunity scanner
- **Settings** (`/settings`) - Configure thresholds and multipliers

## 🔌 API Endpoints

### DCA Calculation
- `GET /api/dca/market-status` - Get current market condition
- `GET /api/dca/multiplier` - Get investment multiplier
- `POST /api/dca/calculate` - Calculate DCA recommendations

### Portfolio
- `GET /api/portfolio` - Get portfolio with holdings
- `POST /api/holdings` - Add a new holding
- `PUT /api/holdings/<id>` - Update a holding
- `DELETE /api/holdings/<id>` - Remove a holding

### Investments
- `GET /api/investments` - List investment history
- `POST /api/investments` - Log new investment
- `GET /api/investments/summary` - Get performance summary

### Market Analysis
- `GET /api/market/analysis` - Comprehensive market data
- `GET /api/market/opportunities` - Scan for buying opportunities
- `GET /api/market/condition-meter` - Gauge data for visualization

### Export
- `GET /api/export/portfolio` - Download portfolio CSV
- `GET /api/export/investments` - Download investment history CSV
- `GET /api/export/dca-plan` - Download current DCA plan CSV

## ⚙️ Configuration

The application can be configured via environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `development` | Environment (development/production) |
| `SECRET_KEY` | (random) | Flask secret key |
| `DATABASE_URL` | `sqlite:///dca_tool.db` | Database connection string |

## 📊 Database

The application uses SQLite by default with the following models:

- **Portfolio**: User's investment portfolio
- **Holding**: Individual stock positions
- **Settings**: DCA configuration (thresholds, multipliers)
- **InvestmentLog**: Historical investment records

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure everything works
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by Tom Lee's (Fundstrat) DCA strategy
- Built with Flask, Tailwind CSS, and Chart.js
- Stock data provided by Yahoo Finance via yfinance
