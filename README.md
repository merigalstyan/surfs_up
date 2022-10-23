# Surfs Up

This analysis is about opening a Surf and Shake shop serving surfboards and ice cream to locals and tourists in Oahu, Hawaii. This analysis aims to retrieve important weather information. In the long term, surf shops should be located in warm areas where tourists and locals regularly visit.

Harvesting a lot of data from different weather stations was essential to get statistical information from this analysis. A considerable part of the analysis was about connecting to databases and reflecting tables to explore climate changes in Oahu.

## Analysis
 
The important parts of this analysis included retrieving precipitation data, finding the number of stations for climate data, and finding low, high, and average temperatures.

### Precipitation

It wasn't only important to have a warm environment; the shop’s location needed balanced precipitation to keep everything green and fresh around, but also not too much to impact the nice ice cream and surfing weather.

The first step of the analysis included choosing the most recent weather data from 2017 and retrieving precipitation scores using SQLalchemy starting from the last data point in the database.

<img width="814" alt="Screen Shot 2022-10-22 at 8 23 14 PM" src="https://user-images.githubusercontent.com/111609994/197371916-5d24af30-0824-41d2-a9d6-104409f25d79.png">

Eventually, plotting this data frame, we can observe that even though some months have higher precipitation rates, overall, Oahu seems pretty ideal for this shop.

<img width="615" alt="Screen Shot 2022-10-22 at 8 27 54 PM" src="https://user-images.githubusercontent.com/111609994/197371989-ea3149f0-2ee8-4773-be33-ad1aee84fcd8.png">

### Stations

Another hurdle along the way was ensuring that the weather data wasn't coming from too few sources and thus resulting in invalid analysis. To make sure, using ***session.query*** function can retrieve all the stations that provided the climate data:

<img width="698" alt="Screen Shot 2022-10-22 at 8 30 16 PM" src="https://user-images.githubusercontent.com/111609994/197372056-9dedd468-1e0e-4553-b4a4-b499a363a36b.png">

This code retrieved **nine** stations in descending order with station USC00519281 being the most active one.
We can assume that's a solid start for this analysis.

### Low, High, and Average Temperatures

Finally, **session.query** and **func** methods allow us to retrieve the different temperature points:

<img width="745" alt="Screen Shot 2022-10-22 at 8 33 47 PM" src="https://user-images.githubusercontent.com/111609994/197372166-4afb611a-dcf9-4b8c-a9b8-7918b76cbf17.png">

The lowest temperature turned out to be 54.0, the maximum - 85.0 and the average - 71.66.
 
## Trends

Even though the above information is great to base decisions on, it's still risky. We need to analyze some trends further.
 
To do so, let's have a look at June and December. Using **sqlalchemy** and **pandas**, we can create a data frame depicting the temperatures throughout June.

<img width="1063" alt="Screen Shot 2022-10-22 at 8 39 05 PM" src="https://user-images.githubusercontent.com/111609994/197372330-5b63f224-5b8b-4463-86c2-e95e3d7e4a5b.png">

Once the dataframe is retrieved, using **describe()** we can see the summary statistics for June:

<img width="161" alt="Screen Shot 2022-10-22 at 8 41 49 PM" src="https://user-images.githubusercontent.com/111609994/197372498-6478e88b-b270-48be-809a-2f8afd781fd8.png">

The same code can be applied to look at the month of December:

<img width="1118" alt="Screen Shot 2022-10-22 at 8 42 44 PM" src="https://user-images.githubusercontent.com/111609994/197372535-08559a4a-5054-4d9e-9d21-daf8c427733a.png">

Here are the results using **describe()** function for December:

<img width="201" alt="Screen Shot 2022-10-22 at 8 43 34 PM" src="https://user-images.githubusercontent.com/111609994/197372554-9a24f17a-e97c-43a3-9fe7-97c3003ec486.png">

## Results
 
Looking at the analysis from June and December, Oahu has pretty good weather all year round.
 
* The maximum temperature is higher by two degrees in June. Both months have relatively close maximum temperature points.
* The average temperature is higher by three degrees in June compared to December. 
* The minimum temperature is lower in December by 8 degrees compared to June.
 
## Summary
 
Even though there are little differences between max and min temperature points, overall, the average temperature is close enough for these months. The summary should be relatively the same throughout the year. Perhaps an additional query could be run on precipitation for these months to see which season has a higher chance of rainfall throughout the year.



