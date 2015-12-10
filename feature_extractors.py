# -*- coding: utf-8 -*-
from process_gram import process_grammar
import codecs
import re


first_pp = ['мы', 'я', 'наш', 'мой']
second_pp = ['ты', 'вы', 'ваш', 'твой']
third_pp = ['он', 'она', 'они', 'оно', 'их', 'ee', 'его', 'ихний', 'ихним', 'ихнем']
indef_pron = ['некто', 'некого', 'некому', 'некем', 'нечто', 'нечего', 'нечему', 'нечем', 'некоторый', 'некий', 'любой',
              'никто', 'ничто', 'никакой', 'нисколько', 'нигде', 'негде', 'некуда', 'никуда', 'неоткуда', 'ниоткуда',
              'некогда', 'никогда', 'никак', 'незачем', 'незачем']
place_adverbs = ['близко', 'ближе', 'вблизи', 'вверх', 'вверху', 'ввысь', 'вглубь', 'вдали', 'вдаль', 'везде', 'взад',
                 'влево', 'вне', 'вниз', 'внизу', 'внутри', 'внутрь', 'вовне', 'вовнутрь', 'вокруг', 'вперед',
                 'впереди', 'вправо', 'всюду', 'высоко', 'выше', 'глубоко', 'глубже', 'далеко', 'дальше', 'донизу',
                 'дома', 'здесь', 'издалека', 'издалече', 'издали', 'изнутри', 'кверху', 'книзу', 'кругом', 'левее',
                 'наверх', 'наверху', 'наискосок', 'налево', 'направо', 'напротив', 'наружно', 'наружу', 'невысоко',
                 'неглубоко', 'недалеко', 'неподалеку', 'низко', 'ниже', 'одаль', 'около', 'окрест', 'особняком',
                 'отдельно', 'откуда', 'отсюда', 'поближе', 'поверх', 'повсеместно', 'повсюду', 'повыше', 'поглубже',
                 'подальше', 'позади', 'пониже', 'понизу', 'посередке', 'посередине', 'посреди', 'посредине', 'поодаль',
                 'правее', 'рядом', 'сбоку', 'сверху', 'свыше', 'сзади', 'слева', 'снизу', 'снаружи', 'спереди',
                 'справа', 'стороной', 'супротив']
time_adverbs = ['бесконечно', 'беспрерывно', 'ввек', 'весной', 'вечно', 'вмиг', 'вначале', 'вовек', 'вовремя', 'впору',
                'впоследствии',
                'впредь', 'враз', 'временно', 'всечасно', 'вскоре', 'встарь', 'вчера', 'вчерась', 'давеча', 'давно',
                'давненько', 'денно', 'длительно', 'днесь', 'доколе', 'долго', 'дольше', 'доныне',
                'досветла', 'доселе', 'досрочно', 'дотемна', 'доутра', 'единовременно', 'ежеквартально', 'ежеминутно',
                'еженощно', 'ежесекундно', 'ежечасно', 'еще', 'заблаговременно', 'завсегда', 'завтра', 'задолго',
                'загодя', 'заранее', 'зараз', 'засим', 'затем', 'зимой', 'извечно', 'издревле', 'изначально', 'иногда',
                'исконно', 'испокон', 'исстари', 'круглосуточно', 'кряду', 'летом', 'мимолетно', 'навек', 'навеки',
                'навсегда', 'надолго', 'назавтра', 'накануне', 'наконец', 'намедни', 'наперед', 'напоследок',
                'напролет', 'насовсем', 'наутро', 'недавно', 'недолго', 'незадолго', 'незамедлительно', 'ненадолго',
                'нескоро', 'неоднократно', 'нонче', 'непрерывно', 'непродолжительно', 'нощно', 'ныне', 'нынче',
                'однажды', 'одновременно', 'осенью', 'отколе', 'отныне', 'отродясь', 'первоначально', 'позавчера',
                'позднее', 'поздно', 'поздновато', 'позже', 'подолгу', 'подряд', 'пожизненно', 'пока', 'покамест',
                'поныне', 'поначалу', 'попозже', 'пораньше', 'после', 'послезавтра',
                'поспешно', 'поскорее', 'постоянно', 'поутру', 'прежде', 'преждевременно', 'присно',
                'продолжительно', 'редко', 'реже', 'ранее', 'рано', 'рановато', 'раньше', 'редко', 'своевременно',
                'сегодня', 'скорее', 'скорей', 'скоро', 'смолоду', 'сначала', 'сперва', 'сразу', 'срочно', 'сроду',
                'теперича', 'часто', 'уже', 'ужо']
interrogative_pronoun = ['кто', 'что', 'какой', 'каков', 'чей', 'который', 'почему', 'зачем', 'где', 'куда', 'откуда',
                         'отчего']


def is_have_grammar(e):
    # try:
    return e[1] != ''
    # except KeyError as ke:
    #     print("Key error:" + str(e))
    #     raise ke


#pronouns
#1
def first_person_pronoun(t):
    fpp1 = 0
    for el in t:
        if el[2] in first_pp:
            fpp1 += 1
    print('1')
    return fpp1


#2
def second_person_pronoun(t):
    spp2 = 0
    for el in t:
        if el[2] in second_pp:
            spp2 += 1
    print('2')
    return spp2


#3
def third_person_pronoun(t):
    tpp3 = 0
    for el in t:
        if el[2] in third_pp:
            tpp3 += 1
    print('3')
    return tpp3


#4
def reflexive_pronoun(t):
    rfl_pn = 0
    for el in t:
        if el[2] in ['себя', 'свой']:
            rfl_pn += 1
    print('4')
    return rfl_pn


#5
def adjective_pronoun(t):
    adj_pron = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            flag_adj = False
            d_next_el = {}
            d_prev_el = {}
            d_el = process_grammar(el)
            if i + 1 < len(t):
                next_el = t[i + 1]
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                #test that pronoun agrees with the next word which is noun, adjective, pronoun or participle
                if el[2] in ['это', 'этот', 'тот']:
                    if is_have_grammar(next_el):
                        if (d_next_el.get('pos') == 'N' or d_next_el.get('pos') == 'A' or
                                    d_next_el.get('pos') == 'P' or
                                (d_next_el.get('pos') == 'V' and d_next_el.get('vform') == 'p')):
                            #attention that might be mistakes with nominative and accusative cases!
                            #like in construction "этот его ослабевший голос".
                            if d_next_el.get('case') == d_el.get('case'):
                                #test that the next word is not "весь",
                                # "все" which agree with current demonstrative pronoun
                                if next_el[2] not in ['весь', 'все']:
                                    flag_adj = True
                    else:
                        continue
            if i > 0:
                prev_el = t[i - 1]
                d_prev_el = process_grammar(prev_el)
                d_prev_el = d_prev_el if d_prev_el is not None else {}
                #test that pronoun agrees with the previous word which is noun, adjective, pronoun or participle
                if el[2] in ['это', 'этот', 'тот']:
                    if is_have_grammar(prev_el):
                        if (d_prev_el.get('pos') == 'N' or d_prev_el.get('pos') == 'A' or d_prev_el.get('pos') == 'P' or
                                (d_prev_el.get('pos') == 'V' and d_prev_el.get('vform') == 'p')):
                            if d_prev_el.get('case') == d_el.get('case'):
                                #test that the previous word is not "весь",
                                # все which agree with the current demonstrative pronoun
                                if prev_el[2] not in ['весь', 'все']:
                                    flag_adj = True

                    else:
                        continue
            if flag_adj:
                adj_pron += 1
                #print(el[0], next_el[0])
        else:
            continue
    print('5')
    return adj_pron


