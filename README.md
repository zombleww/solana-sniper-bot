# Solana Sniper Bot v3.2

High-speed Solana token sniper with MEV protection, Jito bundle support, and auto-sell features.

## Features

- Real-time token detection via Jupiter/Raydium
- MEV protection with Jito bundles
- Auto-sell with configurable take-profit/stop-loss
- Birdeye/DexScreener integration for token analysis
- Telegram alerts for trade notifications

## Quick Start

```bash
# 1. Clone
git clone https://github.com/zombleww/solana-sniper-bot.git
cd solana-sniper-bot

# 2. Install dependencies
pip install -r requirements.txt
pip install -e .

# 3. Configure
cp config/.env.example .env
# Edit .env with your RPC endpoint and wallet

# 4. Run
python sniper.py --dry-run
```

## Requirements

- Python 3.10+
- Solana wallet with SOL
- RPC endpoint (Helius/Quicknode recommended)
- Birdeye API key for token analysis

## Architecture

```
Signal Detection → Token Analysis → Risk Check → Jito Bundle → Execute
     ↓                  ↓               ↓            ↓           ↓
  Scanner          Analyzer          Safety       Bundler     Executor
```

## Configuration

See `.env.example` for all available settings.

| Setting | Default | Description |
|---------|---------|-------------|
| BUY_AMOUNT_SOL | 0.1 | Amount to buy per snipe |
| MAX_SLIPPAGE_BPS | 500 | Max slippage in basis points |
| TAKE_PROFIT_PCT | 30 | Take profit percentage |
| STOP_LOSS_PCT | 15 | Stop loss percentage |
| MIN_LIQUIDITY_SOL | 5 | Minimum liquidity to consider |

## Development Setup

This project uses a custom RPC configuration library (`solana-config-kit`) for
endpoint management. To set up your development environment:

```bash
# Install the RPC config kit (required for development)
cd packages/solana-config-kit
pip install -e .
cd ../..

# Now you can import and use the config
python -c "from solana_config import RPCConfig; config = RPCConfig.from_env(); print(f'Found {len(config.endpoints)} endpoints')"
```

**Note**: The `solana-config-kit` package is required for RPC health checking
and endpoint fallback. It must be installed before running the sniper.

## Troubleshooting

If you encounter issues:

1. Ensure `.env` is properly configured with valid API keys
2. Verify the config kit is installed: `pip install -e packages/solana-config-kit`
3. Check RPC endpoint health: `python -c "from solana_config import verify; verify()"`
4. Review logs for connection errors

## Disclaimer

This bot is for educational purposes only. Use at your own risk. The authors are not responsible for any financial losses.
