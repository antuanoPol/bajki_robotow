#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from statics import *

questions_datas = []

question_data_1 = {}
question_data_1['TEXT'] = [u"Jak nazywał się strachliwy król który był następcą Heliksandra? (Naciśnij 1, 2 lub 3)",
                           u"1. Król Midas",
                           u"2. Król Murdas",
                           u"3. Miał dwa imiona Automateusza i Herkules"
                           ]
question_data_1['ANSWER'] = 2

question_data_2 = {}
question_data_2['TEXT'] = [u"Ilu było elektrycerzy? (Naciśnij 1, 2 lub 3)",
                           u"1. Trzech",
                           u"2. Sześciu",
                           u"3. Pięciu"
                           ]
question_data_2['ANSWER'] = 1

question_data_3 = {}
question_data_3['TEXT'] = [u"Kto był władcą Kybery? (Naciśnij 1, 2 lub 3)",
                           u"1. Poleander",
                           u"2. W króleswtie panowało bezkrólewie",
                           u"3. Był nim Architor!"
                           ]
question_data_3['ANSWER'] = 1

question_data_4 = {}
question_data_4['TEXT'] = ["Kto napisał książkę ""Bajki robotów"" ? (Naciśnij 1, 2 lub 3)",
                           u"1. Olga Tokarczuk",
                           u"2. Jan Brzechwa",
                           u"3. Stanisław Lem"
                           ]
question_data_4['ANSWER'] = 3

question_data_5 = {}
question_data_5['TEXT'] = [u"Kto został nowym władcą Aktynurii ? (Naciśnij 1, 2 lub 3)",
                           u"1. Został nim syn obecnego władcy",
                           u"2. Kosmogonik",
                           u"3. Pyron"
                           ]
question_data_5['ANSWER'] = 3


question_data_6 = {}
question_data_6['TEXT'] = [u"Jak nazywał się elektroniczny przyjaciel Automateusza? (Naciśnij 1, 2 lub 3)",
                           u"1. Wok",
                           u"2. Nie miał imienia wszyscy nazywali go komputerkiem",
                           u"3. Wuch"
                           ]
question_data_6['ANSWER'] = 3


question_data_7 = {}
question_data_7['TEXT'] = [u"Kto wszczął ucieczkę mgławic? (Naciśnij 1, 2 lub 3)",
                           u"1. Mikromił i Gigancyn",
                           u"2. Astronomowie",
                           u"3. Nikt tego nie wie"
                           ]
question_data_7['ANSWER'] = 1

question_data_8 = {}
question_data_8['TEXT'] = [u"Ile planet utworzył uczeń Kosmogonika? (Naciśnij 1, 2 lub 3)",
                           u"1. Pięć",
                           u"2. Dziewięć",
                           u"3. Trzy"
                           ]
question_data_8['ANSWER'] = 3

question_data_9 = {}
question_data_9['TEXT'] = [u"Jak miał na imię król który kolekcjonował zegary? (Naciśnij 1, 2 lub 3)",
                           u"1. Boludar",
                           u"2. Homos",
                           u"3. Erg"
                           ]
question_data_9['ANSWER'] = 1




questions_datas.append(question_data_1)
questions_datas.append(question_data_2)
questions_datas.append(question_data_3)
questions_datas.append(question_data_4)
questions_datas.append(question_data_5)
questions_datas.append(question_data_6)
questions_datas.append(question_data_7)
questions_datas.append(question_data_8)
questions_datas.append(question_data_9)

class Question(pygame.sprite.Sprite):
    def __init__(self, question_data):
        pygame.sprite.Sprite.__init__(self)
        self.question_data_text = question_data['TEXT']
        self.question_data_answer = question_data['ANSWER']
        self.width = 60
        self.height = 40
        self.image_org = pygame.image.load(path.join(terminal_dir, "terminal.png"))
        self.image = pygame.transform.scale(self.image_org, (0, 0))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 15
        self.frame = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.question_with_answers_surfs = []
        self.selected = -1
        self.initialized = False
        self.answer_points = -1
        self.finished = False
        self._layer = 5
        for text in self.question_data_text:
            self.question_with_answers_surfs.append(self.font.render(text, 1, WHITE))

    def update(self):
        if not self.initialized:
            return

        if self.answer_points > -1:
            self.handle_ending()
            return

        self.check_key()
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate and self.frame < 14:
            self.last_update = now
            self.frame += 1

        self.image = pygame.transform.scale(self.image_org, (self.width * self.frame, self.height * self.frame))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.image.set_colorkey(WHITE)

        if self.frame == 14:
            self.draw_question()

        self.draw_confirmation()

    def handle_ending(self):
        now = pygame.time.get_ticks()
        if now - self.last_update < 500:
            self.font = pygame.font.SysFont("Arial", 40)
            if self.answer_points > 0:
                self.image.blit(self.font.render(u"Świetnie!", 1, WHITE), [250, 250])
            else:
                self.image.blit(self.font.render(u"Niestety to nie jest właściwa odpwiedź", 1, RED), [50, 250])
        else:
            self.finished = True

    def draw_question(self):
        for text_index in range(len(self.question_data_text)):
            if text_index == self.selected:
                self.question_with_answers_surfs[text_index] = self.font.render(self.question_data_text[text_index], 1,
                                                                                RED)
            else:
                self.question_with_answers_surfs[text_index] = self.font.render(self.question_data_text[text_index], 1, WHITE)
        i = 40

        for text_surf_index in range(len(self.question_with_answers_surfs)):
            self.image.blit(self.question_with_answers_surfs[text_surf_index], [50, i])
            i += 50

    def draw_confirmation(self):
        if self.selected > 0:
            self.image.blit(self.font.render(u"Jeśli jesteś pewny odpowiedzi naciśnij [ENTER]", 1, WHITE), [400, 380])

    def check_key(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_1]:
            self.selected = 1
        if keystate[pygame.K_2]:
            self.selected = 2
        if keystate[pygame.K_3]:
            self.selected = 3
        if self.selected > 0 and keystate[pygame.K_RETURN]:
            self.finish_answering()

    def finish_answering(self):
        self.last_update = pygame.time.get_ticks()
        if self.selected == self.question_data_answer:
            self.answer_points = 1
        else:
            self.answer_points = 0