#6
def nom_pronoun(t):
    pronom = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            #test that el is demonstrative pronoun and not conjunction "то"
            if el[2] in ['это', 'этот', 'тот']:
                cond1 = True
            else:
                #test that the pronoun has some forms of pronoun "то", which are not homonyms to conjunction "то"
                if el[2] == 'то':
                    cond1 = el[0] in ['том', 'того']
                else:
                    cond1 = False
            #check part of speech
            cond2 = el[1][0] == 'P'

            if cond1 and cond2:
                flag_r = False
                flag_l = False
                eto_next_verb = False
                next_verb_neutral = False
                next_verb_infinitive = False
                instrumental_predicate_noun = False
                predicate_adverb_short_adj = False
                prev_ves = False

                d_next_el = {}
                d_next_next_el = {}
                d_prev_el = {}
                d_el = process_grammar(el)

                if i + 1 < len(t):
                    next_el = t[i + 1]
                    d_next_el = process_grammar(next_el)
                    d_next_el = d_next_el if d_next_el is not None else {}

                    #test that the next word is not noun, adjective or pronoun which agree with "этот" in case
                    if is_have_grammar(next_el):
                        if (d_next_el.get('pos') == 'N' or
                                    d_next_el.get('pos') == 'A' or
                                    d_next_el.get('pos') == 'P' or
                                (d_next_el.get('pos') == 'V' and d_next_el.get('vform') == 'p')):
                            if d_next_el['case'] == d_el['case']:
                                flag_r = True
                                #test that the current word has the form "это" and the next word is verb
                    #test that the next word is verb and it's infinitive
                    next_verb_infinitive = d_next_el.get('pos') == 'V' and d_next_el.get('vform') == 'n'

                if i + 2 < len(t):
                    next_el = t[i + 1]
                    next_next_el = t[i + 2]
                    d_next_el = process_grammar(next_el)
                    d_next_el = d_next_el if d_next_el is not None else {}
                    d_next_next_el = process_grammar(next_next_el)
                    d_next_next_el = d_next_next_el if d_next_next_el is not None else {}

                    eto_next_verb = (el[0] == 'это' and d_next_el.get('pos') == 'V')
                    #test that the next word is verb and it's gender is neutral and it's form is not participle
                    #next_verb_neutral = (d_next_el.get('pos') == 'V' and d_next_el.get('gender') == 'n' and
                    #                    d_next_el.get('vform') != 'p')
                    #test that the next_next word is not in instrumental case, not an adverb and not the short form
                    #of adjective
                    instrumental_predicate_noun = (
                        (d_next_next_el.get('pos') == 'N' or d_next_next_el.get('pos') == 'A')
                        and d_next_next_el.get('case') == 'i')
                    predicate_adverb_short_adj = (d_next_next_el.get('pos') == 'R' or (d_next_next_el.get('pos') == 'A'
                                                                                       and d_next_next_el.get(
                        'definiteness') == 's'))

                if i > 0:
                    prev_el = t[i - 1]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}

                    #test that the previous word is not noun, adjective or pronoun which agree with "этот" in case
                    if is_have_grammar(prev_el):
                        if (d_prev_el.get('pos') == 'N' or
                                    d_prev_el.get('pos') == 'A' or
                                    d_prev_el.get('pos') == 'P' or
                                (d_prev_el.get('pos') == 'V' and d_prev_el.get('vform') == 'p')):
                            if d_el['case'] == d_prev_el['case']:
                                flag_l = True
                        #test that the previous word is "весь" or "все" which agree with "этот"
                        prev_ves = (prev_el[2] in ['все', 'весь'] and d_prev_el.get('case') == d_el.get('case'))

                # test that it is a construction like Это было черной собакой not Это была черная собака.
                # The first sentence is with a proform.
                if eto_next_verb:
                    if (prev_ves or not flag_l) and not instrumental_predicate_noun and not predicate_adverb_short_adj:
                        print(el[0], next_el[0])
                        pronom += 1

                        #if ((prev_ves or not flag_l) and (next_verb_neutral or next_verb_infinitive)
                        #and not instrumental_predicate_noun and not predicate_adverb_short_adj):
                        #print(el[0], next_el[0])
                        #pronom += 1
                else:
                    if (prev_ves or not flag_l) and not flag_r:
                        #print(el[0], next_el[0])
                        pronom += 1
        else:
            continue
    print('6')
    return pronom


#7
def indefinite_pron(t):
    indefpronom = 0
    for i, el in enumerate(t):
        if re.search(r'-то|-нибудь|-либо', el[0], re.UNICODE):
            #print(el[0])
            indefpronom += 1
        if re.match('кое', el[0], re.UNICODE):
            #print(el[0])
            indefpronom += 1
        if el[2] in indef_pron:
            #print(el[0])
            indefpronom += 1
        #test for pronouns like "кто-кто, что-что, куда-куда"
        if el[0] in ['кто-кто', 'кого-кого', 'кому-кому', 'кем-кем', 'ком-ком', 'что-что', 'чего-чего', 'чему-чему',
                     'чем-чем', 'куда-куда', 'где-где']:
            #print(el[0])
            indefpronom += 1
        if i + 2 < len(t):
            next_el = t[i + 1]
            next_next_el = t[i + 2]
            #search for pronouns like "какой бы то ни было"
            if el[0] == 'бы' and next_el[0] == 'то' and next_next_el[0] == 'ни':
                #print(el[0])
                indefpronom += 1
                #test for constructions with interrogative pronouns like "нужно ли чего; если кто придет". ???
                #if el[0] in ['ли', 'если'] and next_el[2] in ['кто', 'что', 'чем']:
                #print(el[0])
                #indefpronom += 1
                #test for constructions like "что хочешь, какой угодно, как попало".
                #if el[2] in ['что', 'кто', 'куда', 'как', 'какой', 'чей'] and next_el[0] in ['хочешь', 'угодно',
                #                                                                            'получится', 'попало']:
                #print(el[0])
                #indefpronom += 1
            if el[2] in ['что', 'кто', 'куда', 'как', 'какой', 'чей'] and next_el[0] in ['угодно', 'получится',
                                                                                         'попало']:
                #print(el[0])
                indefpronom += 1

            #test for constructions like "непонятно какой, невесть кто, неизвестно кто, ?все равно кто"
            # (list is not finished).
            if ((el[0] in ['равно', 'непонятно', 'невесть'] or el[0] == "неизвестно") and
                        next_el[2] in ['что', 'чем', 'кто', 'куда', 'как', 'какой', 'чей', 'когда', 'где', 'откуда',
                                       'зачем', 'почему', 'отчего', 'сколько', 'который']):
                #print(el[0])
                indefpronom += 1
            if is_have_grammar(next_el):
                # search for pronouns like "не кто другой, ни кто иной" etc.
                if (el[0] in ['не', 'ни']) and (next_el[1][0] == 'P') and (next_next_el[2] in ['иной', 'другой']):
                    #print(el[0])
                    indefpronom += 1
                # search for pronouns like "ни о ком, не с чем, ни о каком".
                if el[0] in ['не', 'ни'] and next_el[1][0] == 'S' and next_next_el[2] in ['кто', 'что', 'какой']:
                    #print(el[0])
                    indefpronom += 1
            else:
                continue
    print('7')
    return indefpronom


#verbs
#8
def past_tense(t):
    past = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('tense') == 's':
                past += 1
                #print(el[0])
        else:
            continue
    print('8')
    return past


#9
def perf_aspect(t):
    perf = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('aspect') == 'p':
                perf += 1
                #print(el[0])
        else:
            continue
    print('9')
    return perf


#10
def present_tense(t):
    pres = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('tense') == 'p':
                pres += 1
                #print(el[0])
        else:
            continue
    print('10')
    return pres


#adverb
#11
def place_adverb(t):
    pl_adv = 0
    for i, el in enumerate(t):
        #test for words that not tagged as adverbs, but they are
        if el[0] in ['далеко-далеко', 'высоко-высоко', 'везде-везде', 'близко-близко', 'низко-низко', 'левее', 'правее',
                     'там', 'тут', 'здесь', 'везде', 'туточки', 'тудой', 'сюдой', 'туда', 'сюда', 'туда-сюда', 'всюду',
                     'повсюду', 'отовсюду', 'отсюда']:
            pl_adv += 1
            #print(el[0])
        if is_have_grammar(el):
            d_el = process_grammar(el)
            #test that word in vocabulary of place adverbs
            if d_el.get('pos') == 'R' and el[2] in place_adverbs:
                pl_adv += 1
                #print(el[0])
        else:
            continue
    print('11')
    return pl_adv


