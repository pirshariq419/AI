
jug1, jug2, goal = 4, 3, 2 

visited = [[False for _ in range(jug2 + 1)] for _ in range(jug1 + 1)] 

def waterJug(vol1, vol2):
	
	if (vol1 == goal and vol2 == 0) or (vol2 == goal and vol1 == 0): 
		print(vol1,"\t", vol2)
		print("Solution Found")
		return True

	if visited[vol1][vol2]:
		return False
	
	visited[vol1][vol2] = True
	
	print(vol1,"\t", vol2)
	
	return (
        waterJug(0, vol2) or 
        waterJug(vol1, 0) or  
        waterJug(jug1, vol2) or  
        waterJug(vol1, jug2) or 
        waterJug(vol1 + min(vol2, (jug1 - vol1)), vol2 - min(vol2, (jug1 - vol1))) or  
        waterJug(vol1 - min(vol1, (jug2 - vol2)), vol2 + min(vol1, (jug2 - vol2)))  
    ) 

print("Steps: ") 
print("Jug1 \t Jug2 ")
print("----- \t ------")
waterJug(0, 0)
