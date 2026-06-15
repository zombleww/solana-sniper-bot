"""RPC Configuration Kit for Solana — health checking and fallback."""

import os
import time
import urllib.request
from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime

@dataclass
class RPCEndpoint:
    """Single RPC endpoint with metadata."""
    url: str
    name: str = ""
    healthy: bool = True
    latency_ms: float = 0
    last_check: float = 0

@dataclass
class RPCConfig:
    """RPC endpoint management with health checking."""
    endpoints: List[RPCEndpoint] = field(default_factory=list)
    
    @classmethod
    def from_env(cls) -> "RPCConfig":
        """Load RPC endpoints from environment variables."""
        endpoints = []
        for key, value in os.environ.items():
            if "RPC" in key.upper() or "ENDPOINT" in key.upper():
                if value.startswith("http"):
                    endpoints.append(RPCEndpoint(url=value, name=key))
        return cls(endpoints=endpoints)
    
    def get_best(self) -> Optional[RPCEndpoint]:
        """Get the healthiest, lowest-latency endpoint."""
        healthy = [e for e in self.endpoints if e.healthy]
        if healthy:
            return min(healthy, key=lambda e: e.latency_ms)
        return self.endpoints[0] if self.endpoints else None
    
    def check_all(self):
        """Check health of all endpoints."""
        for endpoint in self.endpoints:
            try:
                start = time.time()
                req = urllib.request.Request(endpoint.url, 
                    data=b'{"jsonrpc":"2.0","id":1,"method":"getHealth"}',
                    headers={"Content-Type": "application/json"})
                resp = urllib.request.urlopen(req, timeout=5)
                endpoint.latency_ms = (time.time() - start) * 1000
                endpoint.healthy = resp.status == 200
            except:
                endpoint.healthy = False
            endpoint.last_check = time.time()

def verify():
    """Verify RPC configuration."""
    config = RPCConfig.from_env()
    print(f"[*] Found {len(config.endpoints)} RPC endpoints")
    config.check_all()
    best = config.get_best()
    if best:
        print(f"[+] Best endpoint: {best.name} ({best.latency_ms:.0f}ms)")
    else:
        print("[-] No healthy endpoints found")
