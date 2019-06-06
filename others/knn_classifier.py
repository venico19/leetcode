import heapq

def knnClassifier(training_features, training_labels, test_features, k):
    """
    :type training_features: List[List[Float]]
    :type training_labels: List[int]
    :type k: int
    :rtype test_labels: List[int]
    """
    n, m = len(training_features), len(test_features)
    assert(k <= n)
    
    test_labels = [0 for _ in range(m)]

    for i in range(m):
        sample = test_features[i]
        heap = []
        counter = {}
        for j in range(n):
            distance = getDistance(sample, training_features[j])
            label = training_labels[j]
            heapq.heappush(heap, (-distance, label))
            counter[label] = counter.get(label, 0) + 1
            if len(heap) > k:
                _, pop_label = heapq.heappop(heap)
                counter[pop_label] -= 1
        test_labels[i] = majorityVote(counter)

    return test_labels

def majorityVote(counter):
    max_count = 0
    res = None
    for key, value in counter.items():
        if value > max_count:
            res = key
    return res

def getDistance(A, B):
    d = len(A)
    res = 0.0
    for i in range(d):
        res += (A[i]- B[i]) ** 2
    return res ** 0.5

if __name__ == "__main__":
    training_features = [[1, 2], [2, 3], [1, 3], [9, 10], [10, 9], [11, 9]]
    training_labels = [1, 1, 1, 2, 2, 2]
    test_features = [[0, 0], [12, 12], [-1, -1]]
    test_labels = knnClassifier(training_features, training_labels, test_features, 3)
    print(test_labels)
