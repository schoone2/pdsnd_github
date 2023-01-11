#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np


# In[2]:

# Create list of available city data.
CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }


# In[3]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Welcome to US Bikeshare Program!!')
    # TO DO: get user input for city (chicago, new york city, washington). 
    #HINT: Use a while loop to handle invalid inputswhile 
    
    while True:
        city = input("\nChoose One of the Following Cities. New York City, Chicago or Washington?\n")
        city = city.lower()
        
        if city not in ('new york city', 'chicago', 'washington'):
            print("City Was Not Found! Check Spelling and Capitalization!")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich of the Following Months Do You Want to Analyze? January, February, March, April, May, June or type 'all'\n")
        month = month.lower()
        
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Month Did Not Match One of the Available Options Given. Try Again!")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich Weekday Do You Want to Analyze! Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'\n")
        day = day.lower()
        
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Weeday Did Not Match One of the Available Option Give. Try Again!")
            continue
        else:
            break

    print('-'*60)
    return city, month, day


# In[4]:


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
    # load data file into DF
    df = pd.read_csv(CITY_DATA[city], verbose=True)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    #print(df)
    
    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
 
    
    return df


# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    
    print('Most Common Bike Sharing Month:', most_common_month)

    # TO DO: display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]
    
    print('Most Popular Bike Sharing Day:', most_popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Hour for Bike Sharing:', most_popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    
    print('Most Common Start Station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    
    print('\nMost Common End Station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_frequent_station_combo = df['Start To End'].mode()[0]
    
    print(f"\nThe Most Frequent Station Combination is {most_frequent_station_combo}.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    minute, second = divmod(df['Trip Duration'].sum(), 60)
    
    print('Total Travel Time - Minutes:', minute, " Seconds: ", second)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('Mean Travel Time:', mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def display_data(df):
    
    get_data = input("Would You Like to View More Rows of Trip Data? (Enter Yes or No)")
    start_idx = 0
    display_more = "yes"
    
    numberOfRows = int(input("How Many Rows to View?"))

    if get_data.lower() == "yes":
        while (display_more == "yes"):
            print(df.iloc[start_idx:start_idx+numberOfRows])
            start_idx += numberOfRows
            display_more = input("Would You Like to View Another "+str(numberOfRows)+" Rows of Trip Data? (Enter Yes or No): ").lower()


# In[9]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    num_user_types = df['User Type'].value_counts()

    print('Number of User Types:\n', num_user_types)

    # TO DO: Display counts of gender
    try:
        listed_gender_types = df['Gender'].value_counts()
        print('\nListed Gender Types Below:\n', listed_gender_types)
    except:
        print("\nThere Is No 'Gender' Data In the File Given!")

    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest Birth Year:', earliest_birth_year)
    except:
        print("\nThere Is No 'Birth Year' Data In the File Given To Find Earliest Birth Year!")
   
    try:
        most_recent_birth = df['Birth Year'].max()
        print('\nMost Recent Birth Year:', most_recent_birth)
    except:
        print("\nThere Is No 'Birth Year' Data In the File Given To Find Most Recent Birth Year!")
        
    try:
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nMost Common Birth Year:', common_birth_year)
    except:
        print("\nThere Is No 'Birth Year' Data In the File Given To Find Most Common Birth Year!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:


#=================== MAIN PROGRAM =======================#
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

