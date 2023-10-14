# Social Media Variety Geolocation Task (SMG)

The SMG task consists of three subtasks focusing on three different language areas:
- DE-AT: This subtask focuses on Jodel conversations initiated in Germany and Austria, which are written in standard German but contain regional and dialectal forms.
- CH: This subtask focuses on Jodel conversations initiated in German-speaking Switzerland, which are held majoritarily in Swiss German dialects.
- BCMS: This subtask is focused on geolocated tweets published in the area of Croatia, Bosnia and Herzegovina, Montenegro and Serbia in the so-called BCMS macro-language.

The data format is identical for all three subtasks. Each line contains a classification instance with three tab-separated columns:
- the latitude coordinate
- the longitude coordinate
- the text.
For evaluation, only the text column will be given, and participants are expected to predict latitude and longitude coordinates.

The three subtasks feature different data sizes and different levels of linguistic variation. Participants are encouraged to submit their solutions for all subtasks, but partial submissions are accepted as well. We accept both closed (constrained) and open(unconstrained) participations.

We provide an evaluation script (evaluate.py) that computes the median and mean distances between the prediction output and the reference. Median distance will be the primary evaluation metric for the SMG task.

A baseline model that predicts the centroid for each classification instance obtains the following median distances on the dev set:
- DE-AT: 205.54 km
- CH:     53.29 km
- BCMS:  156.29 km
