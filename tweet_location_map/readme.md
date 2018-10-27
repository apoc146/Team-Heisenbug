<b> The idea is to associate emergency hashtags for people needing assistance or care. Owing to the trending nature of social media, this would allow us to have a prioritized real time monitoring system and a visualization of the crisis afflicted zone</b> 

We've written a script that makes use of the twitter location to scrape the tweets off a particular hashtag. (We've used #MeToo for testing purposes here. It can be replaced by any hashtag).
The scraped tweets are then dumped on to a json file where the coordinates of users with geolocation enabled can be extracted. <b> There are four sets of coordinates, each corresponding to the latitude and longitude of a GPS satellite reading. (four satellites needed to determine position)</b>
Given a little more time, we would have liked to <b>extract and use an API to determine the address of the coordinates where the tweets originated in order to maintain a realtime monitoring mechanism of people needing assistance</b>.
