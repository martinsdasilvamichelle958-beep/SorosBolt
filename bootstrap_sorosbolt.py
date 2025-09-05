import os, textwrap, zipfile, json

ROOT = os.path.join(os.path.expanduser("~"), "Documents", "SorosBolt_Complete_All")

DIRS = [
    "", "core", "strategies", "app", "integrations", "news", "backtest", "scripts", "logs", "reports"
]

def W(relpath: str, content: str):
    abspath = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(abspath), exist_ok=True)
    with open(abspath, "w", encoding="utf-8") as f:
        f.write(textwrap.dedent(content).lstrip("\n"))

# 1) Criar estrutura
for d in DIRS:
    os.makedirs(os.path.join(ROOT, d), exist_ok=True)

# 2) Raiz
W("requirements.txt", """
python-binance==1.0.19
python-dotenv==1.0.1
pandas==2.2.2
numpy==1.26.4
ta==0.11.0
fastapi==0.111.0
uvicorn==0.30.1
requests==2.32.3
feedparser==6.0.11
jinja2==3.1.4
""")

W(".env.example", """
# Binance
BINANCE_API_KEY=d7a67dfb17204cd09aac9b96664495f6500de85e

BINANCE_API_SECRET=BBF3lgPOrcuPcFhDlWZbajZvjyyZexlVT45UtCVMThggl2CYw1cqj7aUNtcIFzzU


MODE=TESTNET
DRY_RUN=True

# Ativo e dados
BASE_SYMBOL=BTCUSDT
CANDLE_INTERVAL=1m
CANDLE_LIMIT=400

# Risco e proteções
RISK_PER_TRADE_PCT=0.5
MAX_DAILY_LOSS_PCT=3.0
STOP_LOSS_PCT=0.8
TAKE_PROFIT_PCT=1.2

# Multi-timeframe
USE_MTF=True
MTF_INTERVAL=5m
ADX_TREND_TH=18
DONCHIAN_N=20
ATR_PERIOD=14

# Piramidagem
PYRAMID_ENABLED=False
PYRAMID_MAX=2
PYRAMID_STEP_ATR=0.5

# Drawdown throttle
DD_CUT_1=3.0
DD_CUT_1_FACTOR=0.7
DD_CUT_2=6.0
DD_CUT_2_FACTOR=0.4

# Anti-manipulação
DEPTH_LIMIT=50
VOL_SPIKE_MULT=2.5
SPREAD_MAX_PCT=0.15
WALL_RATIO_TH=0.18
WALL_DROP_SEC=30

# Tempo máximo de posição
MAX_POSITION_MINUTES=60

# Painel
ENABLE_LOCAL_APP=True
APP_HOST=127.0.0.1
APP_PORT=8000

# Notícias / Telegram
NEWS_ENABLE=True
NEWS_POLL_SEC=120
TELEGRAM_BOT_TOKEN=8220821635:AAGh55lmAqYl53L1A-QUluLNUFykyeG0d0o

TELEGRAM_CHAT_ID=8220821635
CRYPTOPANIC_TOKEN=
CRYPTOPANIC_FILTER=important,hot
NEWS_KEYWORDS=BTC,Bitcoin,ETF,SEC,Binance,Halving

# Avançado
WEBSOCKET_ENABLE=True
WS_BOOK_DEPTH=10
ANTI_SCORE_BLOCK_TH=0.70
SERVER_TIME_SYNC_SEC=300
TRAIL_ATR_MULT=1.2
TRAIL_RECREATE_MIN_PCT=0.15
ENFORCE_MIN_NOTIONAL=True
MAX_SLIPPAGE_BPS=15
FEES_RATE=0.001

# Telegram polling
COMMANDS_ENABLE=True
TELEGRAM_POLL_SEC=5
""")

W("README.md", """
# SorosBolt Oráculo Visionário
- Bot modular com engine de execução, risk management, anti-manipulação, 3 estratégias, painel FastAPI, Telegram e backtest PRO.

## Rodar
