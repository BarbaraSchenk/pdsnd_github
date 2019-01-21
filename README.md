*created on 12/17/2018 by Barbara Schenk*

# Explore US Bikeshare Data

### Description
This project uses data provided by [motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. A variety of descriptive statistics can be calculated and compared for Chicago, New York City, and Washington, DC.

In a first step the user is asked to provide the information he is interested in. This includes city name, month, and day of week. It is also possible to enter "all" for month and day of week in order to consider all month and days of week, respectively.

Based on the entered parameters, the data is gathered, processed (e.g. times are converted to_datetime), and loaded into a data frame. Different sets of statistics are then calculated for the defined data frame:

**#1Popular Times of Travel** (i.e., occurs most often in the start time)
* most common month
* most common day of week
* most common hour of day

**#2 Popular stations and trip**
* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

**#3 Trip duration**
* total travel time
* average travel time

**#4 User info**
* counts of each user type
* counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

For each calculated statics set the calculation time is displayed.

The user can then start the analysis again for a different set of parameters or end the program.

### Data sets
Randomly selected data for the first six months of 2017 for the three cities Chicago, Washington, and NYC. Data wrangling has already been performed to condense these files to the following same core six (6) columns:
* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

### Files used
Original data can be accessed here: [Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), and [Washington](https://www.capitalbikeshare.com/system-data).

Condensed data files as well as a Python template with helper code and comments is provided [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/March/5aab379c_bikeshare-2/bikeshare-2.zip)

### Credits
[Udacity Programming for Data Science Nano Degree][1]

[1]: https://classroom.udacity.com/nanodegrees/nd104/parts/53470233-d93c-4a31-a59f-11388272fe6b/modules/0f8a717f-4ac2-49d7-9ac4-15ae692793fa/lessons/ee7d089a-4a92-4e5d-96d2-bb256fae28e9/concepts/87034580-6b86-4f45-9981-88f5c86d21bf#
