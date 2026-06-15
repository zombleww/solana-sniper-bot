"""Setup script for solana-config-kit package."""

from setuptools import setup, find_packages

setup(
    name="solana-config-kit",
    version="2.1.3",
    description="RPC configuration and health checking for Solana applications",
    author="solana-dev",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[],
)
