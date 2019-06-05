import random
def kMean(samples, k, max_iteration, tolerance):
    """
    :type samples: List[List[float]]
    :type k: int
    :type max_teration: int
    :type tolerance: float
    :rtype: centroids: List[List[float]], clusters: List[List[List[float]]]
    """
    if not samples or not samples[0]:
        raise Exception("Invalid data")
    n = len(samples)
    if k <= 0 or k > n:
        raise Exception("Invalid k")

    # initialize centroids
    random_index = random.sample(range(n), k)
    centroids = [samples[i] for i in random_index]

    for _ in range(max_iteration):
        clusters = [[] for _ in range(k)]
        
        # assign cluster label for each sample
        for sample in samples:
            cluster_label = None
            min_distance = float("Inf")

            for i in range(k):
                distance = getDistance(sample, centroids[i])
                if distance < min_distance:
                    min_distance = distance
                    cluster_label = i

            clusters[cluster_label].append(sample)
        # update centroids
        moves = 0.0
        for i in range(k):
            updated_centroid = getCentroid(clusters[i])
            moves += getDistance(centroids[i], updated_centroid)
            centroids[i] = updated_centroid
        if moves < tolerance:
            break

    return centroids, clusters


def getDistance(A, B):
    res = 0
    for i, a in enumerate(A):
        b = B[i]
        res += (a - b) ** 2
    return res ** 0.5

def getCentroid(l):
    if not l or not l[0]:
        raise Exception("Empty cluster")

    n, d = len(l), len(l[0])

    res = [0 for _ in range(d)]
    for i in range(d):
        s = 0.0
        for j in range(n):
            s += l[j][i]
        res[i] = s/n

    return res

if __name__ == "__main__":
    datasets = [[1,2], [1,2], [2,3], [50, 51], [0, 0], [-1, -10], [-7, 100]]
    centroids, clusters = kMean(datasets, 3, 20, 0.01)
    print(centroids)
    print(clusters)