#12
def time_adverb(t):
    tm_adv = 0
    for i, el in enumerate(t):
        if el[0] in ['только-только', 'давным-давно', 'раным-рано', 'перво-наперво', 'ввек', 'вдругорядь', 'досветла',
                     'дотемна', 'невовремя', 'несвоевременно', 'пополуночи', 'пополудни', 'сейчас', 'сызмала',
                     'сыздетства', 'сызмалу', 'сызмальства', 'сызмальству', 'всечасно', 'допоздна', 'теперь']:
            tm_adv += 1
            #print(el[0])

        if is_have_grammar(el):
            d_el = process_grammar(el)
            #test that word in vocabulary of time adverbs
            if d_el.get('pos') == 'R' and el[2] in time_adverbs:
                tm_adv += 1
                #print(el[0])
            #test for word like весной, осенью, утром, ночью which tagged as nouns
            if el[0] in ['весной', 'зимой', 'осенью', 'летом', 'утром', 'днем', 'вечером', 'ночью', 'позднее',
                         'скорее', 'скорей', 'подоле', 'порой', 'потом']:
                d_next_el = {}
                d_prev_el = {}
                flag_l = False
                flag_r = False

                if i + 1 < len(t):
                    next_el = t[i + 1]
                    d_next_el = process_grammar(next_el)
                    d_next_el = d_next_el if d_next_el is not None else {}
                    #test that next is noun, pronoun or participle which agree in case with current word
                    if is_have_grammar(next_el):
                        if (d_next_el.get('pos') == 'N' or
                                    d_next_el.get('pos') == 'A' or
                                    d_next_el.get('pos') == 'P' or
                                    d_next_el.get('vform') == 'p'):
                            if d_next_el.get('case') == d_el.get('case'):
                                flag_r = True
                if i > 0:
                    prev_el = t[i - 1]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}

                    #test that previous is noun, pronoun or participle which agree in case with current word
                    if is_have_grammar(prev_el):
                        if (d_prev_el.get('pos') == 'N' or
                                    d_prev_el.get('pos') == 'A' or
                                    d_prev_el.get('pos') == 'P' or
                                    d_prev_el.get('vform') == 'p'):
                            if d_el.get('case') == d_prev_el.get('case'):
                                flag_l = True
                        #test that previous word is preposition
                        if d_prev_el.get('pos') == 'S' and d_prev_el.get('type') == 'p':
                            flag_r = True

                #test that word порой is not a form of verb рыть
                if d_el.get('pos') == 'V':
                    flag_r = True

                if not flag_l or not flag_r:
                    tm_adv += 1
                    #print(el[0])
        else:
            continue
    print('12')
    return tm_adv


#13
def total_adverb(t):
    total_adv = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'R':
                total_adv += 1
        else:
            continue
    print('13')
    return total_adv


#14
def wh_questions(t):
    wh_quest = 0
    l = len(t)
    #test that sentence is interrogative
    #try:
    #x = t[l - 1]
    #except Exception as ex:
    #print(t)
    #raise ex
    if t[l - 1][0] == '?':
        for i, el in enumerate(t):
            #test that pronoun is in the left periphery of the sentence (or it's preceded by preposition or
            # personal pronoun and preposition) and not preceded by comma.
            if i in range(3):
                if i == 0 or (i > 0 and t[i - 1][0] != ','):
                    #test that pronoun in the list of interrogative words which are not tagged as pronouns
                    if el[0] in ['чем', 'как', 'сколько', 'насколько', 'каковой', 'какового', 'каковому',
                                 'каковым', 'каковом']:
                        wh_quest += 1
                        #print(el[0])
                    if is_have_grammar(el):
                        d_el = process_grammar(el)
                        #test that pronoun in the vocabulary
                        if d_el.get('pos') == 'P' and el[2] in interrogative_pronoun:
                            wh_quest += 1
                            #print(el[0])
                else:
                    continue
    else:
        pass
    print('14')
    return wh_quest


#nouns
#15
#16
def is_nominalization(t):
    nomz = 0
    nouns = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'N':
                with codecs.open('dictionaries/final_lemmas_nominaliz_nouns.txt', mode='r', encoding='utf-8') as f:
                    read_lines = [s.strip() for s in f.readlines()]
                    if el[2].lower() in read_lines:
                        nomz += 1
                        #print(el[0])
                    else:
                        nouns += 1
                        #print(el[0])
        else:
            continue
    print('15, 16')
    return nomz, nouns


#verb
#17
#18
def is_agentless_passive(t):
    passive = 0
    by_passive = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            #test passive voice
            d_next_el = {}
            if d_el.get('pos') == 'V' and 'p' == d_el.get('voice'):
                if i + 1 < len(t):
                    next_el = t[i + 1]
                    d_next_el = process_grammar(next_el)
                    d_next_el = d_next_el if d_next_el is not None else {}
                    #test that the next word is instrumental noun
                    if is_have_grammar(next_el):
                        if (d_next_el.get('pos') == 'N' or d_next_el.get('pos') == 'P') and d_next_el.get(
                                'case') == 'i':
                            by_passive += 1
                            #print(el[0])
                        else:
                            passive += 1
                            #print(el[0])
                else:
                    passive += 1
                    #print(el[0])
        else:
            continue
    print('17, 18')
    return passive, by_passive


#19
def infinitives(t):
    infin = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            #test that the word is infinitive verb
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'n':
                infin += 1
                #print(el[0])
        else:
            continue
    print('19')
    return infin


