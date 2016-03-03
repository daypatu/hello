a = ({1, 2}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {6, 5})
#a = ({1, 2}, {1, 3}, {1, 4}, {2, 3}, {3, 4}, {3,5}, {5,6})
a = ({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},
     {9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)
#a = ({1,3},{3,4},{3,5},{4,6},{6,7},{8,3},{8,1},{2,6},{8,4},{9,5},{4,5},{1,7},)
#a = ({1,2},{1,3},{1,5},{2,3},{2,4},{4,6},{5,6},)
#a = ({1,2},{1,3},{1,4},{2,3},{2,4},{3,4},)
#a = ({1,2},{2,3},{3,4},{4,5},{5,2},{1,6},{6,7},{7,8},{8,9},{9,6},{1,10},
#    {10,11},{11,12},{12,13},{13,10},{1,14},{14,15},{15,16},{16,17},{17,14},)
a = ({1,2},{1,3},{1,5},{2,3},{2,4},{4,6},{5,6},)

def break_rings(rings):
    
    
    
    bul = True
    slomano =set() #set of numbers of broken rings

    while bul:
    
        k = 0  #number of broken ring
        Max = 0
        dict1 = {}
        bul = False
        current = 0
        for item in rings:
            
            if slomano.isdisjoint(item):
                bul = True
                for i in item:
                    if i not in dict1:
                        dict1[i] = 1
                        current = i
                    else:
                        dict1[i] += 1
                    
        print("ring:connections = ",dict1)
        
        break_cicle = True
        for key in dict1:  #check if there is any ring with one connection
            if dict1[key] == 1:  
                k = key
                break_cicle = False
                break
        
        if break_cicle and (dict1 != {}) : #if there is no ring with one connection
                                            # we seek a cicle
            cicle = set()
            visited = {}
            for key in dict1:
                visited[key] = 0
            visited[current] = 1
            jj = 0
            while cicle == set():
                jj += 1
                
                for key in visited:
        
                    if ({current, key} in rings):
                        if visited[key] == 0:
                            current = key
                            visited[key] = jj
                            
                            break
                        elif visited[key] != jj-2:
                            c = visited[key]
                            
                            for m in visited:
                                if visited[m] >= c:
                                    cicle.add(m)
                            break
                
            print("There is a cicle in the graph: ",cicle)
            
            for item in cicle:
                if Max < dict1[item]:
                    Max = dict1[item]
                    k = item
                    
            if k in dict1:  #we break the element of cicle with the biggest
                             #amount of connections
                slomano.add(k)
                
        
        else:                     #if there is a ring with one connection
            for item in rings:  #we break its neighbour        
                if (k in item) and slomano.isdisjoint(item):
                    
                    for i in item:
                        if i != k:
                            
                            slomano.add(i)
                    
        print("Broken rings = ",slomano)
        print("")

    print("We should break: ")       
    
    return len(slomano)



print(break_rings(a))
