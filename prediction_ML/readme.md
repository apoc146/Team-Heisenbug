We used a feed forward neural network architecture to predict magnitudes of earthquakes on particular latitudes and longitudes. <br>We also tried something similar with an LSTM network but the results were not as promising, however, we did generate a heatmap visualization of earthquake prone areas based on the data using mpl_toolkits' basemap 
<br><br>
The tweets ipynb was a simple test script we ran to fetch tweets for testing purposes. We based it off #hurricanerelief to see the kinds of results we got</b>
<br><br>
<b> A third excellent idea we were looking to implement was to conduct was P Wave detection. The idea behind this was to detect the precursor P Waves to the destructive S Waves and take possible precautionary measures.</b>
<b> <br><br>We intended to implement this by processing the waveforms and using Mel Frequency Cepstral Coefficients (MFCCs) for feature extraction and then classifying using either a convnet or other simpler binary classification algorithms.</b>
<br>
Unfortunately we couldn't do this as the data for P Waveforms was very hard to find.

The dataset we used for earthquake prediction was https://www.kaggle.com/usgs/earthquake-database>

