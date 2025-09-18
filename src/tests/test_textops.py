from collections import Counter

def unique_words_preserve_order(words):
    """Return a list of unique words preserving their first occurrence order."""
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


def top_k_frequent_first_tie(words, k):
    """Return top k most frequent words. In case of tie, word with earlier appearance wins."""
    if k <= 0:
        raise ValueError("k must be a positive integer")

    freq = Counter(words)
    first_occurrence = {}
    for index, word in enumerate(words):
        if word not in first_occurrence:
            first_occurrence[word] = index

    # Sort: frequency descending, then first appearance ascending
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], first_occurrence[x[0]]))
    return [word for word, _ in sorted_items[:k]]


def redact_words(words, banned_words):
    """Redact words from the list that are present in banned_words."""
    banned_set = set(banned_words)
    return ["***" if word in banned_set else word for word in words]
