def bucketsort(arr):

    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(num * bucket_count)
        buckets[index].append(num)

    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])

    return [num for bucket in buckets for num in bucket]

arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucketsort(arr))