#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import codecs
import feature_extractors
import csv

# используется для работы с большими корпусами, где каждый текст разобран независимо таггером
#xml документ не включает тэгов слов и предложений

def read_text(text_lines):
    print(text_lines[0])
    s = re.search('id=\"(.+?)\"', text_lines[0])
    id = int(s.group(1))

    tuple_lines = []
    for line in text_lines[1:-1]:
        clean_line = re.sub('\</?(br|o|guessed).*?\>', '', line).strip()
        if len(clean_line) > 0:
            line_tuple = clean_line.split('\t')
            if len(line_tuple) == 3:
                line_tuple[0] = line_tuple[0].lower()
                line_tuple[2] = line_tuple[2].lower()
                line_tuple = tuple(line_tuple)
                tuple_lines.append(line_tuple)

    sents = [[]]
    for i, t in enumerate(tuple_lines):
        sents[-1].append(t)
        if t[1] == 'SENT' and i < len(tuple_lines) - 1:
            sents.append([])

    return id, sents


def process_text(id, sents, vectorwriter):
    values = []
    first_person_pronoun_results = 0
    second_person_pronoun_results = 0
    third_person_pronoun_results = 0
    reflexive_pronoun_results = 0
    adjective_pronoun_results = 0
    nom_pronoun_results = 0
    indefinite_pron_results = 0
    past_tense_results = 0
    perf_aspect_results = 0
    present_tense_results = 0
    place_adverb_results = 0
    time_adverb_results = 0
    total_adverb_results = 0
    wh_questions_results = 0
    nominalization_results = 0
    nouns_results = 0
    passive_results = 0
    by_passive_results = 0
    infin_results = 0
    speech_verb_results = 0
    mental_verb_results = 0
    that_compl_results = 0
    wh_relative_results = 0
    pied_piping_results = 0
    total_PP_results = 0
    exclamation_results = 0
    word_length_results = 0
    all_letters = 0
    all_words = 0
    sentence_length_results = 0
    all_sent_words = 0
    all_sent_marks = 0
    type_token_ratio_results = 0
    all_types = set()
    all_tokens = 0
    verbal_adverb_results = 0
    passive_participial_clauses_results = 0
    active_participial_clauses_results = 0
    imperative_mood_results = 0
    predicative_adjectives_results = 0
    attributive_adjective_results = 0
    causative_subordinate_results = 0
    concessive_subordinate_results = 0
    conditional_subordinate_results = 0
    purpose_subordinate_results = 0
    negation_results = 0
    conditional_mood_results = 0
    modal_possibility_results = 0
    modal_necessity_results = 0
    evaluative_vocabulary_results = 0
    evidentiality_results = 0
    parenthesis_attitude_evaluation_results = 0
    animate_nouns_results = 0
    parenthesis_accentuation_results = 0
    parenthesis_relation_results = 0
    phrasal_coordination_results = 0
    other_coordination_results = 0
    degree_adverb_results = 0
    particles_results = 0
    time_nouns_results = 0
    quantity_nouns_results = 0
    causative_verb_results = 0
    numeral_results = 0
    existential_verb_results = 0
    change_verb_results = 0
    movement_verb_results = 0
    phisical_prop_adjective_results = 0
    time_adjective_results = 0
    size_adjective_results = 0

    for sent in sents:
        first_person_pronoun_results += feature_extractors.first_person_pronoun(sent)
        second_person_pronoun_results += feature_extractors.second_person_pronoun(sent)
        third_person_pronoun_results += feature_extractors.third_person_pronoun(sent)
        reflexive_pronoun_results += feature_extractors.reflexive_pronoun(sent)
        adjective_pronoun_results += feature_extractors.adjective_pronoun(sent)
        nom_pronoun_results += feature_extractors.nom_pronoun(sent)
        indefinite_pron_results += feature_extractors.indefinite_pron(sent)
        past_tense_results += feature_extractors.past_tense(sent)
        perf_aspect_results += feature_extractors.perf_aspect(sent)
        present_tense_results += feature_extractors.present_tense(sent)
        place_adverb_results += feature_extractors.place_adverb(sent)
        time_adverb_results += feature_extractors.time_adverb(sent)
        total_adverb_results += feature_extractors.total_adverb(sent)
        wh_questions_results += feature_extractors.wh_questions(sent)
        (nomz, nouns) = feature_extractors.is_nominalization(sent)
        nominalization_results += nomz
        nouns_results += nouns
        (passive, by_passive) = feature_extractors.is_agentless_passive(sent)
        passive_results += passive
        by_passive_results += by_passive
        infin_results += feature_extractors.infinitives(sent)
        speech_verb_results += feature_extractors.speech_verb(sent)
        mental_verb_results += feature_extractors.mental_verb(sent)
        that_compl_results += feature_extractors.that_complement(sent)
        (wh_rel, pied_pip) = feature_extractors.wh_relatives_and_pied_piping(sent)
        wh_relative_results += wh_rel
        pied_piping_results += pied_pip
        total_PP_results += feature_extractors.total_PP(sent)
        exclamation_results += feature_extractors.is_exclamation(sent)
        (letters, words) = feature_extractors.word_length(sent)
        all_letters += letters
        all_words += words
        sent_words = feature_extractors.sentence_length(sent)
        all_sent_words += sent_words
        all_sent_marks += 1
        (types, tokens) = feature_extractors.type_token_ratio(sent)
        all_types = all_types.union(types)
        all_tokens += tokens
        verbal_adverb_results += feature_extractors.is_verbal_adverb(sent)
        passive_participial_clauses_results += feature_extractors.passive_participial_clauses(sent)
        active_participial_clauses_results += feature_extractors.active_participial_clauses(sent)
        imperative_mood_results += feature_extractors.imperative_mood(sent)
        predicative_adjectives_results += feature_extractors.predicative_adjectives(sent)
        attributive_adjective_results += feature_extractors.attributive_adjective(sent)
        causative_subordinate_results += feature_extractors.causative_subordinate(sent)
        concessive_subordinate_results += feature_extractors.concessive_subordinate(sent)
        conditional_subordinate_results += feature_extractors.conditional_subordinate(sent)
        purpose_subordinate_results += feature_extractors.purpose_subordinate(sent)
        negation_results += feature_extractors.negation(sent)
        conditional_mood_results += feature_extractors.conditional_mood(sent)
        modal_possibility_results += feature_extractors.modal_possibility(sent)
        modal_necessity_results += feature_extractors.modal_necessity(sent)
        evaluative_vocabulary_results += feature_extractors.evaluative_vocabulary(sent)
        evidentiality_results += feature_extractors.evidentiality(sent)
        parenthesis_attitude_evaluation_results += feature_extractors.parenthesis_attitude_evaluation(sent)
        animate_nouns_results += feature_extractors.animate_nouns(sent)
        parenthesis_accentuation_results += feature_extractors.parenthesis_accentuation(sent)
        parenthesis_relation_results += feature_extractors.parenthesis_relation(sent)
        (phrasal, other) = feature_extractors.coordination(sent)
        phrasal_coordination_results += phrasal
        other_coordination_results += other
        degree_adverb_results += feature_extractors.degree_adverb(sent)
        particles_results += feature_extractors.particles(sent)
        time_nouns_results += feature_extractors.time_nouns(sent)
        quantity_nouns_results += feature_extractors.quantity_nouns(sent)
        causative_verb_results += feature_extractors.causative_verb(sent)
        numeral_results += feature_extractors.numeral(sent)
        existential_verb_results += feature_extractors.existential_verb(sent)
        change_verb_results += feature_extractors.change_verb(sent)
        movement_verb_results += feature_extractors.movement_verb(sent)
        phisical_prop_adjective_results += feature_extractors.phisical_prop_adjective(sent)
        time_adjective_results += feature_extractors.time_adjective(sent)
        size_adjective_results += feature_extractors.size_adjective(sent)

    sentence_length_results = all_sent_words / all_sent_marks
    type_token_ratio_results = len(all_types) / all_tokens
    word_length_results = all_letters / all_words
    word_count = all_words
    values.append(id)
    values.append(first_person_pronoun_results / word_count)
    values.append(second_person_pronoun_results / word_count)
    values.append(third_person_pronoun_results / word_count)
    values.append(reflexive_pronoun_results / word_count)
    values.append(adjective_pronoun_results / word_count)
    values.append(nom_pronoun_results / word_count)
    values.append(indefinite_pron_results / word_count)
    values.append(past_tense_results / word_count)
    values.append(perf_aspect_results / word_count)
    values.append(present_tense_results / word_count)
    values.append(place_adverb_results / word_count)
    values.append(time_adverb_results / word_count)
    values.append(total_adverb_results / word_count)
    values.append(wh_questions_results / word_count)
    values.append(nominalization_results / word_count)
    values.append(nouns_results / word_count)
    values.append(passive_results / word_count)
    values.append(by_passive_results / word_count)
    values.append(infin_results / word_count)
    values.append(speech_verb_results / word_count)
    values.append(mental_verb_results / word_count)
    values.append(that_compl_results / word_count)
    values.append(wh_relative_results / word_count)
    values.append(pied_piping_results / word_count)
    values.append(total_PP_results / word_count)
    values.append(exclamation_results / word_count)
    values.append(word_length_results)
    values.append(sentence_length_results)
    values.append(type_token_ratio_results)
    values.append(verbal_adverb_results / word_count)
    values.append(passive_participial_clauses_results / word_count)
    values.append(active_participial_clauses_results / word_count)
    values.append(imperative_mood_results / word_count)
    values.append(predicative_adjectives_results / word_count)
    values.append(attributive_adjective_results / word_count)
    values.append(causative_subordinate_results / word_count)
    values.append(concessive_subordinate_results / word_count)
    values.append(conditional_subordinate_results / word_count)
    values.append(purpose_subordinate_results / word_count)
    values.append(negation_results / word_count)
    values.append(conditional_mood_results / word_count)
    values.append(modal_possibility_results / word_count)
    values.append(modal_necessity_results / word_count)
    values.append(evaluative_vocabulary_results / word_count)
    values.append(evidentiality_results / word_count)
    values.append(parenthesis_attitude_evaluation_results / word_count)
    values.append(animate_nouns_results / word_count)
    values.append(parenthesis_accentuation_results / word_count)
    values.append(parenthesis_relation_results / word_count)
    values.append(phrasal_coordination_results / word_count)
    values.append(other_coordination_results / word_count)
    values.append(degree_adverb_results / word_count)
    values.append(particles_results / word_count)
    values.append(time_nouns_results / word_count)
    values.append(quantity_nouns_results / word_count)
    values.append(causative_verb_results / word_count)
    values.append(numeral_results / word_count)
    values.append(existential_verb_results / word_count)
    values.append(change_verb_results / word_count)
    values.append(movement_verb_results / word_count)
    values.append(phisical_prop_adjective_results / word_count)
    values.append(time_adjective_results / word_count)
    values.append(size_adjective_results / word_count)

    vectorwriter.writerow(values)


