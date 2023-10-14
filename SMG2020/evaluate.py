#! /usr/bin/env python3

import math, statistics, sys


# from http://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
def dist(lat1,lon1,lat2,lon2):
	R = 6371	# Radius of the earth in km
	dLat = math.radians(lat2-lat1)
	dLon = math.radians(lon2-lon1)
	a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = R * c	# Distance in km
	return d


def evaluate(prediction, gold):
	distances = []
	for p, g in zip(prediction, gold):
		p_col = p.strip().split("\t")
		g_col = g.strip().split("\t")
		d = dist(float(p_col[0]), float(p_col[1]), float(g_col[0]), float(g_col[1]))
		distances.append(d)
	print("Median distance: {:.2f} km".format(statistics.median(distances)))
	print("Mean distance:   {:.2f} km".format(statistics.mean(distances)))
	print("Note: The official VarDial 2020 metric is median distance.")


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: {} systemoutput.txt gold.txt".format(sys.argv[0]))
		sys.exit(1)
	
	evaluate(open(sys.argv[1], 'r'), open(sys.argv[2], 'r'))
