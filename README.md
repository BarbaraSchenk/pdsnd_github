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

### Files used
Include the files used

### Credits
It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.
