import pygame
import log
from typing import Dict, Tuple, Optional
from datetime import date
import calendar
from calendar import Calendar

BG_COLOUR = (68, 53, 46)
TITLE_COLOUR = (255, 255, 255)
DAY_COLOUR = (44, 44, 44)
CURR_MONTH_COLOUR = (145, 133, 127)
OTHER_MONTH_COLOUR = (96, 88, 84)


def run_calendar() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Calendar')
    while True:
        pygame.draw.rect(screen, BG_COLOUR, (20, 20, 760, 560))
        font = pygame.font.SysFont('CALISTO', 32)
        date_dict = draw_calendar(screen, font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP and \
                    select_day(screen, event.button, event.pos, date_dict):
                return
        pygame.display.flip()


def draw_calendar(screen: pygame.Surface, font: pygame.font.SysFont) \
        -> Dict[Tuple[int, int, int], Tuple[int, int, int, int]]:
    c = Calendar(calendar.SUNDAY)
    today = date.today()
    date_dict = {}
    x = 20
    y = 125
    large_font = pygame.font.SysFont('CALISTO', 54)
    month_surface = large_font.render(str(today.strftime('%B')), 1,
                                      TITLE_COLOUR)
    screen.blit(month_surface, (75, 40))
    for item in c.itermonthdates(today.year, today.month):
        if item.month == today.month:
            pygame.draw.rect(screen, CURR_MONTH_COLOUR, (x, y, 100, 75))
            day_surface = font.render(str(item.day), 1, DAY_COLOUR)
        else:
            pygame.draw.rect(screen, OTHER_MONTH_COLOUR, (x, y, 100, 75))
            day_surface = font.render(str(item.day), 1, DAY_COLOUR)
        date_dict[(item.year, item.month, item.day)] = (x, y, 100, 75)
        screen.blit(day_surface, (x + 5, y))
        if item.weekday() == 5:
            y += 95
            x = 20
        else:
            x += 110
    return date_dict


def select_day(screen: pygame.Surface, button: int, pos: Tuple[int, int],
               date_dict: Dict[Tuple[int, int, int],
                               Tuple[int, int, int, int]]) -> bool:
    if button == 1:
        for day in date_dict:
            if date_dict[day][0] <= pos[0] <= date_dict[day][0] \
                    + date_dict[day][2] and date_dict[day][1] <= pos[1] \
                    <= date_dict[day][1] + date_dict[day][3]:
                log.run_log(day)
                return True
    return False


if __name__ == '__main__':
    run_calendar()
