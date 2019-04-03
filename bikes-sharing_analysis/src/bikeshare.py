import time
import pandas as pd
import numpy as np
import os

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
DAY = ['all', 'monday', 'tuesday', 'wednesday',
       'thursday', 'friday', 'saturday', 'sunday']
MONTH = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DIR_ROOT = os.path.abspath(os.path.dirname(os.getcwd()))
DIR_DATA = os.path.join(DIR_ROOT, 'data/')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = get_input('city', CITY_DATA.keys())
    month = get_input('day', MONTH)
    day = get_input('day', DAY)

    print('-'*40)
    return city, month, day

def get_input(analysis_obj, objects_set):
    "Get the input objects."
    while True:
        ret = input("\nPlease input the %s you want to analyza: " %analysis_obj)
        ret = ret.lower()
        if ret in objects_set:
            break
        else:
            print("Please input the right %s!" %analysis_obj)
    
    return ret

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
    path_city = os.path.join(DIR_DATA, CITY_DATA[city])
    df = pd.read_csv(path_city)

    if (month != 'all'):
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df = df[df['month'] == MONTH.index(month)]

    if (day != 'all'):
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    # mode():Return the highest frequency value in a Series.
    month_most_common = df['month'].mode()[0]
    print("The most common month: ", MONTH[month_most_common].title())

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print("The most common day of week: ", df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ", most_common_end_station)

    # display most frequent combination of start station and end station trip
    # top = df.groupby(['Start Station', 'End Station']).size().idxmax()
    # top[0],top[1]
    df_station = df['Start Station'] + df['End Station']
    most_frequent_station = df_station.mode()[0]
    print("The most commonly frequent combination of start station and end station trip: ",
          most_frequent_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Display total travel time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Display maen travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Display counts of user types:\n", user_types)

    # Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print("Display counts of gender:\n", genders)
    except:
        print("\nWarning! There is no gender infomations in this city.")

    # Display earliest, most recent, and most common year of birth
    try:
        most_common_year = df['Birth Year'].mode()[0]

        year_sorted = df['Birth Year'].sort_values()
        year_sorted = year_sorted.dropna()
        earliest_year = year_sorted.reset_index(drop=True).iloc[0]
        most_recent_year = year_sorted.reset_index(drop=True).iloc[-1]
        print("Display earliest, most recent, and most common year of birth:",
            earliest_year, most_recent_year, most_common_year)
    except:
        print("\nWarning! There is no birth year infomations in this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
