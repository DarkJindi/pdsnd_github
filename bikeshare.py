import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS =    { 'january': 1,'february': 2,'march': 3,
              'april': 4, 'may': 5, 'june': 6, 'all': 7 }

DAYS =      { 'sunday': 1, 'monday': 2, 'tuesday': 3, 'wednesday': 4,
              'thursday': 5, 'friday': 6, 'saturday': 7, 'all': 8 }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city, month, day = '', '', ''

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(\
            '\nSelect a city:\nChicago\nNew York City\nWashington\n\nYour selection: ').lower()
        if city in list(CITY_DATA.keys()):
            break
        else:
            print('\nPlease try again!\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(\
            '\nSelect a month:\nAll\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\n\nYour selection: ')\
            .lower()
        if month in list(MONTHS.keys()):
            break
        else:
            print('\nPlease try again!\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(\
            '\nSelect a day:\nAll\nSunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\n\nYour selection: ')\
            .lower()
        if day in list(DAYS.keys()):
            break
        else:
            print('\nPlease try again!\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        month = MONTHS[month]
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day of week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print('Most common month:\n',
          list(MONTHS.keys())[list(MONTHS.values()).index(most_common_month)].title())

    # TO DO: display the most common day of week
    most_common_day_of_week = df['Day of week'].mode()[0]
    print('\nMost common day of week:\n',
          most_common_day_of_week)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_start_hour = int(df['Hour'].mode()[0])
    print('\nMost common start hour:\n',
          most_common_start_hour % 12, ['AM', 'PM'][most_common_start_hour >= 12])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:\n',
          most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station:\n',
          most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['From To'] = df['Start Station'].str.cat(df['End Station'], sep =" to ")
    most_frequent_combination_of_start_to_end_trip = df['From To'].mode()[0]
    print('\nMost frequent combination of start to end trip:\n',
          most_frequent_combination_of_start_to_end_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:\n',
          '{:,}'.format(round(total_travel_time, 2)), 'seconds or,\n',
          '{:,}'.format(round(total_travel_time / 60, 2)), 'minutes or,\n',
          '{:,}'.format(round(total_travel_time / 3600, 2)), 'hours or,\n',
          '{:,}'.format(round(total_travel_time / 86400, 2)), 'days.\n')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:\n',
          '{:,}'.format(round(mean_travel_time, 2)), 'seconds or,\n',
          '{:,}'.format(round(mean_travel_time / 60, 2)), 'minutes or,\n',
          '{:,}'.format(round(mean_travel_time / 3600, 2)), 'hours.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types:\n')
    for user, count in user_types.items():
        print('{:<13s}{:>7d}'.format(user, count))

    # TO DO: Display counts of gender
    print('\nGender count:\n')
    try:
        gender = df['Gender'].value_counts()
        for user, count in gender.items():
            print('{:<13s}{:>7d}'.format(user, count))
    except:
        print('The city you selected does not have Gender data.')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nYear of birth stats:\n')
    try:
        print('Earliest year of birth:\n',
              df['Birth Year'].min())
        print('\nMost recent year of birth:\n',
              df['Birth Year'].max())
        print('\nMost common year of birth:\n',
              df['Birth Year'].mode()[0])
    except:
        print('The city you selected does not have Birth Year data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Upon request of user, print raw data."""
    for i in range(0, df.shape[0], 5):
        print("\nI can show you 5 lines of raw data at a time if you like.")
        action = input("Type 'yes' to continue or 'no' to stop: ")
        if action.lower() != 'yes':
            break
        else:
            print(df.iloc[i: i + 5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

## References:
## 1. Udacity lessons and exercises
## 2. Python documentation from python.org
## 3. Pandas documentation from pandas.pydata.org
## 4. GeeksforGeeks.org
## 5. stackoverflow.com
