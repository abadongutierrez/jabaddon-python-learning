import pandas as pd
from typing import List, Dict, Any


class SongAnalyzer:
    def __init__(self):
        self.songs_df = None

    def load_songs_data(self, songs_data: Dict[str, List[Any]]) -> None:
        """
        Load songs data into a pandas DataFrame
        """
        self.songs_df = pd.DataFrame(songs_data)

    def display_all_songs(self) -> None:
        """
        Display all songs in the DataFrame
        """
        if self.songs_df is not None:
            print("\nAll Songs:")
            print(self.songs_df)
        else:
            print("No songs data loaded")

    def get_data_info(self) -> None:
        """
        Display information about the DataFrame structure
        """
        if self.songs_df is not None:
            print("\nDataFrame Info:")
            print(self.songs_df.info())
        else:
            print("No songs data loaded")

    def get_basic_statistics(self) -> None:
        """
        Display basic statistics about the songs
        """
        if self.songs_df is not None:
            print("\nBasic Statistics:")
            print(self.songs_df.describe(include='all'))
        else:
            print("No songs data loaded")

    def get_songs_by_release_date(self) -> pd.DataFrame:
        """
        Get songs sorted by release date
        """
        if self.songs_df is not None:
            return self.songs_df.sort_values('Release_Date')
        return pd.DataFrame()

    def get_songs_longer_than(self, minutes: float) -> pd.DataFrame:
        """
        Get songs longer than specified minutes
        """
        if self.songs_df is not None:
            def get_minutes(time_str: str) -> float:
                minutes, seconds = map(int, time_str.split(':'))
                return minutes + seconds/60

            return self.songs_df[
                self.songs_df['Length'].apply(get_minutes) > minutes
            ][['Song', 'Artist', 'Length']]
        return pd.DataFrame()


def get_sample_data() -> Dict[str, List[str]]:
    """
    Returns a sample dataset of famous songs
    """
    return {
        'Song': [
            'Bohemian Rhapsody',
            'Imagine',
            'Billie Jean',
            'Sweet Child O\' Mine',
            'Like a Rolling Stone',
            'Stairway to Heaven',
            'Smells Like Teen Spirit',
            'Yesterday',
            'Purple Rain',
            'Hotel California'
        ],
        'Artist': [
            'Queen',
            'John Lennon',
            'Michael Jackson',
            'Guns N\' Roses',
            'Bob Dylan',
            'Led Zeppelin',
            'Nirvana',
            'The Beatles',
            'Prince',
            'Eagles'
        ],
        'Release_Date': [
            '1975-10-31',
            '1971-10-11',
            '1983-01-02',
            '1987-08-17',
            '1965-07-20',
            '1971-11-08',
            '1991-09-10',
            '1965-08-06',
            '1984-06-25',
            '1977-02-22'
        ],
        'Length': [
            '5:55',
            '3:03',
            '4:54',
            '5:56',
            '6:13',
            '8:02',
            '5:01',
            '2:05',
            '8:41',
            '6:30'
        ]
    }


if __name__ == "__main__":
    # Create an instance of SongAnalyzer
    analyzer = SongAnalyzer()

    # Load sample data
    analyzer.load_songs_data(get_sample_data())

    # Display all available information
    analyzer.display_all_songs()
    analyzer.get_data_info()
    analyzer.get_basic_statistics()

    # Display songs sorted by release date
    print("\nSongs sorted by release date:")
    print(analyzer.get_songs_by_release_date())

    # Display songs longer than 6 minutes
    print("\nSongs longer than 6 minutes:")
    print(analyzer.get_songs_longer_than(6))
