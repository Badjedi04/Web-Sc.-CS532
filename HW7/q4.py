import numpy as np

def sim_distance(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    if not si:
        return 0
    sum_of_squares = sum([pow(prefs[p1][item] - prefs[p2][item], 2) for item in si])
    return 1 / (1 + np.sqrt(sum_of_squares))

def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    if not si:
        return 0
    n = len(si)
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    sum1_sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2_sq = sum([pow(prefs[p2][it], 2) for it in si])
    p_sum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    num = p_sum - (sum1 * sum2 / n)
    den = np.sqrt((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r

def top_matches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort(reverse=True)
    return scores[:n]

def least_matches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    return scores[:n]

def transform_prefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            result[item][person] = prefs[person][item]
    return result

def load_movie_lens():
    movies = {}
    with open('u.item.txt', encoding='ISO-8859-1') as f:
        for line in f:
            (id, title) = line.split('|')[0:2]
            movies[id] = title
    prefs = {}
    with open('u.data.txt', encoding='ISO-8859-1') as f:
        for line in f:
            (user, movieid, rating, ts) = line.split('\t')
            prefs.setdefault(user, {})
            prefs[user][movies[movieid]] = float(rating)
    return prefs

prefs = load_movie_lens()
mod_prefs = transform_prefs(prefs)

list_movies = top_matches(mod_prefs, 'Silence of the Lambs, The (1991)', n=5)
print(list_movies)

list_movies = least_matches(mod_prefs, 'Silence of the Lambs, The (1991)', n=5)
print(list_movies)

list_movies = top_matches(mod_prefs, 'Pulp Fiction (1994)', n=5)
print(list_movies)

list_movies = least_matches(mod_prefs, 'Pulp Fiction (1994)', n=5)
print(list_movies)
