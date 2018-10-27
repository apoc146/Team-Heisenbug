# CodeFunDo Web-Application
the web app tries to achive following goals
1.)<b>Precaution</b>:the web app displays basic information issued by goverment agencies regarding the steps they can take 
to reduce loss to life and property
2)Show live updates from USGS handle to broadcast news about latest earthquakes,pipointing location and magnitude
3)A heat map to let people know about seismic activity around the world with details like location,magnitude and time
4)it not only allows user to sort by magnitue and time but also displays very recent earthquakes
5)it is able to do so because of the live USGS api ang google maps geomapping api

<br><br>
<b>Management</b>
<br>
<b>Idea for Faster aid delivery and treatment</b>
<ul>

<li>
Another big problem that rescuer has to face is that when rescued there is no way to determine the persons identity
</li>

<li>
Often a valuable amount of time is wasted in basic medical checkups which can been avoided if basic medical and personal details are readily avaible
</li>
  
<li>
This also allows in easily informing family and settle medical and other insurance claims
</li>

<li>
Same data can be used to send distress messages on their mail id using "sendemail" package in linux or using paid service like
<b>Twilio</b>
</li>
  
<li>
Our Idea was to allow user to upload basic info along with his image which gets stored in Azure SQL DB
</li>

<li>
When a rescuer rescues someone he can scan his image and upload
</li>
  
<li>
The image is matched across all images in db using Azure Face Matching Azure Cognitive API and top 3 entries are returned
</li>
  
<li>
The resuer can then select the most similar one and know his medical history,allergies,blood group,insurance claims and contact details
</li>

<li>How ever we ares still in process to implement this and hope to finsish intergating the api in next couple of hours
</li>

</ul>
