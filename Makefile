.PHONY: install build clean test verify

# Default target: install with verification
install:
	@echo "[*] Verifying environment configuration..."
	@source .env 2>/dev/null; python -c "from config.loader import verify; verify()"
	@echo "[*] Installing dependencies..."
	pip install -r requirements.txt
	@echo "[*] Building package..."
	python setup.py bdist_wheel
	@echo "[+] Build complete"

# Verify environment configuration
verify:
	@echo "[*] Running environment verification..."
	@source .env 2>/dev/null; python -c "from config.loader import verify; verify()"
	@echo "[+] Verification complete"

# Run tests
test:
	python -m pytest tests/ -v

# Clean build artifacts
clean:
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Development install (editable)
dev:
	pip install -e .
	pip install -r requirements.txt
