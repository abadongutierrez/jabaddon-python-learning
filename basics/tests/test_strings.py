import pytest
import sys
import os

# Add the src directory to the Python path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from strings import reverse_string


class TestReverseString:
    """Test cases for the reverse_string function."""
    
    def test_reverse_basic_string(self):
        """Test reversing a basic string."""
        result = reverse_string("hello")
        expected = "olleh"
        assert result == expected
    
    def test_reverse_with_spaces(self):
        """Test reversing a string with spaces."""
        result = reverse_string("hello world")
        expected = "dlrow olleh"
        assert result == expected
    
    def test_reverse_with_punctuation(self):
        """Test reversing a string with punctuation."""
        result = reverse_string("Hello, World!")
        expected = "!dlroW ,olleH"
        assert result == expected
    
    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        result = reverse_string("")
        expected = ""
        assert result == expected
    
    def test_reverse_single_character(self):
        """Test reversing a single character."""
        result = reverse_string("a")
        expected = "a"
        assert result == expected
    
    def test_reverse_palindrome(self):
        """Test reversing a palindrome."""
        result = reverse_string("racecar")
        expected = "racecar"
        assert result == expected
    
    def test_reverse_with_numbers(self):
        """Test reversing a string with numbers."""
        result = reverse_string("abc123")
        expected = "321cba"
        assert result == expected
    
    def test_reverse_with_special_characters(self):
        """Test reversing a string with special characters."""
        result = reverse_string("@#$%^&*()")
        expected = ")(*&^%$#@"
        assert result == expected
    
    def test_reverse_unicode_characters(self):
        """Test reversing a string with unicode characters."""
        result = reverse_string("héllo")
        expected = "olléh"
        assert result == expected


def test_reverse_string_original_example():
    """Test the original example from the code."""
    result = reverse_string("Hello Python!")
    expected = "!nohtyP olleH"
    assert result == expected


# Parametrized test for multiple test cases
@pytest.mark.parametrize("input_string,expected", [
    ("python", "nohtyp"),
    ("Programming", "gnimmargorP"),
    ("12345", "54321"),
    ("  spaces  ", "  secaps  "),
    ("MixedCASE", "ESACdexiM"),
])
def test_reverse_string_parametrized(input_string, expected):
    """Parametrized test with multiple input/expected pairs."""
    assert reverse_string(input_string) == expected
