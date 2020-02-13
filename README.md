# Wiki-Views
With this Python script you can create a WikiViews object taking a person's name as the parameter that holds information about their Wikipedia page's views over the past 60 days. The data is pulled from Wikipedia's page view API.

## Object Instantiation
The default parameter is 'Lisa Simpson.' 

![instantiation](images/Lisa_instantiate.png)

## Methods
`plot_two_months` returns a time-series plot of Wikipedia views over the previous 60 days.

![plot](images/Lisa_graph.png)

`max_views` returns a tuple of the date of the maximum number of views and the number of views.

![max](images/Lisa_max.png)


`mean` returns the mean daily views over the 60-day period.

![mean](images/Lisa_mean.png)

`sixty_day_count` returns a total count of views over the previous 60 days.

![60 days](images/Lisa_sixty_days.png)

`thirty_day_count` returns a total count of views over the previous month.

![30 days](images/Lisa_30_days.png)

`seven_day_count` returns a total count of views over the previous week.

![7 days](images/Lisa_seven_days.png)

`yesterday` returns a count of views over the previous day.

![1 day](images/Lisa_yesterday.png)

`get_views` returns a dictionary with key, value of date, views for the previous 60 days. 

![views dictionary](images/Lisa_get_views.png)

`values` returns an array of number of views per day over the previous 60 days.

![values](images/Lisa_values.png)