#20
def speech_verb(t):
    sp_verb = 0
    with codecs.open(r'dictionaries\all_lemmas_verb_speech.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip() for s in f.readlines()]
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V':
                if el[2].lower() in read_lines:
                    sp_verb += 1
                    #print(el[0])
        else:
            continue
    print('20')
    return sp_verb


#21
def mental_verb(t):
    mntl_verb = 0
    with codecs.open(r'dictionaries\all_lemmas_verb_mental.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip() for s in f.readlines()]
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V':
                if el[2].lower() in read_lines:
                    mntl_verb += 1
                    #print(el[0])
        else:
            continue
    print('21')
    return mntl_verb


#22
def that_complement(t):
    that_compl = 0
    l = len(t)
    for i, el in enumerate(t):
        if is_have_grammar(el):
            if t[l - 1][0] != '?':
                d_el = process_grammar(el)
                d_next_el = {}
                if i + 1 < len(t):
                    next_el = t[i + 1]
                    d_next_el = process_grammar(next_el)
                    d_next_el = d_next_el if d_next_el is not None else {}
                    #test that current word is verb or short-form adjective and the next word is not a verb or
                    #short-form adjective because of sentences like 'Я был счастлив, что она пришла'.

                    if d_el.get('pos') == 'V' or (d_el.get('pos') == 'A' and d_el.get('definiteness') == 's'):
                        if is_have_grammar(next_el):
                            if (d_next_el.get('pos') != 'V' and
                                    (d_next_el.get('pos') != 'A' or d_next_el.get('definiteness') != 's')):
                                for j in range(4):
                                    #test that there's no pronouns like 'то, это, такой' between the current word and comma
                                    #because of sentences like 'Я не предвидел того, что вы приедете',
                                    #  which has relative meaning.
                                    #test that conjunction like 'что', 'чтобы' directly follow after comma
                                    if (i + j + 1 < len(t) and
                                                t[i + j][2] not in ['весь', 'все', 'такой', 'то', 'это', 'тот',
                                                                    'этот'] and
                                                t[i + j + 1][0] == ',' and i + j + 2 < len(t) and
                                                t[i + j + 2][2] in ['что', 'чтобы']):
                                        if i + j + 3 < len(t):
                                            #test that if the conjunction is 'чтобы', there's no infinitive verb after it
                                            #to check that it's not an infinitive clause
                                            if t[i + j + 2][2] == 'чтобы':
                                                if is_have_grammar(t[i + j + 3]):
                                                    d_is_inf_el = process_grammar(t[i + j + 3])
                                                    if d_is_inf_el.get('pos') == 'V' and d_is_inf_el.get(
                                                            'vform') == 'n':
                                                        continue
                                                    else:
                                                        that_compl += 1
                                                        #print(el[0])
                                            else:
                                                that_compl += 1
                                                #print(el[0])
                        else:
                            continue
        else:
            continue
    print('22')
    return that_compl


#23
#24
def wh_relatives_and_pied_piping(t):
    wh_relative = 0
    pied_piping = 0
    l = len(t)
    #get the list of prepositions
    with codecs.open(r'dictionaries\all_lemmas_prepositions.txt', mode='r', encoding='utf-8') as f:
        prepositions = [s.strip() for s in f.readlines()]
    #test that sentence is not interrogative
    if t[l - 1][0] != '?':
        for i, el in enumerate(t):
            #test that pronoun is in the left periphery of the sentence and preceded by comma
            if el[2] in ['какой', 'чей', 'который', 'почему', 'зачем', 'где', 'куда', 'откуда', 'отчего']:
                d_prev_el = {}
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        wh_relative += 1
                        #print(prev_el[0], el[0])
                    else:
                        #test that pronoun is preceded by preposition and comma. Pied-piping relative clause
                        if is_have_grammar(prev_el):
                            d_prev_el = process_grammar(prev_el)
                            d_prev_el = d_prev_el if d_prev_el is not None else {}
                            if prev_el[2].lower() in prepositions or d_prev_el.get('pos') == 'S':
                                if i - 2 > 0 and t[i - 2][0] == ',':
                                    pied_piping += 1
                                    #print(prev_el[0], el[0])
                            #test that there's pied-piping relative clause which is preceded by noun,
                            # preposition and comma
                            if d_prev_el.get('pos') == 'N' or d_prev_el.get('pos') == 'P':
                                d_prev_prev_el = {}
                                if i - 3 > 0:
                                    prev_prev_el = t[i - 2]
                                    if is_have_grammar(prev_prev_el):
                                        d_prev_prev_el = process_grammar(prev_prev_el)
                                        d_prev_prev_el = d_prev_prev_el if d_prev_prev_el is not None else {}
                                        if prev_prev_el[2].lower() in prepositions or d_prev_prev_el.get('pos') == 'S':
                                            if t[i - 3][0] == ',':
                                                pied_piping += 1
                                                #print(prev_el[0], el[0])
                            else:
                                continue
            #test that there's the example of relative clause structure like "Это был тот, кого я не боюсь".
            if el[2] in ['кто']:
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        if i - 2 > 0 and t[i - 2][2] in ['тот', 'то', 'все', 'весь', 'такой']:
                            wh_relative += 1
                            #print(prev_el[0], el[0])
                    else:
                        #test that pronoun is preceded by preposition and comma. Pied-piping relative clause
                        if is_have_grammar(prev_el):
                            d_prev_el = process_grammar(prev_el)
                            d_prev_el = d_prev_el if d_prev_el is not None else {}
                            if prev_el[2].lower() in prepositions or d_prev_el.get('pos') == 'S':
                                if (i - 3 > 0 and t[i - 2][0] == ',' and
                                            t[i - 3][2] in ['тот', 'то', 'все', 'весь', 'такой']):
                                    pied_piping += 1
                                    #print(prev_el[0], el[0])
                            #test that there's pied-piping relative clause which is preceded by noun,
                            # preposition and comma
                            if d_prev_el.get('pos') == 'N' or d_prev_el.get('pos') == 'P':
                                d_prev_prev_el = {}
                                if i - 4 > 0:
                                    prev_prev_el = t[i - 2]
                                    if is_have_grammar(prev_prev_el):
                                        d_prev_prev_el = process_grammar(prev_prev_el)
                                        d_prev_prev_el = d_prev_prev_el if d_prev_prev_el is not None else {}
                                        if prev_prev_el[2].lower() in prepositions or d_prev_prev_el.get('pos') == 'S':
                                            if (t[i - 3][0] == ',' and
                                                        t[i - 4][2] in ['тот', 'то', 'все', 'весь', 'такой']):
                                                pied_piping += 1
                                                #print(prev_el[0], el[0])
                            else:
                                continue
            else:
                continue
    #print('23', '24')
    print('23')
    return wh_relative, pied_piping


#25
def total_PP(t):
    prep_phrase = 0
    with codecs.open(r'dictionaries\all_lemmas_prepositions.txt', mode='r', encoding='utf-8') as f:
        prepositions = [s.strip() for s in f.readlines()]
    for i, el in enumerate(t):
        if el[2] in prepositions:
            prep_phrase += 1
            #print(el[0])
        else:
            if is_have_grammar(el):
                d_el = process_grammar(el)
                if d_el.get('pos') == 'S' and el[0] != '.':
                    prep_phrase += 1
                    #print(el[0])
            else:
                continue
    print('25')
    return prep_phrase


#26
def is_exclamation(t):
    excl = 0
    l = len(t)
    if t[l - 1][0] == '!':
        excl += 1
    print('26')
    return excl


#27
def word_length(t):
    words = 0
    letters = 0
    for el in t:
        if el[0] not in ['.', ',', '!', '?', ':', ';', '"', '-', '—', '–']:
            words += 1
            #print(el[0])
            for let in el[0]:
                letters += 1
        else:
            continue
    print('27')
    return letters, words


#28
def sentence_length(t):
    sent_words = 0
    for el in t:
        if el[0] not in ['.', ',', '!', '?', ':', ';', '"', '-', '—', '–'] and el[1] != 'SENT':
            sent_words += 1
            #print(el[0])
    #return sent_words, sent```_marks / 2
    print('28')
    return sent_words


#29
def type_token_ratio(t):
    types = set()
    tokens = 0
    for el in t:
        if el[0] not in ['.', ',', '!', '?', ':', ';', '"', '-', '—', '–', '@', '#', '"', '$', '%', '*', '+', ')', '(',
                         '[', ']', '{', '}', '&']:
            types.add(el[2])
            tokens += 1
        else:
            continue
    print('29')
    return types, tokens


#30
def is_verbal_adverb(t):
    gerund = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            #test that the word is verbal adverb
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'g':
                gerund += 1
                #print(el[0])
        else:
            continue
    print('30')
    return gerund


#31
def passive_participial_clauses(t):
    pas_part_clauses = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            flag_predicate = False
            d_el = process_grammar(el)
            #test that current word is past participle
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'p' and d_el.get('voice') == 'p':
                d_prev_el = {}
                d_prev_prev_el = {}
                if i > 0:
                    prev_el = t[i - 1]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    #test that the word is not a part of predicate like 'быть уставшим', 'становиться раздраженным'
                    if d_prev_el.get('pos') == 'V' and prev_el[2].lower() in ['быть', 'делаться', 'сделаться',
                                                                              'казаться',
                                                                              'называться', 'становиться', 'являться']:
                        flag_predicate = True
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    d_prev_prev_el = process_grammar(prev_prev_el)
                    d_prev_prev_el = d_prev_prev_el if d_prev_prev_el is not None else {}
                    #test that the word is not a part of predicate separated by adverb or patricles from the list
                    if d_prev_prev_el.get('pos') == 'V' and prev_prev_el[2].lower() in ['быть', 'делаться', 'сделаться',
                                                                                        'казаться',
                                                                                        'называться', 'становиться',
                                                                                        'являться']:
                        if d_prev_el.get('pos') == 'R' or prev_el[0].lower() in ['ли', 'бы', 'не']:
                            flag_predicate = True

                if not flag_predicate:
                    pas_part_clauses += 1
                    #print(el[0])
        else:
            continue
    print('31')
    return pas_part_clauses


#32
def active_participial_clauses(t):
    act_part_clauses = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            flag_predicate = False
            d_el = process_grammar(el)
            #test that current word is active/medial participle
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'p' and d_el.get('voice') != 'p':
                d_prev_el = {}
                d_prev_prev_el = {}
                if i > 0:
                    prev_el = t[i - 1]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    #test that the word is not a part of predicate like 'быть потрясающим'
                    if d_prev_el.get('pos') == 'V' and prev_el[2].lower() in ['быть', 'делаться', 'сделаться',
                                                                              'казаться',
                                                                              'называться', 'становиться', 'являться']:
                        flag_predicate = True
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    d_prev_prev_el = process_grammar(prev_prev_el)
                    d_prev_prev_el = d_prev_prev_el if d_prev_prev_el is not None else {}
                    #test that the word is not a part of predicate separated by adverb or patricles from the list
                    if d_prev_prev_el.get('pos') == 'V' and prev_prev_el[2].lower() in ['быть', 'делаться', 'сделаться',
                                                                                        'казаться',
                                                                                        'называться', 'становиться',
                                                                                        'являться']:
                        if d_prev_el.get('pos') == 'R' or prev_el[0].lower() in ['ли', 'бы', 'не']:
                            flag_predicate = True

                if not flag_predicate:
                    act_part_clauses += 1
                    #print(el[0])
        else:
            continue
    print('32')
    return act_part_clauses


#33
def imperative_mood(t):
    imp_mood = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            d_prev = {}
            d_next_el = {}
            #test that catch constructions like "давайте пишите" to assign only one mark of imperative mood
            #????? почему слово давай без глагола после него проходит этот тест?
            if (d_el.get('pos') == 'V' and d_el.get('vform') == 'm'):
                if el[0].lower() == 'давайте' or el[0].lower() == 'давай':
                    pass
                else:
                    imp_mood += 1
                    #print(el[0])
            #test that catch only "давай/те" without any verb after it
            if el[0].lower() == 'давайте' or el[0].lower() == 'давай':
                if i + 1 < len(t):
                    next_el = t[i + 1]
                    if is_have_grammar(next_el):
                        d_next_el = process_grammar(next_el)
                        d_next_el = d_next_el if d_next_el is not None else {}
                        if d_next_el.get('pos') != 'V':
                            imp_mood += 1
                            #print(el[0])
                        elif d_next_el.get('vform') != 'm':
                            imp_mood += 1
                            #print(el[0])
                        else:
                            continue
            if i > 0:
                prev_el = t[i - 1]
                if d_el.get('pos') == 'V' and d_el.get('vform') == 'i' and d_el.get('person') == '3':
                    if prev_el[0].lower() in ['да', 'пусть', 'пускай']:
                        imp_mood += 1
                        #print(el[0])
        else:
            continue
    print('33')
    return imp_mood


#34
def predicative_adjectives(t):
    pred_adj = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'A' and d_el.get('definiteness') == 's':
                pred_adj += 1
                #print(el[0])
            if d_el.get('pos') == 'A' and d_el.get('definiteness') == 'f':
                d_prev_el = {}
                if i > 0:
                    prev_el = t[i - 1]
                    if is_have_grammar(prev_el):
                        d_prev_el = process_grammar(prev_el)
                        d_prev_el = d_prev_el if d_prev_el is not None else {}
                        if d_prev_el.get('pos') == 'V' and prev_el[2] in ['быть', 'делаться', 'сделаться', 'казаться',
                                                                          'называться', 'становиться', 'являться']:
                            pred_adj += 1
                            #print(el[0])
            else:
                continue
        else:
            continue
    print('34')
    return pred_adj


#35
def attributive_adjective(t):
    attr_adj = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            flag_predicate = False
            if d_el.get('pos') == 'A' and d_el.get('definiteness') == 'f':
                d_prev_el = {}
                if i > 0:
                    prev_el = t[i - 1]
                    if is_have_grammar(prev_el):
                        d_prev_el = process_grammar(prev_el)
                        d_prev_el = d_prev_el if d_prev_el is not None else {}
                        if d_prev_el.get('pos') == 'V' and prev_el[2] in ['быть', 'делаться', 'сделаться', 'казаться',
                                                                          'называться', 'становиться', 'являться']:
                            flag_predicate = True
                if not flag_predicate:
                    attr_adj += 1
                    #print(el[0])
                else:
                    continue
        else:
            continue
    print('35')
    return attr_adj


#conjunctions
#36
def causative_subordinate(t):
    causative_sub = 0
    for i, el in enumerate(t):
        if el[0] in ['поскольку', 'ибо']:
            causative_sub += 1
            #print(el[0])
        else:
            if i > 0:
                prev_el = t[i - 1]
                #test that conjunction is 'так как'
                if prev_el[0] == 'так' and el[0] == 'как':
                    causative_sub += 1
                    #print(el[0])
            if i + 1 < len(t):
                next_el = t[i + 1]
                #test that conjunction is 'затем что', 'потому что', 'оттого что'
                if el[0] in ['затем', 'потому', 'оттого'] and next_el[0] == 'что':
                    causative_sub += 1
                    #print(el[0])
            if i + 2 < len(t):
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                #test that conjunction is 'затем что', 'потому что', 'оттого что' separated by comma ('потому, что')
                if el[0] in ['затем', 'потому', 'оттого'] and next_el[0] == ',' and next_next_el[0] == 'что':
                    causative_sub += 1
                    #print(el[0])
                #test that conjunction is 'ввиду того что', 'вследствие того что', 'благодаря тому что'
                if el[0] in ['ввиду', 'вследствие', 'благодаря'] and next_el[2] == 'то' and next_next_el[0] == 'что':
                    causative_sub += 1
                    #print(el[0])
            if i + 3 < len(t):
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                next_next_next_el = t[i + 3]
                #test that conjunction is 'ввиду того, что', 'вследствие того, что', 'благодаря тому, что'
                if (el[0] in ['ввиду', 'вследствие', 'благодаря'] and next_el[2] == 'то' and
                            next_next_el[0] == ',' and next_next_next_el[0] == 'что'):
                    causative_sub += 1
                    #print(el[0])
            if i + 2 < len(t) and i > 0:
                prev_el = t[i - 1]
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                #test that conjunction is 'в силу того что'
                if el[0] == 'силу' and prev_el[0] == 'в' and next_el[2] == 'то' and next_next_el[0] == 'что':
                    causative_sub += 1
                    #print(el[0])
            if i + 3 < len(t) and i > 0:
                prev_el = t[i - 1]
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                next_next_next_el = t[i + 3]
                #test that conjunction is 'в силу того, что'
                if (el[0] == 'силу' and prev_el[0] == 'в' and next_el[2] == 'то' and next_next_el[0] == ',' and
                            next_next_next_el[0] == 'что'):
                    causative_sub += 1
                    #print(el[0])
                #test that conjunction is 'в связи с тем что'
                if (el[0] == 'связи' and prev_el[0] == 'в' and next_el[0] == 'с' and next_next_el[2] == 'то' and
                            next_next_next_el[0] == 'что'):
                    causative_sub += 1
                    #print(el[0])
            if i + 4 < len(t) and i > 0:
                prev_el = t[i - 1]
                next_el = t[i + 1]
                next_next_el = t[i + 2]
                next_next_next_el = t[i + 3]
                next_next_next_next_el = t[i + 4]
                #test that conjunction is 'в связи с тем, что'
                if (el[0] == 'связи' and prev_el[0] == 'в' and next_el[0] == 'с' and next_next_el[2] == 'то' and
                            next_next_next_el[0] == ',' and next_next_next_next_el[0] == 'что'):
                    causative_sub += 1
                    #print(el[0])
            else:
                continue
    print('36')
    return causative_sub


#37
def concessive_subordinate(t):
    concessive_sub = 0
    for i, el in enumerate(t):
        d_next_el = {}
        if el[0] == 'хоть':
            concessive_sub += 1
            #print(el[0])
        if i + 1 < len(t):
            next_el = t[i + 1]
            if el[0] == 'даром' and next_el[0] == 'что':
                concessive_sub += 1
                #print(el[0])
            if el[0] in ['несмотря', 'невзирая'] and next_el[0] == 'на':
                concessive_sub += 1
                #print(el[0])
            if el[0] in ['только', 'лишь', 'добро'] and next_el[0] == 'бы':
                concessive_sub += 1
                #print(el[0])
            if is_have_grammar(next_el):
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                if el[0] in ['пусть', 'пускай'] and not (
                                d_next_el.get('pos') == 'V' and d_next_el.get('person') == '3'):
                    concessive_sub += 1
                    #print(el[0])
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if el[0] == 'хотя' and d_el.get('pos') == 'C':
                concessive_sub += 1
                #print(el[0])
        else:
            continue
    print('37')
    return concessive_sub


#38
def conditional_subordinate(t):
    conditional_sub = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if el[0] in ['если', 'ежели', 'кабы', 'коль', 'коли', 'раз'] and d_el.get('pos') == 'C':
                conditional_sub += 1
                #print(el[0])
        else:
            continue
    print('38')
    return conditional_sub


#39
def purpose_subordinate(t):
    purpose_sub = 0
    for i, el in enumerate(t):
        if el[0] == 'дабы':
            purpose_sub += 1
            #print(el[0])
        if el[0] in ['чтобы', 'чтоб']:
            if i == 0:
                purpose_sub += 1
                #print(el[0])
            else:
                flag_not_purpose = False
                if i > 0:
                    prev_el = t[i - 1]
                    if prev_el[2] in ['сомневаться', 'хотеть', 'захотеть', 'требовать', 'просить', 'желать',
                                      'ждать', 'мечтать', 'любить', 'загадать', 'захотеться', 'хотеться']:
                        flag_not_purpose = True
                if i - 1 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    if prev_el[0] == ',' and prev_prev_el[2] in ['сомневаться', 'хотеть', 'захотеть', 'требовать',
                                                                 'просить', 'желать', 'ждать', 'мечтать', 'любить',
                                                                 'загадать', 'захотеться', 'хотеться']:
                        flag_not_purpose = True
                    if (prev_el[2] in ['уверить', 'уверен', 'уверенный', 'верить', 'сказать', 'то'] and
                                prev_prev_el[0] == 'не'):
                        flag_not_purpose = True
                if i - 2 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    prev_prev_prev_el = t[i - 3]
                    if (prev_el[0] == ',' and
                                prev_prev_el[2] in ['уверенный', 'уверен', 'уверить', 'верить', 'сказать', 'то'] and
                                prev_prev_prev_el[0] == 'не'):
                        flag_not_purpose = True
                    if prev_el[2] == 'сказать' and prev_prev_el[2] == 'мочь' and prev_prev_prev_el[0] == 'не':
                        flag_not_purpose = True
                if i - 3 > 0:
                    prev_el = t[i - 1]
                    prev_prev_el = t[i - 2]
                    prev_prev_prev_el = t[i - 3]
                    prev_prev_prev_prev_el = t[i - 4]
                    if (prev_el[0] == ',' and prev_prev_el[2] == 'сказать' and prev_prev_prev_el[2] == 'мочь' and
                                prev_prev_prev_prev_el[0] == 'не'):
                        flag_not_purpose = True
                if not flag_not_purpose:
                    purpose_sub += 1
                    #print(el[0])
                else:
                    continue
    print('39')
    return purpose_sub


#40
def negation(t):
    neg = 0
    for i, el in enumerate(t):
        if el[0] == 'не':
            neg += 1
            #print(el[0])
    print('40')
    return neg


#41
def conditional_mood(t):
    cond = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'V' and d_el.get('vform') == 'c' or el[0] == 'бы':
                cond += 1
                #print(el[0])
        else:
            continue
    print('41')
    return cond


#42
def modal_possibility(t):
    mod_pos = 0
    for i, el in enumerate(t):
        if el[2] in ['мочь'] or el[0] in ['по-видимому']:
            mod_pos += 1
            #print(el[0])
        if is_have_grammar(el):
            d_next_el = {}
            d_prev_el = {}
            d_el = process_grammar(el)
            if i + 1 < len(t):
                next_el = t[i + 1]
                if ((el[0] == 'можно' and next_el[0] == 'быть') or
                        (el[0] == 'всей' and next_el[0] == 'вероятности')):
                    mod_pos += 1
                    #print(el[0])
            if d_el.get('pos') == 'R' and el[2] in ['наверное', 'наверно', 'возможно', 'видимо', 'верно', 'вероятно',
                                                    'пожалуй', 'можно']:
                mod_pos += 1
                #print(el[0])
    print('42')
    return mod_pos


#43
def modal_necessity(t):
    mod_nec = 0
    for i, el in enumerate(t):
        d_next_el = {}
        d_el = process_grammar(el)
        if el[0] == 'требуется':
            mod_nec += 1
            #print(el[0])
        if i + 1 < len(t):
            next_el = t[i + 1]
            if is_have_grammar(next_el):
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                if el[0] in ['следует', 'надлежит'] and d_next_el.get('pos') == 'V' and d_next_el.get('vform') == 'n':
                    mod_nec += 1
                    #print(el[0])
        if is_have_grammar(el):
            if d_el.get('pos') == 'R' and el[2] in ['нужно', 'необходимо', 'нельзя', 'обязательно', 'неизбежно',
                                                    'непременно']:
                mod_nec += 1
                #print(el[0])
            if el[2] in ['должный', 'обязанный'] and d_el.get('pos') == 'A' and d_el.get('definiteness') == 's':
                mod_nec += 1
                #print(el[0])
    print('43')
    return mod_nec


#44
def evaluative_vocabulary(t):
    eval = 0
    with codecs.open(r'evaluative_vocab.txt', mode='r', encoding='utf-8') as f:
        evaluative_words = [s.strip() for s in f.readlines()]
    for i, el in enumerate(t):
        if el[2] in evaluative_words:
            eval += 1
            #print(el[2])
    #print('44')
    return eval


#45
def evidentiality(t):
    evid = 0
    for i, el in enumerate(t):
        if el[0] in ['по-видимому', 'по-моему', 'по-твоему', 'по-вашему']:
            evid += 1
            #print(el[0])
        d_next_el = {}
        d_prev_el = {}
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'Q' and el[2] in ['якобы', 'будто', 'де']:
                evid += 1
                #print(el[0])
            if d_el.get('pos') == 'R' and el[2] in ['видимо', 'кажется', 'похоже', 'мол', 'дескать', 'говорят']:
                evid += 1
                #print(el[0])
        if i == 0 and el[0] == 'видно':
            if i + 1 < len(t):
                next_el = t[i + 1]
                if next_el[0] == ',':
                    evid += 1
                    #print(el[0])
        if i > 0 and i + 1 < len(t):
            if el[0] == 'видно':
                next_el = t[i + 1]
                prev_el = t[i - 1]
                if (prev_el[0] == ',' or prev_el[0] == 'как') and next_el[0] in [',', '.']:
                    evid += 1
                    #print(el[0])
        if i > 0:
            prev_el = t[i - 1]
            if el[0] in ['слухам', 'мнению', 'словам', 'сообщению', 'выражению'] and prev_el[0] == 'по':
                evid += 1
                #print(el[0])
            if ((el[0] in ['слышно', 'оказалось', 'известно'] or
                         el[2] in ['полагать', 'считать', 'писать', 'говорить']) and prev_el[0] == 'как'):
                evid += 1
                #print(el[0])
            if el[0] == 'зрения' and prev_el[0] == 'точки':
                evid += 1
                #print(el[0])
    print('45')
    return evid


#46
def parenthesis_attitude_evaluation(t):
    parent = 0
    for i, el in enumerate(t):
        flag = False
        if el[0] in ['увы', 'странно', 'удивительно', 'надеюсь', 'думаю', 'полагаю', 'пожалуй', 'думается', 'конечно',
                     'разумеется', 'бесспорно', 'действительно', 'положим', 'предположим', 'допустим', 'признаюсь']:
            if i + 1 < len(t):
                next_el = t[i + 1]
                if i == 0 and next_el[0] == ',':
                    flag = True
                if i > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        flag = True
        if el[0] in ['счастью', 'радости', 'удовольствию', 'несчастью', 'удивлению', 'сожалению', 'изумлению', 'стыду',
                     'досаде', 'неудовольствю', 'прискорбию', 'огорчению']:
            if i > 0:
                prev_el = t[i - 1]
                if prev_el[0] == 'к':
                    flag = True
            if i - 1 > 0:
                prev_prev_el = t[i - 2]
                if prev_prev_el[0] == 'к':
                    flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 1 or (i - 1 > 0 and t[i - 2][0] == ','):
                prev_el = t[i - 1]
                if (el[0] in ['хорошо', 'хуже', 'плохо', 'хуже', 'обидно'] and prev_el[0] == 'что' or
                                el[0] in ['несчастью', 'правде', 'существу', 'сути'] and prev_el[0] == 'по' or
                                el[0] == 'дело' and prev_el[0] in ['странное', 'удивительное', 'непонятное'] or
                                el[0] == 'доброго' and prev_el[0] == 'чего' or el[0] == 'полагать' and prev_el[
                    0] == 'надо' or
                                el[0] == 'сомнения' and prev_el[0] == 'без' or el[0] == 'собой' and prev_el[
                    0] == 'само' or
                                el[0] == 'образом' and prev_el[0] == 'некоторым' or el[0] == 'хотите' and prev_el[
                    0] == 'если' or
                                el[0] == 'шуток' and prev_el[0] == 'кроме' or el[0] == 'скажу' and prev_el[
                    0] == 'прямо' or
                                el[0] == 'беду' and prev_el[0] == 'на' or el[0] == 'делом' and prev_el[
                    0] == 'грешным' or
                                el[0] == 'час' and prev_el[0] in ['неровен', 'неровён'] or el[0] == 'нарочно' and
                        prev_el[0] == 'как'):
                    if next_el[0] in [',', '.']:
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 2 or (i - 2 > 0 and t[i - 3][0] == ','):
                prev_el = t[i - 1]
                prev_prev_el = t[i - 2]
                if (el[0] == 'бог' and prev_el[0] == 'дай' and prev_prev_el[0] == 'не' or
                                    el[0] == 'разумеется' and prev_el[0] == 'собой' and prev_prev_el[0] == 'само' or
                                    el[0] == 'смысле' and prev_el[0] == 'каком-то' and prev_prev_el[0] == 'в' or
                                    el[0] == 'совести' and prev_el[0] == 'по' and prev_prev_el[0] == 'говоря' or
                                    el[0] == 'чести' and prev_el[0] == 'по' and prev_prev_el[0] == 'сказать' or
                                    el[0] == 'говоря' and prev_el[0] == 'нами' and prev_prev_el[0] == 'между' or
                                    el[0] == 'сказать' and prev_el[0] == 'правду' and prev_prev_el[0] == 'если' or
                                    el[0] == 'говоря' and prev_el[0] == 'правде' and prev_prev_el[0] == 'по' or
                                    el[0] == 'говоря' and prev_el[0] == 'сущности' and prev_prev_el[0] == 'в' or
                                    el[0] == 'говорить' and prev_el[0] == 'зря' and prev_prev_el[0] == 'нечего' or
                                    el[0] in ['хорошо', 'лучше', 'плохо', 'хуже'] and prev_el[0] == 'еще' and
                                prev_prev_el[0] == 'что'):
                    if next_el[0] in [',', '.']:
                        flag = True
        if flag:
            parent += 1
            #print(el[0])
    print('46')
    return parent


#47
def animate_nouns(t):
    anim_nouns = 0
    with codecs.open('dictionaries/all_lemmas_animate_nouns.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2] in read_lines:
            anim_nouns += 1
            #print(el[0])
    print('47')
    return anim_nouns


#48
def parenthesis_accentuation(t):
    parent = 0
    for i, el in enumerate(t):
        flag = False
        if el[0] in ['повторяю', 'повторяем', 'подчеркиваю', 'подчеркиваем', 'представь', 'представьте', 'поверишь',
                     'поверите', 'вообрази', 'вообразите', 'согласись', 'согласитесь', 'заметь', 'заметьте', 'замечу',
                     'заметим', 'например', 'знаешь', 'знаете', 'значит', 'понимаешь', 'понимаете', 'главное',
                     'собственно', 'поверь', 'поверьте']:
            if i + 1 < len(t):
                next_el = t[i + 1]
                if i == 0 and next_el[0] == ',':
                    flag = True
                if i > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 1 or (i - 1 > 0 and t[i - 2][0] == ','):
                prev_el = t[i - 1]
                if (el[0] in ['важно', 'существенно'] and prev_el[0] == 'что' or
                                el[0] in ['поверишь', 'поверите'] and prev_el[0] == 'не' or
                                el[0] == 'дело' and prev_el[0] == 'главное' or
                                el[0] in ['напоминаю', 'напоминаем'] and prev_el[0] == 'как' or
                                el[0] == 'примеру' and prev_el[0] == 'к' or
                                el[0] == 'сказать' and prev_el[0] == 'так' or
                                el[0] in ['вам', 'тебе'] and prev_el[0] == 'скажу' or
                                el[0] == 'сказать' and prev_el[0] == 'надо' or
                                el[0] == 'общем' and prev_el[0] == 'в' or
                                el[0] == 'говоря' and prev_el[0] == 'собственно'):
                    if next_el[0] in [',', '.']:
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 2 or (i - 2 > 0 and t[i - 3][0] == ','):
                prev_el = t[i - 1]
                prev_prev_el = t[i - 2]
                if (el[0] in ['важнее', 'существеннее'] and prev_el[0] == 'еще' and prev_prev_el[0] == 'что' or
                                    el[0] == 'представить' and prev_el[0] == 'себе' and prev_prev_el[0] in ['можешь',
                                                                                                            'можете']):
                    if next_el[0] in [',', '.']:
                        flag = True
        if flag:
            parent += 1
            #print(el[0])
    print('48')
    return parent


#49
def parenthesis_relation(t):
    parent = 0
    for i, el in enumerate(t):
        flag = False
        if el[0] in ['вдобавок', 'притом', 'следовательно', 'напротив', 'наоборот', 'во-первых', 'во-вторых',
                     'в-третьих', 'в-четвертых', 'в-пятых', 'в-шестых', 'в-седьмых', 'в-восьмых', 'в-девятых',
                     'в-десятых']:
            if i + 1 < len(t):
                next_el = t[i + 1]
                if i == 0 and next_el[0] == ',':
                    flag = True
                if i > 0:
                    prev_el = t[i - 1]
                    if prev_el[0] == ',':
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 1 or (i - 1 > 0 and t[i - 2][0] == ','):
                prev_el = t[i - 1]
                if (el[0] == 'того' and prev_el[0] in ['кроме', 'сверх'] or
                                el[0] == 'быть' and prev_el[0] == 'стало' or
                                el[0] == 'более' and prev_el[0] == 'тем' or
                                el[0] in ['водится', 'повелось', 'всегда'] and prev_el[0] == 'как' or
                                el[0] in ['обычаю', 'обыкновению'] and prev_el[0] == 'по' or
                                el[0] in ['твоя', 'ваша'] and prev_el[0] == 'воля' or
                                el[0] == 'воля' and prev_el[0] in ['твоя', 'ваша']):
                    if next_el[0] in [',', '.']:
                        flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if i == 2 or (i - 2 > 0 and t[i - 3][0] == ','):
                prev_el = t[i - 1]
                prev_prev_el = t[i - 2]
                if (el[0] == 'же' and prev_el[0] == 'тому' and prev_prev_el[0] == 'к' or
                                    el[0] == 'всего' and prev_el[0] == 'довершение' and prev_prev_el[0] == 'в' or
                                    el[0] == 'хочешь' and prev_el[0] == 'ты' and prev_prev_el[0] == 'как'):
                    if next_el[0] in [',', '.']:
                        flag = True
        if flag:
            parent += 1
            #print(el[0])
    print('49')
    return parent


#50
#51
def coordination(t):
    phras_coord = 0
    other_coord = 0
    for i, el in enumerate(t):
        if el[0] == 'и':
            d_next_el = {}
            d_prev_el = {}
            if i + 1 < len(t) and i > 0:
                prev_el = t[i - 1]
                next_el = t[i + 1]
                if is_have_grammar(prev_el) and is_have_grammar(next_el):
                    d_prev_el = process_grammar(prev_el)
                    d_prev_el = d_prev_el if d_prev_el is not None else {}
                    d_next_el = process_grammar(next_el)
                    d_next_el = d_next_el if d_next_el is not None else {}
                    if d_prev_el.get('pos') == d_next_el.get('pos'):
                        phras_coord += 1
                    elif prev_el[0] == ',':
                        other_coord += 1

    print('50, 51')
    return phras_coord, other_coord


#52
def degree_adverb(t):
    degree = 0
    for i, el in enumerate(t):
        if el[0] in ['чересчур', 'втрое', 'вчетверо', 'впятеро', 'вшестеро', 'всемеро', 'вдесятеро', 'чуть-чуть',
                     'невыразимо', 'несказанно', 'беспредельно', 'безмерно', 'невыносимо', 'феноменально',
                     'сверхъестественно', 'едва-едва']:
            degree += 1
            #if i - 3 > 0 and i + 3 < len(t):
                #print(t[i-3][0], t[i-2][0], t[i-1][0], '*', el[0], '*', t[i+1][0], t[i+2][0], t[i+3][0])
            #if i - 2 > 0 and i + 2 < len(t):
                #print(t[i-2][0], t[i-1][0], '*', el[0], '*', t[i+1][0], t[i+2][0])
            #print(el[0])
        if i + 1 < len(t):
            next_el = t[i + 1]
            if is_have_grammar(next_el):
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                if el[0] == 'несколько' and d_next_el.get('pos') == 'A':
                    degree += 1
                    #if i - 3 > 0 and i + 3 < len(t):
                        #print(t[i-3][0], t[i-2][0], t[i-1][0], '*', el[0], '*', t[i+1][0], t[i+2][0], t[i+3][0])
                    #if i - 2 > 0 and i + 2 < len(t):
                        #print(t[i-2][0], t[i-1][0], '*', el[0], '*', t[i+1][0], t[i+2][0])
                    #print(el[0])
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'R' and el[0] in ['крайне', 'очень', 'страшно', 'удивительно', 'исключительно',
                                                    'слишком', 'гораздо', 'абсолютно', 'совершенно', 'необычно',
                                                    'весьма', 'совсем', 'настолько', 'вдвое', 'еле', 'еле-еле',
                                                    'немного', 'необыкновенно', 'необычайно', 'фантастически',
                                                    'чрезвычайно', 'бешено', 'чудовищно', 'неслыханно', 'божественно',
                                                    'бесконечно', 'безумно', 'смертельно', 'ослепительно', 'нестерпимо',
                                                    'блестяще', 'гениально', 'сравнительно', 'относительно',
                                                    'невероятно', 'едва', 'капельку']:
                degree += 1
                #if i - 3 > 0 and i + 3 < len(t):
                    #print(t[i-3][0], t[i-2][0], t[i-1][0], '*', el[0], '*', t[i+1][0], t[i+2][0], t[i+3][0])
                #if i - 2 > 0 and i + 2 < len(t):
                    #print(t[i-2][0], t[i-1][0], '*', el[0], '*', t[i+1][0], t[i+2][0])
                #print(el[0])
    print('52')
    return degree


#53
def particles(t):
    particle = 0
    for i, el in enumerate(t):
        flag = False
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'Q' and el[0] in ['же', 'ну', 'прямо', 'уж', 'вот', 'там', 'разве', 'ли', 'вроде',
                                                    'ж', 'дай', 'только', 'ведь', 'даже', 'лишь']:
                flag = True
        if el[0] in ['таки', 'ка', 'то-то']:
            flag = True
        if i + 1 < len(t):
            next_el = t[i + 1]
            if is_have_grammar(next_el):
                d_next_el = process_grammar(next_el)
                d_next_el = d_next_el if d_next_el is not None else {}
                if ((el[0] == 'так' and next_el[0] == 'и') or
                (el[2] in ['какой', 'куда', 'где'] and next_el[0] == 'там' and d_next_el.get('pos') == 'Q') or
                (el[0] == 'как' and next_el[0] == 'есть')or
                (el[0] == 'знай' and next_el[0] == 'себе') or
                (el[0] == 'едва' and next_el[0] == 'не')or
                (el[0] == 'как' and next_el[0] == 'раз') or
                (el[0] == 'чуть' and next_el[0] == 'не')or
                (el[0] == 'нет-нет' and next_el[0] == 'и')):
                    flag = True
        if i + 2 < len(t):
            next_el = t[i + 1]
            next_next_el = t[i + 2]
            if ((el[0] == 'не' and next_el[0] == 'то' and next_next_el[0] in ['чтоб', 'чтобы']) or
                    (el[0] == 'не' and next_el[0] == 'иначе' and next_next_el[0] == 'как') or
                    (el[0] == 'чуть' and next_el[0] == 'было' and next_next_el[0] == 'не') or
                    (el[0] == 'того' and next_el[0] == 'и' and next_next_el[0] == 'гляди') or
                    (el[0] == 'нет-нет' and next_el[0] == 'да' and next_next_el[0] == 'и') or
                    (el[0] == 'ни' and next_el[0] == 'на' and next_next_el[0] == 'есть')):
                flag = True
        if flag:
            particle += 1
            #print(el[0])
    print('53')
    return particle


#54
def time_nouns(t):
    time_nouns = 0
    with codecs.open('dictionaries/all_lemmas_time_nouns.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2].lower() in read_lines:
            time_nouns += 1
            #print(el[0])
    print('54')
    return time_nouns


#55
def quantity_nouns(t):
    quant_nouns = 0
    with codecs.open('dictionaries/all_lemmas_quantity_nouns.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2].lower() in read_lines:
            quant_nouns += 1
            #print(el[0])
    print('55')
    return quant_nouns


#56
def causative_verb(t):
    causative = 0
    with codecs.open('dictionaries/all_lemmas_causative_verbs.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2].lower() in read_lines:
            causative += 1
            #print(el[0])
    print('56')
    return causative


#57
def numeral(t):
    num = 0
    for i, el in enumerate(t):
        if is_have_grammar(el):
            d_el = process_grammar(el)
            if d_el.get('pos') == 'M':
                num += 1
                #print(el[0])
    print('57')
    return num


#58
def existential_verb(t):
    verbs = 0
    with codecs.open('dictionaries/all_lemmas_existential_verb.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2].lower() in read_lines:
            verbs += 1
            #print(el[0])
    print('58')
    return verbs


#59
def change_verb(t):
    verbs = 0
    with codecs.open('dictionaries/all_lemmas_change_verb.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2] in read_lines:
            verbs += 1
            #print(el[0])
    print('59')
    return verbs


#60
def movement_verb(t):
    verbs = 0
    with codecs.open('dictionaries/all_lemmas_movement_verb.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2].lower() in read_lines:
            verbs += 1
            #print(el[0])
    print('60')
    return verbs


#61
def phisical_prop_adjective(t):
    adj = 0
    with codecs.open('dictionaries/all_lemmas_phisical_prop_adjective.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2].lower() in read_lines:
            adj += 1
            #print(el[0])
    print('61')
    return adj


#62
def time_adjective(t):
    time_adj = 0
    with codecs.open('dictionaries/all_lemmas_time_adjective.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2].lower() in read_lines:
            time_adj += 1
            #print(el[0])
    print('62')
    return time_adj


#63
def size_adjective(t):
    size_adj = 0
    with codecs.open('dictionaries/all_lemmas_size_adjective.txt', mode='r', encoding='utf-8') as f:
        read_lines = [s.strip().lower() for s in f.readlines()]
    for i, el in enumerate(t):
        #некоторые слова неправильно разбираются теггером и не получют лемму, поэтому не могут быть найдены в словаре
        if el[2] in read_lines:
            size_adj += 1
            #print(el[0])
    print('63')
    return size_adj
