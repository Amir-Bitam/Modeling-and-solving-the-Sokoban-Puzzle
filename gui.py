import pygame
import os

TILE = 64   # size of one cell in pixels
ART_DIR = os.path.join(os.path.dirname(__file__), "ART")


def load(name):
    path = os.path.join(ART_DIR, name + ".png")
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (TILE, TILE))


def draw_board(screen, state, img):
    for i in range(len(state.robot_block)):
        for j in range(len(state.robot_block[0])):
            pos = (j * TILE, i * TILE)
            floor = state.wall_space_obstacle[i][j]
            thing = state.robot_block[i][j]

            if floor == 'O':
                screen.blit(img["wall"], pos)
                continue

            screen.blit(img["space"], pos)
            if floor == 'S':
                screen.blit(img["target"], pos)

            if thing == 'B':
                screen.blit(img["box_on_target"] if floor == 'S' else img["box"], pos)
            elif thing == 'R':
                screen.blit(img["player"], pos)


def show_solution(goal_node, algo_name="", steps=0, elapsed=0.0, delay_ms=400):
    states = goal_node.getPath()
    h = len(states[0].robot_block)
    w = len(states[0].robot_block[0])

    pygame.init()
    screen = pygame.display.set_mode((w * TILE, h * TILE))
    pygame.display.set_caption(
        f"Sokoban — {algo_name} | Cost: {goal_node.g} | Steps explored: {steps} | Time: {elapsed:.2f}s"
    )
    img = {n: load(n) for n in ["wall", "space", "target", "box", "box_on_target", "player"]}

    frame = 0
    last = pygame.time.get_ticks()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if frame < len(states) - 1 and pygame.time.get_ticks() - last >= delay_ms:
            frame += 1
            last = pygame.time.get_ticks()

        draw_board(screen, states[frame], img)
        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()
