import pygame
import cal

PROGRESS_BG_COLOUR = (68, 53, 46)
PROGRESS_TITLE_COLOUR = (255, 255, 255)
LINE_COLOUR = (255, 255, 255)
BUTTON_COLOUR = (76, 74, 73)
ICON_TEXT_COLOUR = (255, 255, 255)
SKILLS_FILE = 'skills.json'


def run_progress() -> None:
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Progress')
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, PROGRESS_BG_COLOUR, (20, 20, 760, 560))
    title_font = pygame.font.SysFont('CALISTO, CALISTOMT', 40)
    text_font = pygame.font.SysFont('CALISTO, CALISTOMT', 16)
    icon_font = pygame.font.SysFont('CALISTO, CALISTOMT', 28)
    title_surface = title_font.render('Progress', 1, PROGRESS_TITLE_COLOUR)
    screen.blit(title_surface, (30, 25))
    pygame.draw.line(screen, LINE_COLOUR, (350, 30), (350, 570))
    back_pos = (30, 540)
    pygame.draw.rect(screen, BUTTON_COLOUR,
                     (back_pos[0], back_pos[1], 90, 30))
    back_surface = icon_font.render('Return', 1, ICON_TEXT_COLOUR)
    screen.blit(back_surface, (33, 540))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP and \
                    back_pos[0] <= event.pos[0] <= back_pos[0] + 100 and \
                    back_pos[1] <= event.pos[1] <= back_pos[1] + 90:
                return cal.run_calendar()

