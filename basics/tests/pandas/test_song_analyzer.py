import pytest
import pandas as pd
from src.pandas.song_analyzer import SongAnalyzer


@pytest.fixture
def sample_song_data():
    """Fixture to provide test song data"""
    return {
        'Song': [
            'Short Song',
            'Medium Song',
            'Long Song',
            'Very Long Song'
        ],
        'Artist': [
            'Artist A',
            'Artist B',
            'Artist C',
            'Artist D'
        ],
        'Release_Date': [
            '2025-01-01',
            '2025-01-02',
            '2025-01-03',
            '2025-01-04'
        ],
        'Length': [
            '2:30',  # 2.5 minutes
            '4:45',  # 4.75 minutes
            '6:15',  # 6.25 minutes
            '8:00'   # 8.0 minutes
        ]
    }


@pytest.fixture
def song_analyzer(sample_song_data):
    """Fixture to provide a SongAnalyzer instance with sample data"""
    analyzer = SongAnalyzer()
    analyzer.load_songs_data(sample_song_data)
    return analyzer


def test_get_songs_longer_than_empty_analyzer():
    """Test get_songs_longer_than with no data loaded"""
    analyzer = SongAnalyzer()
    result = analyzer.get_songs_longer_than(5)
    assert isinstance(result, pd.DataFrame)
    assert result.empty


def test_get_songs_longer_than_no_matches(song_analyzer):
    """Test when no songs match the duration criteria"""
    result = song_analyzer.get_songs_longer_than(10)
    assert isinstance(result, pd.DataFrame)
    assert result.empty


def test_get_songs_longer_than_all_matches(song_analyzer):
    """Test when all songs match the duration criteria"""
    result = song_analyzer.get_songs_longer_than(2)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 4
    assert list(result.columns) == ['Song', 'Artist', 'Length']


def test_get_songs_longer_than_some_matches(song_analyzer):
    """Test when some songs match the duration criteria"""
    result = song_analyzer.get_songs_longer_than(6)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert 'Very Long Song' in result['Song'].values
    assert 'Long Song' in result['Song'].values
    assert 'Short Song' not in result['Song'].values


def test_get_songs_longer_than_exact_match(song_analyzer):
    """Test with duration that matches a song exactly"""
    result = song_analyzer.get_songs_longer_than(6.25)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert 'Very Long Song' in result['Song'].values
