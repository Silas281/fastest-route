#=============================================================================================================================================
# SILAS SANGMIN
# ALGORITHM DESIGN AND ANALYSIS FINAL PROJECT
# fastest.py
#
#
#The program calculates the fastest path from a chosen city to another chosen destination using a modified Dijkstra Algorithm
# Time complexity = O(ElogV) Since the graph uses adjacency list
#===============================================================================================================================================


class Fastest:
    def __init__(self):

        #---------------------------------------------------------------------------------------------
        #READ FILE INPUT TO GET FIRST LINE [NUMBER OF CITIES, NUMBER OF ROUTES, AND DESTINATION]
        #get file input
        self.file = open("fastest.inp.txt", "r")
        #read first line
        self.line = self.file.readline()

        #Get the first line of file as an array
        data = self.line.split(" ") 
        
        #Get the number of cities
        self.total_cities = int(data[0])

        #Get the number of roads
        self.total_routes = int(data[1]) 

        #Get the final destination
        self.dest_city = int(data[2]) 
        
        #this is the starting speed which will be updated to the speed at each optimal route
        self.curr_speed=70

        #Graph Dictionary 
        self.graph={}

        
        #-------------------------------------------------------------------------------------------------

    
    # Add a vertex to the graph
    def add_vertex(self,v):
        if not(v in self.graph):
            self.graph[v] = []
       
            
    # Add an edge to the graph
    def add_edge(self,v1, v2,s,d):

        # Check if vertex v1 and v2 are valid vertices
        if (v1 in self.graph) and (v2 in self.graph):
            temp = [v2, s,d]
            self.graph[v1].append(temp)


    #-----------------------------------
    # THIS FUNCTION USES A DIJKSTRA ALGORITHM TO FIND THE FASTEST ROUTE      
    #------------------------------------
    def dijkstra(self,graph,start, destination):
       
        #A set to Keep track of visited vertices
        visited = set()
        #A dictionary to keep track of the time at each traversal
        time = {start: 0}
        #A dictionary to keep track of next moves. {5:0} means a start_city from 0 to 5
        optimal_moves = {start: None}
            
        #initialize starting city
        start_city=0

        #start traversing all cities
        for v in range(self.total_cities): 
            
            #if city is already visted, skip
            if start_city in visited: 
                continue

            #Current city
            vertex=start_city

            #Add current city to visited
            visited.add(vertex)
            
            if vertex == destination: #bread if destination is reached
                break

            #A dictionary to keep track of all temporal costs around a vertex
            temp_cost={}
            #A dictionary to capture the details of the neighbor city with the optimal route to send the details outside the for loop
            temp_d={}
            for neighbor, speed, distance in graph[vertex]: #for every neighboring city
                if neighbor in visited: #if city is visited
                    continue # skip 
                
                # old_cost = time.get(neighbor, float('inf')) 

                if speed > 0: 
                    #print(vertex," to ",neighbor," :",distance,"/",speed,"-->",distance/speed)
                    temp_time=round(distance/speed,4)
                else:
                    speed=self.curr_speed #use previous speed if current speed is greater than zero
                   # print(vertex," to ",neighbor," :",distance,"/",speed,"-->",distance/speed)
                    temp_time=round(distance/speed,4)

                new_time = time[vertex] + temp_time #calculate new time
                    
                time[neighbor] = new_time #update neighbor city time
                temp_cost[neighbor]=new_time #store temp time
                temp_d[neighbor]=(new_time,neighbor,speed) #store temp details
                

            max_key = min(temp_cost, key=temp_cost.get) #get the key for the neighbor city with the minimum time
            _,start_city,self.curr_speed=temp_d.get(max_key) #get its details and update start city to that city and prev/current speed
            optimal_moves[start_city] = vertex #set that city/neighbor as the next optimal move
            #print("next fastest city-->",start_city)

        #return optimal moves as a dictionary
        return optimal_moves #,visited,time
    
    #Trace path from optimal moves dictionary
    def trace_path(self, optimal_moves, destination):

        output_file = open("fastest.out.txt", 'w')
        
      
        if destination not in optimal_moves:
            return None

        city = destination
        path = ""

        while city is not None: # root has null optimal_moves
            path =str(city)+" "+path #get path in starting from destination
            city = optimal_moves[city] #get path using dict key

        output_file.write(path) # write output to a text file
        return path

    def build_Graph(self):
        for i in range(self.total_routes):
            #file = open("fastest.inp.txt", "r")
            self.line = self.file.readline()
            data = self.line.split(" ")        
            
            #Get the starting city
            src=int(data[0])
            dest=int(data[1])
            speed=int(data[2]) #Get the speed
            #Get the distance
            dist=int(data[3].replace("\n",""))


            #add start city
            self.add_vertex(src) 
            #add destinantion city
            self.add_vertex(dest)
           
            #Add egdes or neighboring cities
            self.add_edge(int(data[0]),int(data[1]),speed,dist)

        self.file.close()

        return self.graph



#===========================================================================================================================================       
#TEST CODE

#create class instance
f=Fastest()

#get Graph
graph=f.build_Graph()

print ("Graph representation: ",graph)


#Compute optimal routes
optimal_moves=f.dijkstra(graph=graph,start=0,destination=1)

#trace optimal path
path=f.trace_path(optimal_moves=optimal_moves,destination=1)

# print("visited-->",visited)
# print("time-->",time)
# print("optimal_moves-->",optimal_moves)
print()

#print graph
print("fastest route-->",path)

print()

#============================================================================================================================

