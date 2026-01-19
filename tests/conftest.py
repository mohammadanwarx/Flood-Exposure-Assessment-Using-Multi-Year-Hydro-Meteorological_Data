"""Test configuration and fixtures."""

import pytest
from pathlib import Path


@pytest.fixture
def sample_data_dir():
    """Fixture providing sample data directory path."""
    return Path(__file__).parent / "data"


@pytest.fixture
def output_dir(tmp_path):
    """Fixture providing temporary output directory."""
    output = tmp_path / "outputs"
    output.mkdir(exist_ok=True)
    return output
