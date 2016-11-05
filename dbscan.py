import math
import numpy
from pylab import*

def findneighbors(point,r):
    neighborpoints = []
    for pt in data:
        #print math.sqrt(math.pow((point[0]-pt[0]),2)+math.pow((point[1]-pt[1]),2))
        if math.sqrt(math.pow((point[0]-pt[0]),2)+math.pow((point[1]-pt[1]),2))<r:
            neighborpoints.append(pt)
    return neighborpoints

def expandcluster(point,neighborpoints,c,r,n):
    point[3]=c
    for pt in neighborpoints:
        if pt[2]==0:
            pt[2]=1
            neighborpointsnext = findneighbors(pt,r)
            if len(neighborpointsnext)>=n:
                neighborpoints.extend(neighborpointsnext)
            if pt[3]==0:
                pt[3]=c
    return neighborpoints
            

def DBSCAN(r,n):
    c = 0;
    for point in data:
        if point[2]==0:
            point[2]=1
            neighborpoints = findneighbors(point,r)
            if len(neighborpoints)<n:
                point[3]=-1
            else:
                c=c+1;
                expandcluster(point,neighborpoints,c,r,n)
                clusters.insert(c-1,[x[0:2] for x in neighborpoints])


point = [[],[],[]]
clusterColor = [{1:'go'},{2:'bo'},{3:'ro'},{4:'wo'}]
with open('abc.csv','rb') as csvfile:
    csvdata = numpy.genfromtxt(csvfile,dtype=float,delimiter=',')
#data = [[1,1,0,0],[2,2,0,0],[3,3,0,0],[8,8,0,0],[9,9,0,0],[12,12,0,0],[13,13,0,0]]
#DBSCAN(3,2)
data=[x[0:2].tolist() for x in csvdata]


clusterX = [x[0] for x in data]
clusterY = [y[1] for y in data]
print numpy.random.rand(3,1)

plot(clusterX,clusterY,marker='o',lw=0,c=numpy.random.rand(3,1))
show()

for d in data:
    d.append(0)
    d.append(0)
clusters = [[]]
DBSCAN(3,2)

for cluster in clusters:
    clusterX = [x[0] for x in cluster]
    clusterY = [y[1] for y in cluster]
    clr = numpy.random.rand(3,1)
    plot(clusterX,clusterY,marker='o',lw=0,c=clr)

show()
