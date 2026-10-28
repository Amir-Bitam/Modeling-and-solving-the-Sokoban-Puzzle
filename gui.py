import pygame
import os

TILE = 64   # size of one cell in pixels
ART_DIR = os.path.join(os.path.dirname(__file__), "ART") # builds path where art is

# function that loads an image (gets it from disque and resizes it)
def load(name):
    path = os.path.join(ART_DIR, name + ".png")
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (TILE, TILE))


# function that draws one state. (img is a dictionary of loaded images)
def draw_board(screen, state, img):
    for i in range(len(state.robot_block)):
        for j in range(len(state.robot_block[0])):
            pos = (j * TILE, i * TILE)    #position of the first pixel
            floor = state.wall_space_obstacle[i][j] #read static cell
            thing = state.robot_block[i][j] # read dynamic cell 

            # paste images in their positions
            if floor == 'O': #if wall
                screen.blit(img["wall"], pos)
                continue

            screen.blit(img["space"], pos)  # if not wall = space
            if floor == 'S': # if target, paste target marker on top of space
                screen.blit(img["target"], pos)

            if thing == 'B': # if box, paste box, if target, paste box on target
                screen.blit(img["box_on_target"] if floor == 'S' else img["box"], pos)
            elif thing == 'R':
                screen.blit(img["player"], pos) #else print robot 


def show_solution(goal_node, algo_name="", steps=0, elapsed=0.0, delay_ms=400):
    states = goal_node.getPath() #get list of path
    h = len(states[0].robot_block)
    w = len(states[0].robot_block[0])

    pygame.init() #start pygame
    screen = pygame.display.set_mode((w * TILE, h * TILE)) #creates window with size of board

    # dislay on windown title bar
    pygame.display.set_caption(
        f"Sokoban — {algo_name} | Cost: {goal_node.g} | Steps explored: {steps} | Time: {elapsed:.2f}s"
    )

    #build a dictionary with all loaded images
    img = {n: load(n) for n in ["wall", "space", "target", "box", "box_on_target", "player"]}

    frame = 0
    last = pygame.time.get_ticks() #returns milliseconds since pygame started

    running = True #keeps game loop running
    while running:
        for event in pygame.event.get(): #listens for the quit action
            if event.type == pygame.QUIT:
                running = False

        if frame < len(states) - 1 and pygame.time.get_ticks() - last >= delay_ms: #we havent reached last board and at least 400ms have passed since last change
            frame += 1 #go to next board
            last = pygame.time.get_ticks() #final bard stays on screen 

        draw_board(screen, states[frame], img) #draw current board
        pygame.display.flip() #show on screen
        pygame.time.Clock().tick(30)

    pygame.quit()
