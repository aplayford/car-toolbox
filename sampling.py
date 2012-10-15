import random
import csv

def sample_to_csv(filename, min_i, max_i, size=None):
    if(size is None):
        size = max_i-min_i+1

    random.seed()
    sample = zip(xrange(1, size+1), random.sample(xrange(min_i, max_i+1), size))

    with open(filename, 'w') as f:
        writer = csv.writer(f)

        writer.writerow(['Rank', 'SampleID'])

        for r in sample:
            writer.writerow(r)
