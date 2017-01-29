E = -1 # Empty
R = 0 # Red
G = 1 # Green
Y = 2 # Yellow
B = 3 # Blue
O = 4 # Orange



class flow_solver(object):
    
    def __init__(self):
        self.rows = 0
        self.columns = 0
        
    def load(self, tablero):
        self.tablero = tablero
        self.rows = len(tablero)
        self.columns = len(tablero[0])
        
        self.cabezas = []
        for i in range(5):
            self.cabezas.append([])
            
        for i in range(self.rows):
            for j in range(self.columns):
                color = self.tablero[i][j]
                if color != E:
                    self.cabezas[color].append([i,j])
        

    def solve(self):
        finished = [False]*5
        
        
        flag = True
        while flag:
            flag = False
            for color in range(len(self.cabezas)):
                if not finished[color]:
                    camino = self.cabezas[color]
                    for i in range(2):
                        cabeza = camino[i]
                        otra = camino[1-i]
                        pos = self.empty_adjacents(cabeza[0], cabeza[1])
                        if len(pos) == 1:
                            cabeza[0] = pos[0][0]
                            cabeza[1] = pos[0][1]
                            flag = True
                            self.tablero[cabeza[0]][cabeza[1]] = color
                            if abs(cabeza[0]-otra[0]) + abs(cabeza[1]-otra[1]) == 1:
                                finished[color] = True
                                break
                            
                            
                    

        '''
        for i in range(self.rows):
            for j in range(self.columns):
                if self.tablero[i][j] != E:
                    print self.empty_adjacents(i, j)
        '''
        
    
    def empty_adjacents(self, row, col):
        adj = []
        if row > 0:
            if self.tablero[row-1][col] == E:
                adj.append((row-1, col))
        if col > 0:
            if self.tablero[row][col-1] == E:
                adj.append((row, col-1))
        if row +1 < self.rows:
            if self.tablero[row+1][col] == E:
                adj.append((row+1, col))
        if col +1 < self.columns:
            if self.tablero[row][col+1] == E:
                adj.append((row, col+1))
        return adj

    def __str__(self):
        t = ""
        for i in range(self.rows):
            for j in range(self.columns):
                t += str(tablero[i][j]) + " "
            t += "\n"
        return t
            
            
if __name__ == "__main__":
    solver = flow_solver() # resuelve tableros 5 x 5
    tablero = [[R, E, G, E, Y],
          [E, E, B, E, O],
          [E, E, E, E, E],
          [E, G, E, Y, E],
          [E, R, B, O, E]]
    solver.load(tablero)
    solver.solve()
    print solver
    
    tablero = [[E, Y, B, G, E],
          [E, E, E, R, E],
          [E, E, R, E, E],
          [Y, E, E, O, E],
          [B, E, O, G, E]]
    solver.load(tablero)
    solver.solve()
    print solver