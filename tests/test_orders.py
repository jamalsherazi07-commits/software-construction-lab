"""Tests for the orders module."""

import pytest

from orders import calculate_order_total


def test_order_total() -> None:
    sample_order = {
        "items": [
            {"price": 25.0, "qty": 2},
            {"price": 40.0, "qty": 1},
            {"price": -5.0, "qty": 3},
        ],
        "member": True,
        "country": "PK",
    }
    assert calculate_order_total(sample_order) == pytest.approx(86.0)
