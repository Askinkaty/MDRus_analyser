# -*- coding: utf-8 -*-

def process_grammar(tag_data):
    if tag_data[1] == '':
        return None
    else:
        d = {'word': tag_data[2]}
        tag = tag_data[1]
        if tag[0] == 'V':
            d['pos'] = tag[0]
            if len(tag) < 11:
                tag = tag.ljust(11, '-')
            d['type'] = tag[1]
            d['vform'] = tag[2]
            d['tense'] = tag[3]
            d['person'] = tag[4]
            d['number'] = tag[5]
            d['gender'] = tag[6]
            d['voice'] = tag[7]
            d['definiteness'] = tag[8]
            d['aspect'] = tag[9]
            d['case'] = tag[10]

        if tag[0] == 'N' or tag[0] == 'A':
            if len(tag) < 7:
                tag = tag.ljust(7, '-')
            d['type'] = tag[1]
            if tag[0] == 'N':
                d['pos'] = tag[0]
                d['gender'] = tag[2]
                d['number'] = tag[3]
                d['case'] = tag[4]
                d['animate'] = tag[5]
                d['case2'] = tag[6]
            if tag[0] == 'A':
                d['pos'] = tag[0]
                d['degree'] = tag[2]
                d['gender'] = tag[3]
                d['number'] = tag[4]
                d['case'] = tag[5]
                d['definiteness'] = tag[6]

        if tag[0] == 'P':
            if len(tag) < 8:
                tag = tag.ljust(9, '-')
            d['pos'] = tag[0]
            d['type'] = tag[1]
            d['person'] = tag[2]
            d['gender'] = tag[3]
            d['number'] = tag[4]
            d['case'] = tag[5]
            d['syntactic_type'] = tag[6]
            d['animate'] = tag[7]

        if tag[0] == 'R':
            if len(tag) < 2:
                tag = tag.ljust(2, '-')
            d['pos'] = tag[0]
            d['degree'] = tag[1]

        if tag[0] == 'S' and tag != 'SENT':
            if len(tag) < 4:
                tag = tag.ljust(4, '-')
            d['pos'] = tag[0]
            d['type'] = tag[1]
            d['formation'] = tag[2]
            d['case'] = tag[3]
        if tag[0] == 'C':
            if len(tag) < 5:
                tag = tag.ljust(5, '-')
            d['pos'] = tag[0]
            d['type'] = tag[1]
            d['formation'] = tag[2]
            d['coord-type'] = tag[3]
            d['sub-type'] = tag[4]
        if tag[0] == 'Q':
            if len(tag) < 2:
                tag = tag.ljust(2, '-')
            d['pos'] = tag[0]
            d['formation'] = tag[1]
        if tag[0] == 'M':
            if len(tag) < 7:
                tag = tag.ljust(7, '-')
            d['pos'] = tag[0]
            d['type'] = tag[1]
            d['gender'] = tag[2]
            d['number'] = tag[3]
            d['case'] = tag[4]
            d['form'] = tag[5]
            d['animate'] = tag[6]



    return d


#print(process_verb_or_nom(['этот',	'P--msna',	'этот']))