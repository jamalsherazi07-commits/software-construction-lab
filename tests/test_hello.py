"""Unit tests for hello module."""

from hello import greet


def test_greet() -> None:
    """Test that greet returns 'Hello, World!'."""
    assert greet("World") == "Hello, World!"
