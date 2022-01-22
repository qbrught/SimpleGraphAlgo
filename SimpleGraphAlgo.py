import pygame
import random
import heapq
pygame.font.init()
screen = pygame.display.set_mode((510, 510))
pygame.display.set_caption("sort")
width = 500
length = 500
circles = [0]*64
circ_clr = ([(0,0,0)]*64)
clr_ind = 0
source = random.randrange(0,7)
end = random.randrange(0,64)
circ_diam = (width - 10)/8
clr = [(0, 0, 0), (255, 0, 0), 
(0,255,0), (128, 128, 128)]
fnt = pygame.font.SysFont("timesnewroman", 20)
def generate_arr():
    for i in range(0, 64):
        circ_clr[i]= clr[0]
        circles[i]= random.randrange(0, 11)
generate_arr() 
#update screen
def refill():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(5)
#draw on screen
def draw():
    for x in range(0,64):     
            num = fnt.render(str(circles[x]),1,(0,0,0))  
            pygame.draw.circle(screen, circ_clr[x],
                ((x%8*(circ_diam+2)+35),(int(x/8)*(circ_diam+2))+35),circ_diam/2,3)    
            screen.blit(num,((x%8*(circ_diam+2)+30,(int(x/8)*circ_diam+2)+25))) 
class simple():
    def getadj(self,circle):
        if (circle%8 != 0 and circle%8+1 != 8):
            if circle >= 8 and circle <= 55:
                return([circle-8,circle+1,circle+8,circle-1]) 
            else:
                if circle < 8:
                    return([-1,circle+1,circle+8,circle-1])
                else:
                    return([circle-8,circle+1,-1,circle-1])
        else:
            if circle == 0:
                return([-1,circle+1,circle+8,-1])
            elif circle == 56:
                return([circle-8,circle+1,-1,-1])
            elif circle == 7:
                return([-1,-1,circle+8,circle-1])
            elif circle == 63:
                return([circle-8,-1,-1,circle-1]) 
            else:
                if circle %8 == 0:
                    return([circle-8,circle+1,circle+8,-1])
                else:
                    return([circle-8,-1,circle+8,circle-1])

    def searchalgo(self,start,goal):
        visited = []
        pq = []
        pq.append((start,circles[start]))
        dm = []
        while len(pq) != 0:
            heapq.heapify(pq)
            current = heapq.heappop(pq)
            if current[0] not in visited:
                visited.append(current[0])
                dm.append((current[0],current[1]))
                if current[0]==goal:
                    if start > goal:
                        return(dm[-1][1])
                    elif goal > start:
                        return(dm[goal][1])
                for child in self.getadj(current[0]):
                    if child !=-1:
                        if child not in visited:
                            heapq.heappush(pq,(child,circles[child]+current[1]))

        print(dm)
def main():
    run = True
    oldend = -1
    oldstart = -1
    s1 = simple()
    while run:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    if oldstart >= 0:
                        for x in range(0,64):
                            circ_clr[x] = clr[0]
                        circ_clr[end] = clr[1]
                        refill()
                    start = random.randrange(0,7)
                    circ_clr[start] = clr[2]
                    refill()
                    oldstart = start
                if event.key == pygame.K_r:
                    if oldend >= 0:
                        for x in range(0,64):
                            circ_clr[x] = clr[0]
                        circ_clr[start] = clr[2]
                        refill()
                    end = random.randrange(0,64)
                    circ_clr[end] = clr[1]
                    refill()
                    oldend = end
                if event.key == pygame.K_z:
                    print(s1.searchalgo(start,end))

        draw()       
        pygame.display.update() 
    pygame.quit()    

if __name__ == "__main__":
    main()          
