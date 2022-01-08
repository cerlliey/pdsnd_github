import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('please enter the name of the city').lower().strip()
    while city not in CITY_DATA:
        print('oh, that\'s not right')
        city = input('please enter the name of the city').lower().strip()
        continue   
            
        
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('please enter the name of the month').lower().strip()
    while month not in month_list:
        print('oh, that\'s not right')
        month = input('please enter the name of the month').lower().strip()
        continue
           
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('please input the day of the week').lower().strip()
    while day not in day_list:
        print('oh, that\'s not right')
        day = input('please enter the name of the day').lower().strip()
        continue
           
        
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start month:', popular_month)

    # TO DO: display the most common day of week
    # find the most popular day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Popular Start day:', popular_day_of_week)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # find the most popular hour
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start to end'] = df['Start Station'] + 'to' + df['End Station']
    popular_start_to_end = df['start to end'].mode()[0]
    print('Most Popular Start to end route:', popular_start_to_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
   
        gender = df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print('the earliest year is', earliest_year)
        recent_year = df['Birth Year'].max()
        print('the most recent year is', recent_year)
        common_year = df['Birth Year'].mode()[0]
        print('the most common year is', common_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def request_five(df):
    start_loc = 0
    end_loc = 5
    while input('would you like to see five rows of data?, type yes or no').lower().strip() == 'yes':
        print(df.iloc[start_loc:end_loc,:])
        start_loc += 5
        end_loc += 5
        
        
     
        
def main():
    while True:
        city, month, day = get_filters()
        if city in CITY_DATA and month in month_list and day in day_list:
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            request_five(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
