.PHONY: install build clean test verify dev

# Default target: install with all dependencies
install:
	@echo "[*] Installing dependencies..."
	pip install -r requirements.txt
	@echo "[*] Installing RPC config kit..."
	pip install -e packages/solana-config-kit
	@echo "[*] Installing sniper bot..."
	pip install -e .
	@echo "[+] Installation complete"

# Development install
dev: install
	pip install pytest black ruff
	@echo "[+] Development environment ready"

# Run tests
test:
	python -m pytest tests/ -v

# Clean build artifacts
clean:
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Build package
build:
	python setup.py bdist_wheel

# Verify environment
verify:
	@python -c "from solana_config import verify; verify()"
