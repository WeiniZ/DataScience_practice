import sys
import math
import random
import subprocess
import numpy as np

def main():
    # How many points are in our dataset?
    num_points = 10
    
    # For each of those points how many dimensions do they have?
    dim = 2
    
    # Bounds for the values of those points in each dimension
    lower_bound = 0
    upper_bound = 200
	
	# The K in k-means. How many clusters do we assume exist?
    num_clusters = 3
    
    # When do we say the optimization has 'converged' and stop updating clusters
    opt_cutoff = 0.5
    
	point_list = [generatePoint(dim, lower_bound, upper_bound) for i in range(num_points)]

	clusters = Kmeans(num_clusters, opt_cutoff, points_list)

class Point:

   def __init__(self, coords):
       # initialize the point with coords
       self.coord = coord
	   self.dim = len(coord)
	   
   def __repr__(self):
       return str(self.coord)
	   
	   
class Cluster:
	
    def __init__(self, point_list):
        # initialize the clusters with the list of points
		# point_list is a list of point() objects
		# attributes: coord, points, 
		
		if len(point_list) == 0:
    		raise Exception("ILLEGAL: empty point list")
	 
		self.dim = point_list[0].dim
		
		for p in point_list:
		    if p.dim != point_list[0].dim:
    			raise Exception("ILLEGAL: wrong dimensions") 
		
        self.points = point_list	 
		
		# Set up the initial centroid (this is usually based off one point)
        self.centroid = self.calculateCentroid()
		
	def __repr__(self):
        return str(self.coord)	
		
	def calculateCentroid(self):
        '''
        Finds a virtual center point for a group of n-dimensional points
        '''	
		num_points = len(self.point_list)
		coords = [p.coord for p in self.point_list]
		coords_list = zip(*coords)
		
		centroid_coords = [math.fsum(d)/num_points for d in coord_list]
	    return(Point(centroid_coords))
		
		
	def optGap(self, points):
        '''
        Returns the distance between the previous centroid and the new after
        recalculating and storing the new centroid.
        '''
	    old_centroid = self.centroid
		self.point_list = point_list
		self.centroid = self.calculateCentroid()
		gap = getDistance(old_centroid, self.centroid)
		return gap
		
	
	
	
	
def generatePoint(dim, lower_bound, upper_bound):
    p = Point([random.uniform(lower_bound, upper_bound) for i in range(dim)])
	return p
		
def getDistance(p1, p2)
    if p1.n ! = p2.n : 
	   raise Exception("ILLEGAL: wrong dimensions") 
	   
	dist = reduce(lambda x,y: x+ pow((p1.coord[y] - p2.coord[y]),2),range(p1.dim), 0.0 )    
    return math.sqrt(dist))
	
def Kmeans():
    #Step 1 Assign points to the closet 
	#Step 2 Update cluster 
	


if __name__ == "__main__": 
    main()


	
	