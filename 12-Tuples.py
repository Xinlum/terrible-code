fin=open('words.txt')

def min_max(t):
    return min(t), max(t)

def printall(*args):
    print(args)

def sum_all(*args):
    return sum([*args])#takes tuple and scatters it to form list for sum

#print(sum_all(1,2,3,4))#TEST

def has_match(t1, t2):#2 sequences such as a list and string
    '''returns True if there is an index i such that t1[i] == t2[i]'''
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

def histogram(s):
    '''returns dictionary counting how many
    times a character shows up, mini version'''
    d=dict()
    for c in s:
        d[c]=d.get(c,0)+1
    return d

def invert_dict(d):
    '''d[k]=v becomes d[v]=[k]'''
    invert={}
    for key in d:
        val=d[key]
        invert.setdefault(val,[]).append(key)#setdefault RETURNS value (THE LIST!) if already present
    return invert#so the above value == d[val].append

def most_frequent(s):
    '''takes a string and prints the
    letters in decreasing order of frequency'''
    d=histogram(s)
    d=invert_dict(d)
    for key,value in reversed(sorted(d.items())):
        print(key,value)

#fin=open('sample_text.txt')#random german i found

def file2string():
    '''takes fin and returns long string'''
    s=''
    for line in fin:
        string=line.strip()
        s+=string
    return s

#s=file2string()
#most_frequent(s)

######

def old_is_anagram(word1,word2):
    '''are word1 and word2 anagrams?'''
    t1=list(word1)
    t2=list(word2)
    t1.sort()
    t2.sort()
    if t1==t2:
        return True
    return False

def word_dict():
    d={}
    for line in fin:
        word=line.strip()
        d[word]=0
    return d

def string_tuple(string):
    '''takes a string and returns a sorted tuple'''
    return tuple(sorted(string))

def anagram_dict():
    '''returns anagram dict tuple key=list of words'''
    words=word_dict()
    ad={}#anagram dictionary
    for string in words:
        tu=string_tuple(string)
        ad.setdefault(tu,[]).append(string)
    return ad

def print_anagrams(ad):
    '''takes ad (anagram dict) and prints words that are anagrams'''
    for k in sorted(ad,key=lambda k:len(ad[k]),reverse=True):
        if len(ad[k])==1:
            continue
        print(ad[k])

def bingo(ad):
    '''prints 8 letter anagrams for scrabble bingo'''
    for k in sorted(ad,key=lambda k:len(ad[k]),reverse=True):
        if len(ad[k])==1:
            continue
        if not len(k)==8:
            continue
        print(ad[k])

ad=anagram_dict()
#print_anagrams(ad)
#bingo(ad)

def word_distance(word1,word2):
    '''computes number of differences in same-length words'''
    assert len(word1)==len(word2)#sanity check to make sure only zip same length
    count=0
    for c1,c2 in zip(word1,word2):
        if not c1==c2:
            count+=1
    return count

def meta(ad):
    '''prints metathesis pairs'''
    for anagrams in ad.values():#for every [list, of, anagrams]
        for word1 in anagrams:#for every word in list...
            for word2 in anagrams:#take every word in list...
                if word1<word2 and word_distance(word1,word2)==2:#see if word_distance==2, meaning only 1 letter is swapped, word1>word2 ensures each pair is only printed once
                    print(word1,word2)
                
#meta(ad)

test=word_dict()
