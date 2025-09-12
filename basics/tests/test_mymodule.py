"""Test cases for the mymodule module."""

import sys
import os
from hamcrest import assert_that, equal_to

# Add the src directory to the Python path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mymodule import square, doubler


class TestSquare:
    """Test cases for the square function."""
    
    def test_square_positive_number(self):
        """Test squaring a positive number."""
        result = square(4)
        assert_that(result, equal_to(16))
    
    def test_square_negative_number(self):
        """Test squaring a negative number."""
        result = square(-3)
        assert_that(result, equal_to(9))
    
    def test_square_zero(self):
        """Test squaring zero."""
        result = square(0)
        assert_that(result, equal_to(0))
    
    def test_square_float(self):
        """Test squaring a float number."""
        result = square(2.5)
        assert_that(result, equal_to(6.25))
    
    def test_square_one(self):
        """Test squaring one."""
        result = square(1)
        assert_that(result, equal_to(1))


class TestDoubler:
    """Test cases for the doubler function."""
    
    def test_doubler_positive_number(self):
        """Test doubling a positive number."""
        result = doubler(5)
        assert_that(result, equal_to(10))
    
    def test_doubler_negative_number(self):
        """Test doubling a negative number."""
        result = doubler(-4)
        assert_that(result, equal_to(-8))
    
    def test_doubler_zero(self):
        """Test doubling zero."""
        result = doubler(0)
        assert_that(result, equal_to(0))
    
    def test_doubler_float(self):
        """Test doubling a float number."""
        result = doubler(3.5)
        assert_that(result, equal_to(7.0))
    
    def test_doubler_one(self):
        """Test doubling one."""
        result = doubler(1)
        assert_that(result, equal_to(2))