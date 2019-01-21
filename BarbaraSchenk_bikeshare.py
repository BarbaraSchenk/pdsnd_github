"""
This project uses data provided by motivate, a bike share system provider for many major cities
in the United States, to uncover bike share usage patterns. A variety of descriptive statistics
can be calculated and compared for Chicago, New York City, and Washington, DC.
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_NAMES = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']
MONTHS_CODE = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}

WEEKDAYS = { 'mon': 'Monday', 'tue': 'Tuesday', 'wed': 'Wednesday', 'thu': 'Thursday', 'fri': 'Friday', 'sat': 'Saturday', 'sun': 'Sunday', 'all': 'All'}

NEW_VARIABLE =[new_1, new_2]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease enter the city for which the statistics should be calculated. Valid values include: \nNew York City, Chicago, or Washington\n')
        if CITY_DATA.get(city.lower()) != None:
            break
        else:
            print('Please enter a correct city name')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease enter the month for which the statistics should be calculated. Valid values include: \nJan, Feb, Mar, Apr, May, Jun, or all\n')
        if month.lower() in MONTH_NAMES:
            break
        else:
            print('Please enter a correct month')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('\nPlease enter the day of week for which the statistics should be calculated. Valid values include: \nMon, Tue, Wed; Thu, Fri, Sat, Sun, or all\n')
        if WEEKDAYS.get(day.lower()) != None:
            break
        else:
            print('Please enter a correct day of week')

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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    filename = CITY_DATA.get(city)
    df = pd.read_csv(filename)

    # convert the Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month_no = MONTH_NAMES.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month_no]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == WEEKDAYS.get(day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n-- Calculating The Most Frequent Times of Travel --\nMost common...')
    start_time = time.time()

    # display the most common month
    most_month = df['month'].mode()[0]
    print("\tMonth is {}".format(MONTHS_CODE.get(most_month)))

    # display the most common day of week
    most_day= df['day_of_week'].mode()[0]
    print("\tWeek day is {}".format(most_day))

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_hour = df['start_hour'].mode()[0]
    print("\tStart hour is {}".format(most_hour))

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n-- Calculating The Most Popular Stations and Trip --\nMost commonly used...')
    start_time = time.time()

    # display most commonly used start station
    most_start = df['Start Station'].mode()[0]
    print("\tStart station is {}".format(most_start))

    # display most commonly used end station
    most_end = df['End Station'].mode()[0]
    print("\tEnd station is {}".format(most_end))

    # display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + ' to ' + df['End Station']
    most_trip= df['start_end'].mode()[0]
    print("\tTrip is {}".format(most_trip))
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n-- Calculating Trip Duration --')
    start_time = time.time()

    # calculate travel time for each row
    df['travel_time'] = df['End Time'] - df['Start Time']

    # display total travel time
    sum_travel = df['travel_time'].sum()
    print("\tTotal travel time is {}".format(sum_travel))

    # display mean travel time
    mean_travel = df['travel_time'].mean()
    print("\tAverage travel time is {}".format(mean_travel))

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\n-- Calculating User Stats --')
    start_time = time.time()

    # Display counts of user types
    # https://erikrood.com/Python_References/rows_cols_python.html
    subscriber = df.loc[df['User Type'] == 'Subscriber']
    customer = df.loc[df['User Type'] == 'Customer']
    print("Counts of user type: {} Subscriber and {} Customer".format(subscriber.count()[0], customer.count()[0]))

    if city != 'washington':
        # Display counts of gender
        male = df.loc[df['Gender'] == 'Male']
        ct_male=male.count()[0]
        female = df.loc[df['Gender'] == 'Female']
        ct_female=female.count()[0]
        print("Counts of gender: {} Male and {} Female".format(ct_male, ct_female))

        # Display earliest, most recent, and most common year of birth
        e_yob = int(df['Birth Year'].min())
        r_yob = int(df['Birth Year'].max())
        c_yob = int(df['Birth Year'].mode()[0])
        print("{} is earliest, {} is most recent, and {} is the most common year of birth.".format(e_yob, r_yob, c_yob))
    else:
        print("No gender or year of birth data available for Washington.")


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        #get criteria for city, month, day from user input
        city, month, day = get_filters()

        print('You entered the following criteria\nCity: {}, Month: {}, Weekday:{}'.format(city, month, day))

        #load user input related data into data frame
        df = load_data(city.lower(), month.lower(), day.lower())
        records=len(df.index)
        print("{} data records match your criteria".format(records))
        print('-'*40)

        if records > 0:
            #compute statistics
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)
            print("Thank you for using the program today! We hope you found the information helpful :-)")
        else:
            print("No data record match your criteria: City: {}, Month: {}, Weekday:{}".format(city, month, day))

        #check if user wants to restart program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
