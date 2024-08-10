import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# coloring the data
b_start_line = '\x1b[6;30;42m'
b_end_line = '\x1b[0m'

r_start_line = '\x1b[1;31;40m'
r_end_line = '\x1b[0m'

d_start_line = '\x1b[1;32;40m'
end_line = '\x1b[0m'

# TESTING
"""
df = pd.read_csv(CITY_DATA["chicago"])
df.head()
"""


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
        or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
        or "all" to apply no day filter
    """
    print(d_start_line + 'Hello! Let\'s explore some US bikeshare data!' + b_end_line)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while True:
        cites = ["chicago", "new york city", "washington"]
        if city in cites:
            break
        else:
            print("city to select from [chicago, new york city, washington]".title())
            city = input(d_start_line+"Please select city name : ( chicago , new york city , washington)\n".title()+end_line).lower()
    print(r_start_line+"you chosed the city of  : {}".format(city).title()+r_end_line)
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if (month in months) or (month == 'all'):
            break
        else:
            print(r_start_line+"\nmonths to select from is : ['january', 'february', 'march', 'april', 'may', 'june'] ".title()+end_line)
            month = input(
                "Please select filter type , 'all' or 'monte name' , if month enter the name of the month (january, february, ... , june)\n".title()).lower()
    print(r_start_line+"you chosed to filter by : {}".format(month)+r_end_line)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while True:
        days = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]
        if (day in days) or (day == 'All'):
            break
        else:
            print("\nfilter by day  enter day name : ".title())
            day = input(d_start_line + "\nPlease select filter type for day of week , \
                        'all' or day , \n if day enter the name of the day (all, monday, \
                        tuesday, ... sunday) capital or small latters or rubrics \n" + r_end_line).title()

    if day == "All":
        day = day.lower()
    print(r_start_line+"you choses to filter by : {}".format(day).title()+r_end_line)
    print(d_start_line + "\ndata will be showing for cit of "+end_line + r_start_line+city.title()+end_line + d_start_line+" in month of " +
          end_line+r_start_line + month.title() + end_line+d_start_line+" in day of "+end_line + r_start_line+day.title()+"." + end_line)
    
    print('-'*40)

    #print( city, month, day)

    return city, month, day


# TESTING
# get_filters()

# print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

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
    # load data based on the arg() from caling the load_date function
    df = pd.read_csv(CITY_DATA[city])

    # converting the start time string to date time to extract from
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    # df['day']   = df['Start Time'].dt.day
    df['Day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)

        # filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month == month+1]

    # filter by day of week if applicable
    if day != 'all':
        """create filter of day
        using the day index in case we asked the user to enter number of the day in the week
        days = ['Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday']
        day  = days.index(day)+1
        filter by day of week to create the new dataframe
        """
        df = df[df['Start Time'].dt.day_name() == day]

    return df

# TESTING
# test_case
# load_data('chicago', 'april', 'Sunday')
# load_data('chicago', 'all', 'all')
# get help to extract day name
# df = df['Start Time'].dt.day_name()
# help link:(https://www.youtube.com/watch?v=6cjXwYqgreE)
# help link:(https://stackoverflow.com/questions/60339049/weekday-name-from-a-pandas-dataframe-date-object)
# df = df['Start Time'].dt.day_name()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print(r_start_line+'\nCalculating The Most Frequent Times of Travel...\n'+end_line)
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print(d_start_line+'\nMost Frequent Month      :', popular_month + end_line)

    # TO DO: display the most common day of week
    popular_day = df['Day'].mode()[0]
    print(d_start_line+'\nMost Frequent day        :', popular_day + end_line)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print(d_start_line+"\nMost Frequent Start Hour :"+end_line, popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# TESTING
""" df=load_data('chicago', 'all', 'all')
time_stats(df)
 """
# df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print(r_start_line+'\nCalculating The Most Popular Stations and Trip...\n'+ end_line)
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df["Start Station"].mode()[0]
    print(r_start_line+'\nMost Commonly used start station :'.title(), commonly_start_station+ end_line)

    # TO DO: display most commonly used end station
    commonly_end_station = df["End Station"].mode()[0]
    print(d_start_line+'\nMost Commonly used end station   : {}'.format(commonly_end_station).title()+ end_line)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end_station = ((" start with :"+df["Start Station"]+", and end with :"+df["End Station"]).max()).title()
    print(d_start_line+'\nMost Frequent start station and\nend station of trip              :'.title(),combination_start_end_station+ end_line)
    # df.mode(axis='columns', numeric_only=False)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# TESTING
""" df=load_data('washington', 'all', 'all')
station_stats(df) """

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print(r_start_line+'\nCalculating Trip Duration...\n' + end_line)
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum().sum()
    print(d_start_line+'\ntotal travel time   : {} hours'.format(total_travel_time).title() + end_line)

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print(d_start_line+'\nmean travel time    : {} hours'.format(mean_travel_time).title() + end_line)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# TESTING
""" df = load_data('chicago', 'april', 'Sunday')
trip_duration_stats(df) """

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print(r_start_line+'\nCalculating User Stats...\n' + end_line)
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users = df['User Type'].count()
    print(r_start_line+'\nTotal number of users    : {} users'.format(count_users).title() + end_line)
    # print value counts for each user type
    user_types = df["User Type"].value_counts()
    print(user_types)


    """ 
      Washington data does not have Gender and Birth Year columns. 
      When user selects Washington as the city your code throws an error. 
      You need to write some control points here. 
      If user choose Washington as city, then this control point should skip Gender and Birth Year analyses.
     """

    # CHECKING FOR GENDER
    # TO DO: Display counts of gender
    if 'Gender' in df:
        # Only access Gender column in this case
        count_gender = df['Gender'].count()
        print(d_start_line+'\nTotal count gender of users    : {} users'.format(count_gender).title()+ end_line)

        gender = df["Gender"].value_counts()
        print(gender)

    else:
        print(r_start_line+"\nGender stats cannot be calculated ,because 'Gender' does not appear in the dataframe" + end_line)

    # CHECKING FOR Birth Year
    if 'Birth Year' in df:
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nearliest birth year    : {}'.format(
            earliest_birth_year).title())

        recent_birth_year = df['Birth Year'].max()
        print(r_start_line+'\nrecent birth year      : {}'.format(recent_birth_year).title() + end_line)

        most_birth_year = df['Birth Year'].mode()[0]
        print(d_start_line+'\nmost birth year        : {}'.format(most_birth_year).title()+ end_line)
    else:
        print(r_start_line+"\nBirth Year stats cannot be calculated ,because Birth Year does not appear in the dataframe" + end_line)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# TESTING
""" 
df=load_data('Washington', 'april', 'Sunday')
user_stats(df)  
"""

def viewing_data_frame(df):

    view_data = input(r_start_line+"Would you like to view 5 rows of individual trip data? Enter 'yes' or 'no'?\n"+ end_line)
    start_loc = 5
    while view_data != 'no':
        print(df.iloc[0:start_loc])
        start_loc += 5
        view_data = input(r_start_line+"Do you wish to continue?: "+ end_line).lower()


# TESTING
""" 
df=load_data('chicago', 'april', 'Sunday')
viewing_data_frame(df)  
"""

# get help to understand how to select rows from the data frame :) 
# help link: // www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        viewing_data_frame(df)

        restart = input(r_start_line+'\nWould you like to restart? Enter yes or no.\n'+ end_line)
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
