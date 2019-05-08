import pygame
import log
import progress
from typing import Dict, Tuple
from datetime import date
import calendar
from calendar import Calendar

BG_COLOUR = (68, 53, 46)
TITLE_COLOUR = (255, 255, 255)
TODAY_COLOUR = (100, 0, 0)
DAY_COLOUR = (44, 44, 44)
CURR_MONTH_COLOUR = (145, 133, 127)
OTHER_MONTH_COLOUR = (96, 88, 84)
BUTTON_COLOUR = (76, 74, 73)
ICON_TEXT_COLOUR = (255, 255, 255)


def run_calendar() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Calendar')
    pygame.draw.rect(screen, BG_COLOUR, (20, 20, 760, 560))
    font = pygame.font.Font('calist.ttf', 32)
    date_dict = draw_calendar(screen, font)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP and \
                    select_day(event.button, event.pos, date_dict):
                return
            elif event.type == pygame.MOUSEBUTTONUP and \
                    650 <= event.pos[0] <= 760 and \
                    40 <= event.pos[1] <= 75:
                return progress.run_progress()
        pygame.display.flip()


def draw_calendar(screen: pygame.Surface, font: pygame.font.SysFont) \
        -> Dict[Tuple[int, int, int], Tuple[int, int, int, int]]:
    c = Calendar(calendar.SUNDAY)
    today = date.today()
    date_dict = {}
    x = 20
    y = 125
    large_font = pygame.font.Font('calist.ttf', 54)
    icon_font = pygame.font.Font('calist.ttf', 28)
    month_surface = large_font.render(str(today.strftime('%B')), 1,
                                      TITLE_COLOUR)
    screen.blit(month_surface, (75, 40))
    pygame.draw.rect(screen, BUTTON_COLOUR, (650, 40, 110, 35))
    skills_surface = icon_font.render('Progress', 1, ICON_TEXT_COLOUR)
    screen.blit(skills_surface, (654, 40))
    for item in c.itermonthdates(today.year, today.month):
        if item.month == today.month:
            pygame.draw.rect(screen, CURR_MONTH_COLOUR, (x, y, 100, 75))
            if item.day == today.day:
                day_surface = font.render(str(item.day), 1, TODAY_COLOUR)
            else:
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


def select_day(button: int, pos: Tuple[int, int],
               date_dict: Dict[Tuple[int, int, int],
                               Tuple[int, int, int, int]]) -> bool:
    if button == 1:
        for day in date_dict:
            d = date(day[0], day[1], day[2])
            if d <= date.today() and \
                    date_dict[day][0] <= pos[0] <= date_dict[day][0] \
                    + date_dict[day][2] and date_dict[day][1] <= pos[1] \
                    <= date_dict[day][1] + date_dict[day][3]:
                log.run_log(day)
                return True
    return False


if __name__ == '__main__':
    run_calendar()
    pygame.quit()
