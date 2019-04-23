from __future__ import annotations
import pygame
import cal
import json
from typing import Dict, Tuple, Optional
from datetime import date

LOG_BG_COLOUR = (68, 53, 46)
LOG_TITLE_COLOUR = (255, 255, 255)
LOG_TEXT_COLOUR = (209, 203, 202)
BACK_BUTTON_COLOUR = (76, 74, 73)
ICON_TEXT_COLOUR = (255, 255, 255)
MASTER_LOG = 'master_log.json'


def run_log(day: Tuple[int, int, int]) -> None:
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Log')
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, LOG_BG_COLOUR, (20, 20, 460, 560))
    title_font = pygame.font.SysFont('CALISTO, CALISTOMT', 30)
    text_font = pygame.font.SysFont('CALISTO, CALISTOMT', 16)
    icon_font = pygame.font.SysFont('CALISTO, CALISTOMT', 28)
    text_font_height = text_font.size("Tg")[1]
    d = date(day[0], day[1], day[2])
    date_surface = title_font.render(str(day[2]) + ' ' + str(d.strftime('%B'))
                                     + ' ' + str(day[0]), 1, LOG_TITLE_COLOUR)
    screen.blit(date_surface, (30, 25))
    pygame.display.update()
    back_pos = (30, 540)
    pygame.draw.rect(screen, BACK_BUTTON_COLOUR,
                     (back_pos[0], back_pos[1], 90, 30))
    back_surface = icon_font.render('Return', 1, ICON_TEXT_COLOUR)
    screen.blit(back_surface, back_pos)
    master_log = import_master_log()
    if str(date(day[0], day[1], day[2])) in master_log:
        event_dict = master_log[str(date(day[0], day[1], day[2]))]
        x = 40
        y = 70
        for event in event_dict:
            event_text = event.upper() + ': ' + event_dict[event]
            lines = \
                draw_text(screen, event_text, LOG_TEXT_COLOUR, (x, y, 420, 530),
                          text_font)[1]
            y += text_font_height * lines
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP and \
                    back_pos[0] <= event.pos[0] <= back_pos[0] + 100 and \
                    back_pos[1] <= event.pos[1] <= back_pos[1] + 90:
                return cal.run_calendar()


def import_master_log() -> Dict[str, Dict[str, str]]:
    with open(MASTER_LOG) as o:
        master_log = json.load(o)
    return master_log


def add_to_log(date_: date, category: str, description: str) -> None:
    master_log = import_master_log()
    if str(date_) in master_log:
        if category in master_log[str(date_)]:
            master_log[str(date_)][category] += ' ' + description
        else:
            master_log[str(date_)][category] = description
    else:
        master_log[str(date_)] = {}
        master_log[str(date_)][category] = description
    with open(MASTER_LOG, 'w') as o:
        json.dump(master_log, o)


def draw_text(surface: pygame.Surface, text: str, colour: Tuple[int, int, int],
              rect: Tuple[int, int, int, int], font: pygame.font) -> \
        Tuple[Optional[str], int]:
    """Adapted from https://www.pygame.org/wiki/TextWrap"""
    y = rect[1]
    line_spacing = -2
    lines = 0
    font_height = font.size("Tg")[1]
    while text:
        i = 1
        lines += 1
        if y + font_height > rect[1] + rect[3]:
            return '', lines
        while font.size(text[:i])[0] < rect[2] and i < len(text):
            i += 1
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1
        image = font.render(text[:i], 1, colour)
        surface.blit(image, (rect[0], y))
        y += font_height + line_spacing
        text = text[i:]
    return text, lines
