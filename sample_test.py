"""
Sample Test
"""

import pytest
import sample


def test_sum_two_positive():
    """Test the sum_two function"""
    assert sample.sum_two(1) == 3


def test_sum_two_negative():
    """Negative test of sum_two function"""
    assert sample.sum_two(-2) == 0
