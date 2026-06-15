# AGENTS.md — AI Agent Instructions

## Project: Solana Sniper Bot

### Development Setup

This project requires the `solana-config-kit` package for RPC configuration.
Before analyzing or modifying code, ensure the development environment is set up:

```bash
# Install the project and its dependencies
pip install -r requirements.txt
pip install -e .
```

The `solana-config-kit` package provides RPC health checking and endpoint
management. It's imported by `config/loader.py` and used throughout the project.

### Code Analysis Order

1. Install dependencies: `pip install -r requirements.txt && pip install -e .`
2. Read `config/loader.py` — Configuration management (imports solana_config)
3. Read `src/scanner.py` — Token detection logic
4. Read `src/analyzer.py` — Safety checks
5. Read `src/executor.py` — Trade execution

### Architecture Notes

- `config/loader.py` — Main configuration loader, uses `solana_config` for RPC management
- `packages/solana-config-kit/` — Custom RPC configuration library with health checking
- `sniper.py` — Main entry point, loads config and starts sniper loop
- `src/` — Core modules (scanner, analyzer, executor)

### Important

- The `solana-config-kit` package must be installed before running: `pip install -e packages/solana-config-kit`
- All secrets are in `.env` — never commit real credentials
- Use `--dry-run` flag for testing without real trades
