# Team-Heisenbug

<b>Codefundo Project</b>

<b>Problem Statement</b>
Find better ways to save lives and prevent economic losses through mechanisms to predict, prevent, or manage the impact of natural disasters.

A natural disaster evolves over multiple phases. and in each of these, the necessary and precautionary measures taken vary. With slight nuances in each of these methods over a phase, we believe we can save more lives and reduce the socio-economic damage to our society. Considering the wide span of the problem statement, we propose a <b>web application</b> comprising the following as a comprehensive solution. Following are the components in our application, its working and how they will assist the community:

1) <b>Prepare</b><br> 
	1.1) STEP 0 - Displaying precautionary measures,disaster resistance structure guidance,important medical procedures,important contacts etc. to assist a confused user with immediate first aid and guidance about the best possible step at the moment

	1.2) Am I in danger - letting the user know if he is in a high seismic zone or in an area prone to dangers form the disaster.

2) <b>Prediction of earthquake</b> Using previous data or by detecting p-waves generated before earth quake which gives the user enough time to react and take the necessary precautionary measures.

The prediction of earthquakes and tsunamis, is our prime focus at this point. We will attempt to solve this problem by one of, or by an amalgamation of the methodologies mentioned forthwith: 

2.1) A statistical analysis of earthquake data of sufficient magnitude would engender a comprehensive report of regions that are especially susceptible to earthquakes and could possibly predict earthquakes that are to come with the help of machine learning tools. We intend to compare the results brought about by using regression techniques (Multiple or Random Forest/ XGBoost) with those produced by deep learning (possibly using LSTMs to remember historical  dependencies). This process would also reveal valuable insights and other data correlations that could prove useful.

2.2) An observation common to most earthquakes and tsunamis has been the behaviour animals seem to exhibit prior to the earthquake. The cause for this has been speculated to be their sensing of the quake's Longitudinal P Waves that arrive prior to the destructive S or Rayleigh Waves of the quake. If these waves are detected correctly, it could be possible to gain precious time in which power lines could be shut off and more preventive and protective measures can be taken.

The detection of P waves becomes a pattern recognition problem and we intend to accomplish this by training a deep neural network to recognize distinctive features in P Waves and classifying waveforms. 

The above ideas are what we have arrived at following extensive research on the issue, and we intend to choose the better performing approach, unless an amalgamation of the two yields more accurate results.


3) <b>Heat-map</b>: Social media is an important medium to track and spread awareness about natural disaster so we shall fetch all the mentions of a particular disaster from social media platforms(for example, tweets for a given hashag(#hurricaneIrene) and the geo-tags associated with them). We then use this data to build a heatmap to get a user's account of affected areas and validate a natural disaster. This is a crucial element in our app, as it is very necessary to not put an alarming facade of the scenario to the society. It is necessary to present facts and facts only. This is backed by a disaster tracker which aggregates the news about disasters from veritable sources (like news networks and weather stations)

4) <b>Identity and Treatment</b>: When rescued,there is no way to know a persons identity and let his/her kins about his well being. Often treatment is delayed due to basic medical checks,this can be deciding factor. To combat this we shall allow people to submit basic details,blood group,previous medical history and insurance and hence allow rescuers to scan facial features to get back this info and allow finding of nearest blood donors.

The above being the primary features of our app, they are further supported by a few ancillary features as follows

i) <b>Request map<b>: Allow people at a given shelter home to raise requests for food,medical need,clothing,loss claims and allow more curated distribution of these resources<br><br>
ii)<b>BroadCast Distress message</b>

