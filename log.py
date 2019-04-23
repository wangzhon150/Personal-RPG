import pygame
import cal
from typing import Dict, Tuple, Optional
from datetime import date
import calendar
from calendar import Calendar

LOG_BG_COLOUR = (68, 53, 46)
LOG_TITLE_COLOUR = (255, 255, 255)
BACK_BUTTON_COLOUR = (76, 74, 73)
ICON_TEXT_COLOUR = (255, 255, 255)


def run_log(day: Tuple[int, int, int]) -> None:
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Log')
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, LOG_BG_COLOUR, (20, 20, 460, 560))
    font = pygame.font.SysFont('CALISTO', 44)
    icon_font = pygame.font.SysFont('CALISTO', 28)
    d = date(day[0], day[1], day[2])
    date_surface = font.render(str(day[2]) + ' ' + str(d.strftime('%B'))
                               + ' ' + str(day[0]), 1, LOG_TITLE_COLOUR)
    screen.blit(date_surface, (30, 25))
    pygame.display.update()
    back_pos = (30, 540)
    pygame.draw.rect(screen, BACK_BUTTON_COLOUR,
                     (back_pos[0], back_pos[1], 90, 30))
    back_surface = icon_font.render('Return', 1, ICON_TEXT_COLOUR)
    screen.blit(back_surface, back_pos)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP and \
                    back_pos[0] <= event.pos[0] <= back_pos[0] + 100 and \
                    back_pos[1] <= event.pos[1] <= back_pos[1] + 90:
                return cal.run_calendar()
