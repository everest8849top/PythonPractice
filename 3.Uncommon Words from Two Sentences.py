"""Finding Uncommon Words from Two Sentences
A word is considered uncommon if it occurs exactly once in one of the sentences\
    and does not appear in the other. \
    To solve this problem, you need to find all the words that appear only once in two given sentences.

Here’s an example of the input and output values of this problem:

sentence 1 = “the quick brown fox jumps over the lazy dog”,
sentence 2 = “the quick brown dog jumps over the lazy fox”
Output: [‘fox’, ‘dog’]
In the example above, the uncommon words in these two sentences are “fox” and “dog”\
    since they appear exactly once in each sentence and do not appear in the other.
"""


def uncommon_from_setences(s1, s2):
    words1 = s1.split()
    words2 = s2.split()

    counts = {}
    for word in words1 + words2:
        counts[word] = counts.get(word, 0) + 1
    uncommon = [word for word in counts if counts[word] == 1]
    return uncommon


s1 = "this apple is sweet"
s2 = "this apple is sour"

print(uncommon_from_setences(s1, s2))