with codecs.open("processed_corpus_3.xml", mode='r', encoding="utf-8") as f:
    with open('test.csv', 'w') as csvfile:
        vectorwriter = csv.writer(csvfile)
        vectorwriter.writerow(
            ['id', 'first_person_pronoun', 'second_person_pronoun', 'third_person_pronoun',
               'reflexive_pronoun', 'adjective_pronoun', 'nom_pronoun', 'indefinite_pron',
               'past_tense', 'perf_aspect', 'present_tense', 'place_adverb', 'time_adverb',
               'total_adverb', 'wh_questions', 'nominalization', 'nouns', 'passive', 'by_passive',
               'infin', 'speech_verb', 'mental_verb', 'that_compl', 'wh_relative', 'pied_piping',
               'total_PP', 'exclamation', 'word_length', 'type_token_ratio', 'sentence_length',
               'verbal_adverb', 'passive_participial_clauses', 'active_participial_clauses',
               'imperative_mood', 'predicative_adjectives', 'attributive_adjective',
               'causative_subordinate', 'concessive_subordinate', 'conditional_subordinate',
               'purpose_subordinate', 'negation',
               'conditional_mood', 'modal_possibility',
               'modal_necessity',
               'evaluative_vocabulary', 'evidentiality', 'parenthesis_attitude_evaluation', 'animate_nouns',
               'parenthesis_accentuation', 'parenthesis_relation', 'phrasal_coordination',
               'other_coordination', 'degree_adverb', 'particles', 'time_nouns', 'quantity_nouns',
               'causative_verb', 'numeral', 'existential_verb', 'change_verb', 'movement_verb',
               'phisical_prop_adjective', 'time_adjective', 'size_adjective'
            ])

        current_text = []
        line_stripped = None
        for line in f:
            line_stripped = line.strip()
            if len(line_stripped) > 0:
                current_text.append(line)
            if line_stripped == '</text>':
                if len(current_text) > 102:
                    id, sents = read_text(current_text)
                    #print(current_text)
                    print(id)
                    process_text(id, sents, vectorwriter)
                current_text = []

        # Если так получилось, что последний текст не закрыт
        if line_stripped != '</text>' and len(current_text) > 101:
            current_text.append('</text>')
            id, sents = read_text(current_text)
            process_text(id, sents, vectorwriter)
