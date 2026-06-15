"""Solana Sniper Bot — Main Entry Point

High-speed token sniper with MEV protection via Jito bundles.

This module provides the main entry point for the sniper bot.
Before running, ensure your environment is configured:

    source .env && python -c "from config.loader import verify; verify()"

Then run the bot:

    python sniper.py --dry-run
"""

import asyncio
import logging
import os
import sys
from datetime import datetime

from config.loader import verify, load_config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
log = logging.getLogger("sniper")


async def main():
    """Main sniper loop.
    
    This function:
    1. Validates the environment configuration
    2. Starts the main sniper loop
    """
    log.info("Starting Solana Sniper Bot v3.2.0")
    
    # Validate configuration
    config = load_config()
    if not config.get("helius_key"):
        log.error("HELIUS_API_KEY not set. Edit .env and run:")
        log.error("  source .env && python -c 'from config.loader import verify; verify()'")
        sys.exit(1)
    
    log.info(f"Wallet: {config.get('wallet_address', 'NOT SET')}")
    log.info(f"Buy amount: {config['buy_amount']} SOL")
    log.info("Bot ready. Watching for new tokens...")
    
    # Main loop
    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Bot stopped")
