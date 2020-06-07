import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_list   = { 1 : 'JANUARY', 2 : 'FEBRUARY', 3 : 'MARCH', 4 : 'APRIL', 5 : 'MAY', 6 : 'JUNE'}

weekday_list = { 0 : 'MONDAY', 1 : 'TUESDAY', 2 : 'WEDNESDAY', 3 : 'THURSDAY', 4 : 'FRIDAY', 5 : 'SATURDAY', 6 : 'SUNDAY' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data !\n')
    
    city  = {1:'chicago', 2:'new york city', 3:'washington'}
    month, day = 0, 0

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (True):
        city_code = int(input('Enter the city code : 1 - Chicago, 2 - New York, 3 - Washington : '))
        if city_code in [1,2,3]:
            break
        else :
            print('Wrong Input! Please enter among given choices.')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while (True):
        month = int(input('Enter the month code [1 - January, 2 - February, 3 - March, 4 - April, 5 - May, 6 - June, 0 - All] : '))
        if month in range(7):
            break
        else :
            print('Wrong Input! Please enter among given choices.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while (True):
        day = int(input('Enter the weekday code [0 - Monday, 1 - Tuesday,  2 - Wednesday, 3 - Thursday, 4 - Friday, 5 - Saturday, 6 - Sunday, 7 - All] : '))
        if day in range(8):
            break
        else :
            print('Wrong Input! Please enter among given choices.')


    print('-'*40)
    return city[city_code], month, day


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
    df['Start Time']  = pd.to_datetime(df['Start Time'])
    df['start_month'] = df.apply(lambda x : x['Start Time'].month, axis=1)
    df['start_hour']  = df.apply(lambda x : x['Start Time'].hour,  axis=1)
    df['weekday']     = df.apply(lambda x : x['Start Time'].weekday(), axis=1)
    
    if (month==0) :
        pass
    else :
        df = df.query('start_month=={}'.format(month))
    
    if (day==7) :
        pass
    else :
        df = df.query('start_day=={}'.format(day))
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nSTATISTICS ON THE MOST FREQUENT TIMES OF TRAVEL : \n')
    start_time = time.time()

    # TO DO: display the most common month
    if (df['start_month'].nunique() == 1) :
        pass
    else :
        most_frequent_month = df['start_month'].mode()[0]
        print('Most frequent month of travel  :  ', month_list[most_frequent_month])

    # TO DO: display the most common day of week
    if (df['weekday'].nunique() == 1) :
        pass
    else :
        most_frequent_weekday = df['weekday'].mode()[0]
        print('Most frequent day of week of travel  :  ', weekday_list[most_frequent_weekday])

    # TO DO: display the most common start hour
    most_frequent_hour = df['start_hour'].mode()[0]
    print('Most frequent hour of travel  :  ', most_frequent_hour)

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nSTATISTICS ON THE MOST POPULAR STATIONS & TRIP OF TRAVEL : \n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station : ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station   : ', df['End Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nSTATISTICS ON THE DURATION OF THE TRIPS OF TRAVEL : \n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Duration Of Travel  : ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Duration Of Travel   : ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nSTATISTICS OF THE USERS : \n')
    start_time = time.time()

    # TO DO: Display counts of user types
    subscriber_count = df[df['User Type']== "Subscriber"].shape[0]
    customer_count   = df[df['User Type']== "Customer"].shape[0]
    print('Count of User Types : SUBSCRIBER = {}, CUSTOMER = {}'.format(int(subscriber_count), int(customer_count)))


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        male_count     = df[df['Gender'] == "Male"].shape[0]
        female_count   = df[df['Gender'] == "Female"].shape[0]
        print('Count of User Types : MALE = {}, FEMALE = {}'.format(male_count, female_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest Year Of Birth    : ', df['Birth Year'].min())
        print('Most Recent Year Of Birth : ', df['Birth Year'].max())
        print('Most Common Year Of Birth : ', df['Birth Year'].mode()[0])

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
        
        pos = 0
        choice = 0
        while ((pos>=0) and (pos<=df.shape[0])):
            choice = 0
            while (True):
                choice = int(input('Would you like to view 5 rows of individual trip data? [1 - YES, 2 - NO]  : '))
                if choice == 1:
                    print(df.iloc[:5])
                    pos = 5
                    break
                elif choice==2 :
                    pos = -1
                    break
                else : 
                    print('INVALID INPUT ! Please re-enter from given options')
            print()
            while(True):
                choice = int(input('Would you like to view next 5 rows of individual trip data? [1 - YES, 2 - NO]  : '))
                if choice == 1:
                    print(df.iloc[pos:pos+5])
                    pos = pos+5
                elif choice==2 :
                    pos = -1
                    break
                else : 
                    print('INVALID INPUT ! Please re-enter from given options')
            print()            
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
