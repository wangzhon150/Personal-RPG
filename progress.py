import pygame
import cal
import log
import json
from datetime import date
from typing import Dict
from math import floor

PROGRESS_BG_COLOUR = (68, 53, 46)
PROGRESS_TITLE_COLOUR = (255, 255, 255)
SUBTITLE_COLOUR = (255, 255, 255)
LINE_COLOUR = (255, 255, 255)
BUTTON_COLOUR = (76, 74, 73)
ICON_TEXT_COLOUR = (255, 255, 255)
TEXT_COLOUR = (255, 255, 255)
XP_COLOUR = (204, 170, 146)
SKILL_FOREGROUND = (255, 255, 255)
SKILL_BACKGROUND = (76, 74, 73)
SKILLS_FILE = 'skills.json'


def run_progress() -> None:
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Progress')
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, PROGRESS_BG_COLOUR, (20, 20, 760, 560))
    skills = import_skills()
    title_font = pygame.font.Font('calist.ttf', 40)
    subtitle_font = pygame.font.Font('calist.ttf', 24)
    text_font = pygame.font.Font('calist.ttf', 20)
    icon_font = pygame.font.Font('calist.ttf', 28)
    title_surface = title_font.render('Progress', 1, PROGRESS_TITLE_COLOUR)
    screen.blit(title_surface, (30, 25))
    pygame.draw.line(screen, LINE_COLOUR, (350, 30), (350, 570))
    back_pos = (30, 540)
    pygame.draw.rect(screen, BUTTON_COLOUR,
                     (back_pos[0], back_pos[1], 90, 30))
    back_surface = icon_font.render('Return', 1, ICON_TEXT_COLOUR)
    screen.blit(back_surface, (33, 540))
    surface_1 = subtitle_font.render('Adventurer ' + str(get_level_per_xp(skills['Adventurer'])), 1, SUBTITLE_COLOUR)
    xp_1 = subtitle_font.render(' (' + str(skills['Adventurer'] -
                                           get_xp_per_level(get_level_per_xp(skills['Adventurer']))) + '/'
                                + str(get_xp_per_level(get_level_per_xp(skills['Adventurer'])+1))
                                + ' XP)', 1, XP_COLOUR)
    width_1 = get_bar_width('Adventurer')
    pygame.draw.rect(screen, SKILL_BACKGROUND, (40, 133, 280, 22))
    pygame.draw.rect(screen, SKILL_FOREGROUND, (42, 135, width_1, 18))
    surface_2 = subtitle_font.render('Chronicler ' + str(get_level_per_xp(skills['Chronicler'])), 1, SUBTITLE_COLOUR)
    xp_2 = subtitle_font.render(' (' + str(skills['Chronicler'] -
                                           get_xp_per_level(get_level_per_xp(skills['Chronicler']))) + '/'
                                + str(get_xp_per_level(get_level_per_xp(skills['Chronicler'])+1))
                                + ' XP)', 1, XP_COLOUR)
    width_2 = get_bar_width('Chronicler')
    pygame.draw.rect(screen, SKILL_BACKGROUND, (40, 203, 280, 22))
    pygame.draw.rect(screen, SKILL_FOREGROUND, (42, 205, width_2, 18))
    surface_3 = subtitle_font.render('Diligent ' + str(get_level_per_xp(skills['Diligent'])), 1, SUBTITLE_COLOUR)
    xp_3 = subtitle_font.render(' (' + str(skills['Diligent'] -
                                           get_xp_per_level(get_level_per_xp(skills['Diligent']))) + '/'
                                + str(get_xp_per_level(get_level_per_xp(skills['Diligent'])+1))
                                + ' XP)', 1, XP_COLOUR)
    width_3 = get_bar_width('Diligent')
    pygame.draw.rect(screen, SKILL_BACKGROUND, (40, 273, 280, 22))
    pygame.draw.rect(screen, SKILL_FOREGROUND, (42, 275, width_3, 18))
    surface_4 = subtitle_font.render('Erudite ' + str(get_level_per_xp(skills['Erudite'])), 1, SUBTITLE_COLOUR)
    xp_4 = subtitle_font.render(' (' + str(skills['Erudite'] -
                                           get_xp_per_level(get_level_per_xp(skills['Erudite']))) + '/'
                                + str(get_xp_per_level(get_level_per_xp(skills['Erudite'])+1))
                                + ' XP)', 1, XP_COLOUR)
    width_4 = get_bar_width('Erudite')
    pygame.draw.rect(screen, SKILL_BACKGROUND, (40, 343, 280, 22))
    pygame.draw.rect(screen, SKILL_FOREGROUND, (42, 345, width_4, 18))
    surface_5 = subtitle_font.render('Hardy ' + str(get_level_per_xp(skills['Hardy'])), 1, SUBTITLE_COLOUR)
    xp_5 = subtitle_font.render(' (' + str(skills['Hardy'] -
                                           get_xp_per_level(get_level_per_xp(skills['Hardy']))) + '/'
                                + str(get_xp_per_level(get_level_per_xp(skills['Hardy']) + 1))
                                + ' XP)', 1, XP_COLOUR)
    width_5 = get_bar_width('Hardy')
    pygame.draw.rect(screen, SKILL_BACKGROUND, (40, 413, 280, 22))
    pygame.draw.rect(screen, SKILL_FOREGROUND, (42, 415, width_5, 18))
    surface_6 = subtitle_font.render('Wizard ' + str(get_level_per_xp(skills['Wizard'])), 1, SUBTITLE_COLOUR)
    xp_6 = subtitle_font.render(' (' + str(skills['Wizard'] -
                                           get_xp_per_level(get_level_per_xp(skills['Wizard']))) + '/'
                                + str(get_xp_per_level(get_level_per_xp(skills['Wizard'])+1))
                                + ' XP)', 1, XP_COLOUR)
    width_6 = get_bar_width('Wizard')
    pygame.draw.rect(screen, SKILL_BACKGROUND, (40, 483, 280, 22))
    pygame.draw.rect(screen, SKILL_FOREGROUND, (42, 485, width_6, 18))
    screen.blit(surface_1, (40, 100))
    screen.blit(surface_2, (40, 170))
    screen.blit(surface_3, (40, 240))
    screen.blit(surface_4, (40, 310))
    screen.blit(surface_5, (40, 380))
    screen.blit(surface_6, (40, 450))
    screen.blit(xp_1, (220, 100))
    screen.blit(xp_2, (220, 170))
    screen.blit(xp_3, (220, 240))
    screen.blit(xp_4, (220, 310))
    screen.blit(xp_5, (220, 380))
    screen.blit(xp_6, (220, 450))
    # other side
    today = date.today()
    pos_dict = {}
    pygame.draw.rect(screen, BUTTON_COLOUR, (130, 540, 77, 30))
    diary_surface = icon_font.render('Diary', 1, ICON_TEXT_COLOUR)
    screen.blit(diary_surface, (133, 540))
    date_surface = subtitle_font.render('It is ' + today.strftime('%A') + ', ' + str(today.day) + ' '
                                        + today.strftime('%B') + ' ' + str(today.year) + '.', 1, SUBTITLE_COLOUR)
    selection_surface = subtitle_font.render('How did you spend the day?', 1, SUBTITLE_COLOUR)
    pygame.draw.rect(screen, BUTTON_COLOUR, (360, 126, 95, 30))
    a_1 = text_font.render('Discovery', 1, TEXT_COLOUR)
    pos_dict[(360, 126, 95, 30)] = ('Adventurer', 3, 'You discovered a new location: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (463, 126, 60, 30))
    a_2 = text_font.render('Event', 1, TEXT_COLOUR)
    pos_dict[(463, 126, 60, 30)] = ('Adventurer', 4, 'You attended an event: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (530, 126, 80, 30))
    a_3 = text_font.render('Journey', 1, TEXT_COLOUR)
    pos_dict[(530, 126, 80, 30)] = ('Adventurer', 3, 'You journeyed to: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (360, 195, 110, 30))
    c_1 = text_font.render('Chronicling', 1, TEXT_COLOUR)
    pos_dict[(360, 195, 110, 30)] = ('Chronicler', 1, 'You chronicled the day\'s events', False)
    pygame.draw.rect(screen, BUTTON_COLOUR, (478, 195, 100, 30))
    c_2 = text_font.render('Journaling', 1, TEXT_COLOUR)
    pos_dict[(478, 195, 100, 30)] = ('Chronicler', 2, 'You wrote in your log diary', False)
    pygame.draw.rect(screen, BUTTON_COLOUR, (360, 265, 95, 30))
    d_1 = text_font.render('Early Bird', 1, TEXT_COLOUR)
    pos_dict[(360, 265, 95, 30)] = ('Diligent', 2, 'You began your day bright and early', False)
    pygame.draw.rect(screen, BUTTON_COLOUR, (463, 265, 75, 30))
    d_2 = text_font.render('Lecture', 1, TEXT_COLOUR)
    pos_dict[(463, 265, 75, 30)] = ('Diligent', 1, 'You attended a lecture for: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (546, 265, 70, 30))
    d_3 = text_font.render('Review', 1, TEXT_COLOUR)
    pos_dict[(546, 265, 70, 30)] = ('Diligent', 2, 'You reviewed your notes for: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (624, 265, 55, 30))
    d_4 = text_font.render('Tasks', 1, TEXT_COLOUR)
    pos_dict[(624, 265, 55, 30)] = ('Diligent', 2, 'You made some routine progress on: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (360, 335, 75, 30))
    e_1 = text_font.render('Articles', 1, TEXT_COLOUR)
    pos_dict[(360, 335, 75, 30)] = ('Erudite', 2, 'You read some informational articles from: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (443, 335, 60, 30))
    e_2 = text_font.render('Books', 1, TEXT_COLOUR)
    pos_dict[(443, 335, 60, 30)] = ('Erudite', 3, 'You finished a chapter of: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (511, 335, 60, 30))
    e_3 = text_font.render('Trivia', 1, TEXT_COLOUR)
    pos_dict[(511, 335, 60, 30)] = ('Erudite', 2, 'You learned about: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (360, 405, 55, 30))
    h_1 = text_font.render('Walk', 1, TEXT_COLOUR)
    pos_dict[(360, 405, 55, 30)] = ('Hardy', 3, 'You walked a great many steps: ', True)
    pygame.draw.rect(screen, BUTTON_COLOUR, (423, 405, 85, 30))
    h_2 = text_font.render('Workout', 1, TEXT_COLOUR)
    pos_dict[(423, 405, 85, 30)] = ('Hardy', 3, 'You worked out', False)
    pygame.draw.rect(screen, BUTTON_COLOUR, (360, 475, 75, 30))
    w_1 = text_font.render('Sorcery', 1, TEXT_COLOUR)
    pos_dict[(360, 475, 75, 30)] = ('Wizard', 3, 'You made some headway on: ', True)
    screen.blit(a_1, (365, 128))
    screen.blit(a_2, (468, 128))
    screen.blit(a_3, (536, 128))
    screen.blit(c_1, (365, 197))
    screen.blit(c_2, (483, 197))
    screen.blit(d_1, (365, 268))
    screen.blit(d_2, (468, 268))
    screen.blit(d_3, (549, 268))
    screen.blit(d_4, (627, 268))
    screen.blit(e_1, (365, 338))
    screen.blit(e_2, (447, 338))
    screen.blit(e_3, (514, 338))
    screen.blit(h_1, (365, 408))
    screen.blit(h_2, (426, 408))
    screen.blit(w_1, (365, 478))
    screen.blit(date_surface, (360, 35))
    screen.blit(selection_surface, (360, 70))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP and \
                    back_pos[0] <= event.pos[0] <= back_pos[0] + 100 and \
                    back_pos[1] <= event.pos[1] <= back_pos[1] + 90:
                return cal.run_calendar()
            elif event.type == pygame.MOUSEBUTTONUP and \
                    130 <= event.pos[0] <= 207 and \
                    540 <= event.pos[1] <= 570:
                text = input('Diary entry: ')
                log.add_to_log(today, '!!DIARY', text)
            elif event.type == pygame.MOUSEBUTTONUP:
                for pos in pos_dict:
                    if pos[0] <= event.pos[0] <= pos[0] + pos[2] and \
                            pos[1] <= event.pos[1] <= pos[1] + pos[3]:
                        tup = pos_dict[pos]
                        return run_progress_update(tup[0], tup[1], tup[2], tup[3])


def run_progress_update(skill: str, xp: int, text: str, input_: bool) -> None:
    screen = pygame.display.set_mode((500, 200))
    pygame.display.set_caption('Update Progress')
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, PROGRESS_BG_COLOUR, (20, 20, 460, 160))
    text_font = pygame.font.Font('calist.ttf', 20)
    icon_font = pygame.font.Font('calist.ttf', 28)
    back_pos = (30, 140)
    pygame.draw.rect(screen, BUTTON_COLOUR,
                     (back_pos[0], back_pos[1], 90, 30))
    back_surface = icon_font.render('Cancel', 1, ICON_TEXT_COLOUR)
    screen.blit(back_surface, (33, 140))
    pygame.draw.rect(screen, BUTTON_COLOUR, (408, 140, 60, 30))
    save_surface = icon_font.render('Save', 1, ICON_TEXT_COLOUR)
    screen.blit(save_surface, (412, 140))
    if text[-1] == ' ':
        prompt_surface = text_font.render(text, 1, TEXT_COLOUR)
    else:
        prompt_surface = text_font.render(text + '.', 1, TEXT_COLOUR)
    screen.blit(prompt_surface, (40, 40))
    pygame.display.flip()
    if input_:
        text += input(text)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP and \
                    back_pos[0] <= event.pos[0] <= back_pos[0] + 100 and \
                    back_pos[1] <= event.pos[1] <= back_pos[1] + 90:
                return run_progress()
            elif event.type == pygame.MOUSEBUTTONUP and \
                    408 <= event.pos[0] <= 468 and \
                    140 <= event.pos[1] <= 170:
                return update_progress(skill, xp, text)


def update_progress(skill: str, xp: int, text: str) -> None:
    skills = import_skills()
    skills[skill] += xp
    with open(SKILLS_FILE, 'w') as o:
        json.dump(skills, o)
    text += '.'
    if skill == 'Adventurer':
        log.add_to_log(date.today(), 'Adventure', text)
    elif skill == 'Diligent':
        log.add_to_log(date.today(), 'Diligence', text)
    elif skill == 'Erudite':
        log.add_to_log(date.today(), 'Erudition', text)
    elif skill == 'Hardy':
        log.add_to_log(date.today(), 'Hardiness', text)
    elif skill == 'Wizard':
        log.add_to_log(date.today(), 'Wizardry', text)
    return run_progress()


def import_skills() -> Dict[str, int]:
    with open(SKILLS_FILE) as o:
        skills = json.load(o)
    return skills


def get_bar_width(name: str) -> int:
    skills = import_skills()
    xp = skills[name]
    base = get_xp_per_level(get_level_per_xp(xp))
    percent = (xp-base) / (get_xp_per_level(get_level_per_xp(xp)+1) - get_xp_per_level(get_level_per_xp(xp)))
    return floor(percent * 278)


def get_xp_per_level(lvl: int) -> int:
    if lvl <= 0:
        return 0
    elif lvl == 1:
        return 5
    elif lvl == 2:
        return 10
    else:
        return get_xp_per_level(lvl-1) + get_xp_per_level(lvl-2)


def get_level_per_xp(xp: int) -> int:
    if xp <= 4:
        return 0
    else:
        lvl = 1
        while True:
            if xp < get_xp_per_level(lvl):
                return lvl-1
            lvl += 1
