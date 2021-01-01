def gridIllumination(N, lamps, queries):
    # list all positions that need to be illuminated
    # go through queries
    # for each query check if light is on, and turn it off + its 8 adjacents + remove illuminations from those adjacents
    # Notice the difference between a light which is ON and one which is illuminated

    ############# MAIN #############      
            
    lights_on = set()
    illuminated_rows = {}
    illuminated_cols = {}
    illuminated_diagonal_up = {}
    illuminated_diagonal_down = {}
    
    for lamp in lamps:
        lights_on.add((lamp[0], lamp[1]))
        illuminate(lamp[0], lamp[1], illuminated_rows, illuminated_cols, illuminated_diagonal_up, illuminated_diagonal_down)

    ans = []
    
    for q in queries:
        row = q[0]
        col = q[1]
        up = row + col
        down = row - col
        if (row in illuminated_rows and illuminated_rows[row] > 0) or (col in illuminated_cols and illuminated_cols[col] > 0) or (up in illuminated_diagonal_up and illuminated_diagonal_up[up]>0) or (down in illuminated_diagonal_down and illuminated_diagonal_down[down]>0):
            ans.append(1)
        else:
            ans.append(0)
        turnOffAdjLamps(q[0], q[1], lights_on, illuminated_rows, illuminated_cols, illuminated_diagonal_up, illuminated_diagonal_down)
        
    return ans


def reduceIllumination(row, col, illuminated_rows, illuminated_cols, illuminated_diagonal_up, illuminated_diagonal_down):

    #illuminate row
    illuminated_rows[row] = max(0, illuminated_rows.get(row,0) - 1)
    #illuminate col
    illuminated_cols[col] = max(0, illuminated_cols.get(col,0) - 1)
    
    #illuminate diagonal up
    up = row + col
    illuminated_diagonal_up[up] = max(0, illuminated_diagonal_up.get(up,0) - 1)
    #illuminate diagonal down
    down = row-col
    illuminated_diagonal_down[down] = max(0,illuminated_diagonal_down.get(down,0) - 1)
            
            
def illuminate(row, col, illuminated_rows, illuminated_cols, illuminated_diagonal_up, illuminated_diagonal_down):

    #illuminate row
    illuminated_rows[row] = illuminated_rows.get(row,0) + 1
    #illuminate col
    illuminated_cols[col] = illuminated_cols.get(col,0) + 1
    
    #illuminate diagonal up
    up = row + col
    illuminated_diagonal_up[up] = illuminated_diagonal_up.get(up,0) + 1
    #illuminate diagonal down
    down = row-col
    illuminated_diagonal_down[down] = illuminated_diagonal_down.get(down,0) + 1
        
            
def turnOffAdjLamps(row, col, lights_on, illuminated_rows, illuminated_cols, illuminated_diagonal_up, illuminated_diagonal_down):
    
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r>=0 and r <N and c>=0 and c<N:
                if (r,c) in lights_on:
                    reduceIllumination(r, c, illuminated_rows, illuminated_cols, illuminated_diagonal_up, illuminated_diagonal_down)
                    lights_on.remove((r,c))

         

N=100
lamps=[[7,55],[53,61],[2,82],[67,85],[81,75],[38,91],[68,0],[60,43],[40,19],[12,75],[26,2],[24,89],[42,81],[60,58],[77,72],[33,24],[19,93],[7,16],[58,54],[78,57],[97,49],[65,16],[42,75],[90,50],[89,34],[76,97],[58,23],[62,47],[94,28],[88,65],[3,87],[81,10],[12,81],[44,81],[54,92],[90,54],[17,54],[27,82],[48,15],[8,46],[4,99],[15,13],[90,77],[2,87],[18,33],[52,90],[4,95],[57,61],[31,22],[32,8],[49,26],[24,65],[88,55],[88,38],[64,76],[94,76],[59,12],[41,46],[80,28],[38,36],[65,67],[75,37],[56,97],[83,57],[2,4],[44,43],[71,90],[62,40],[79,94],[81,11],[96,34],[38,11],[22,3],[54,96],[78,33],[54,54],[79,98],[1,28],[0,32],[37,11]]
queries=[[24,84],[95,68],[80,35],[31,53],[69,45],[85,29],[87,25],[42,47],[7,59],[99,3],[31,70],[64,62],[44,91],[55,25],[15,52],[95,33],[21,29],[61,34],[93,34],[79,27],[30,86],[52,0],[18,10],[5,1],[40,21],[11,48],[55,94],[22,42],[81,0],[39,43],[5,25],[43,29],[45,47],[83,93],[77,70],[22,63],[30,73],[18,48],[39,88],[91,47]]

print(gridIllumination(N, lamps, queries))

print(gridIllumination(5, [[0,0],[4,4]], [[1,1],[1,0]]))
print(gridIllumination(5, [[0,0],[4,4]], [[1,1],[1,1]]))
