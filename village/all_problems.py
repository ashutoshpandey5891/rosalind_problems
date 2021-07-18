#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:24:10 2020

@author: t1
"""
# import this

## problem 3
def problem3(sent,a,b,c,d):
    res1 = sent[a:(b+1)]
    res2 = sent[c:(d+1)]
    return '{} {}'.format(res1,res2)


# sent1 = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
# print(problem3(sent1,22,27,97,102))

# sent2 = 'ADjXKSWMs3pemQ7yAyZl5m5pfIdbKUnZDgCv8IXmLb0wLutraFul8luwCsjuQslXZ8uJzlye3m8bWTN2lQLZsMwRGq04pJ8O7sJ2ToAR5bn1wbIZsRkJzw2zVAU57pZoW9tbaAqTab2CB7edM2mFcyanochlorisdP91zWRDYz8xEdLgn6c.'
# print(problem3(sent2,44,48,148,159))


def problem4(a,b):
    sum = 0
    for i in range(a,(b+1)):
        if i % 2 != 0:
            sum += i
    return sum

# print(problem4(4208,8335))

def problem5(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        # print(lines)
        with open('output_5.txt','w') as f:
            count = 1
            for line in lines:
                if count % 2 == 0:
                    f.write(line)
                count += 1
            
# problem5('rosalind_ini5.txt')

def problem6(sent):
    word_dict = {}
    words = sent.split(' ')
    for word in words:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for word,val in word_dict.items():
        print('{} {}'.format(word,val))


sample_sent = 'We tried list and we tried dicts also we tried Zen'
sent = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
problem6(sent)