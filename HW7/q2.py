import numpy as np
import math

def sim_distance(prefs: dict[str, dict[str, float]], person1: str, person2: str) -> float:
    '''
    Returns a distance-based similarity score for person1 and person2.
    '''
    shared_items = {item for item in prefs[person1] if item in prefs[person2]}
    if len(shared_items) == 0:
        return 0
    sum_of_squares = sum((prefs[person1][item] - prefs[person2][item]) ** 2 for item in shared_items)
    return 1 / (1 + math.sqrt(sum_of_squares))

def sim_pearson(prefs: dict[str, dict[str, float]], person1: str, person2: str) -> float:
    '''
    Returns the Pearson correlation coefficient for person1 and person2.
    '''
    shared_items = {item for item in prefs[person1] if item in prefs[person2]}
    if len(shared_items) == 0:
        return 0
    n = len(shared_items)
    sum1 = sum(prefs[person1][item] for item in shared_items)
    sum2 = sum(prefs[person2][item] for item in shared_items)
    sum1_sq = sum(prefs[person1][item] ** 2 for item in shared_items)
    sum2_sq = sum(prefs[person2][item] ** 2 for item in shared_items)
    p_sum = sum(prefs[person1][item] * prefs[person2][item] for item in shared_items)
    num = p_sum - (sum1 * sum2) / n
    den = math.sqrt((sum1_sq - (sum1 ** 2) / n) * (sum2_sq - (sum2 ** 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r

def top_matches(
    prefs: dict[str, dict[str, float]],
    person: str,
    n: int = 5,
    similarity: callable = sim_pearson,
) -> list[tuple[float, str]]:
    '''
    Returns the top matches for person from the prefs dictionary. 
    Number of results and similarity function are optional params.
    '''
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort(reverse=True)
    return scores[:n]

def least_matches(
    prefs: dict[str, dict[str, float]],
    person: str,
    n: int = 5,
    similarity: callable = sim_pearson,
) -> list[tuple[float, str]]:
    '''
    Returns the least matches for person from the prefs dictionary. 
    Number of results and similarity function are optional params.
    '''
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    return scores[:n]


def load_movie_lens():
    # Get movie titles
    with open('u.item.txt', encoding='utf-8') as f:
        movies = {}
        for line in f:
            id, title = line.split('|')[:2]
            movies[id] = title

    # Load data
    with open('u.data.txt', encoding='utf-8') as f:
        prefs = {}
        for line in f:
            user, movie_id, rating, _ = line.split('\t')
            prefs.setdefault(user, {})
            prefs[user][movies[movie_id]] = float(rating)

    return prefs


prefs = load_movie_lens()

list_user = top_matches(prefs, '774', n=5)
print(list_user)

list_user = top_matches(prefs, '774', n=5, similarity=sim_distance)
print(list_user)

list_user = least_matches(prefs, '774', n=5)
print(list_user)

list_user = least_matches(prefs, '774', n=5, similarity=sim_distance)
print(list_user)
