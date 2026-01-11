import pygame
from queue import PriorityQueue

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw, start):
    while current in came_from:
        current = came_from[current]
        
        if current != start:
            current.make_path()
            draw()

# G = quanti passi ho fatto per arrivare qua
# H = quanto sono lontano dalla fine? in linea d'area
# F = G + H, piu bassa è la F meglio è

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue() 
    
    open_set.put((0, count, start)) # questo è un taccuino delle cose da controllare, inizia con dentro solo start perche partiamo da li
    
    came_from = {}
    
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start} # serve per velocizzare la ricerca della presenza di un indice senza stare a controllare tutti gli inidici dentro

    while not open_set.empty(): # finche il taccuino ha elementi da controllare allora non esco dal while
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2] # controllo il taccuino, ho 10 elementi da controllare ma in cima, grazie a PriorityQueue() ho sempre l'elemento con la F minore
        open_set_hash.remove(current) # dopo aver scelto la mossa da controllare la rimuovo dal taccuino

        if current == end: # se sono arrivato alla fine allora ripercorro tutto il percorso fatto e all'indietro e colorandolo via via
            reconstruct_path(came_from, end, draw, start)
            end.make_end()
            return True

        for neighbor in current.neighbors: # se non sono arrivato alla fine allora guardo i miei vicini
            temp_g_score = g_score[current] + 1 # +1 è il costo di fare quel passo fino al vicino

            if temp_g_score < g_score[neighbor]: # questo if serve principalmente s eho gia esplorato quel vicino, se ha una G minore vuol dire che dalla partenza a quel vicino c'è una strada piu veloce rispetto a quella che ho seguito adesso

                # se il vicino non è mai stato esplorato oppure ci ho messo meno ad arrivare adesso
                came_from[neighbor] = current # aggiorno la mia lista del percorso seguito
                g_score[neighbor] = temp_g_score # aggiorno la g del vicino
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos()) # calcolo la f del vicino
                
                if neighbor not in open_set_hash: # se il mio vicino non era ancora stato esplorato lo aggiungo alla lista da visitare del mio taccuino
                    count += 1 # utilizzato da priorityqueue in caso di g uguale 
                    open_set.put((f_score[neighbor], count, neighbor)) # aggiungo al mio taccuino di celle da controllare il mio vicino, cioè potrei spostarmi lì se non trovo di meglio'
                    open_set_hash.add(neighbor) # aggiungo alla lista hash il mio vicino così quando avrò la necessità di controllare la sua presenza sarà instantanea
                    if neighbor != end:
                        neighbor.make_open() # coloro il vicino per far capire che l'ho aggiunta al taccuino
        draw() # disegno la mappa

        if current != start:
            current.make_closed() # se mi sono spostato e non sono tornato su start allora coloro in rosso per far capire che ho gia controlato questa casella

    return False