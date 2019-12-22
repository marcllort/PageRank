#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*-

import argparse
import sys
import re
from scipy.sparse import coo_matrix
import numpy
import time


def pagerank(graph, beta=0.85, epsilon=1.0e-8):
    # Fill the initializations
    inlink_map = []

    for j in xrange(graph.shape[0]):
        print >> sys.stderr, "Making in-link map of %d\r" % (j),
        inlink_map.append(graph.getcol(j).nonzero()[0])

    out_degree = numpy.array(graph.sum(axis=1))

    print >> sys.stderr, "\nLink-map done!"
    ranks = numpy.ones(graph.shape[0]) / graph.shape[0]

    new_ranks = {}
    delta = 1.0
    n_iterations = 0

    while delta > epsilon:
        new_ranks = numpy.zeros(graph.shape[0])
        t = 0

        for links in inlink_map:
            for link in links:
                new_ranks[t] += ranks[link] / out_degree[link]
            new_ranks[t] = new_ranks[t] * beta
            t += 1

        s = sum(new_ranks)
        t = 0

        for links in inlink_map:
            new_ranks[t] = new_ranks[t] + ((1 - s) / graph.shape[0])
            t += 1

        delta = numpy.sqrt(numpy.sum(numpy.power(ranks - new_ranks, 2)))
        ranks, new_ranks = new_ranks, ranks
        print >> sys.stderr, "\nIteration %d has been computed with an delta of %e (epsilon=%e)" % (
            n_iterations, delta, epsilon)
        n_iterations += 1


    print
    rranks = {}
    for i in xrange(ranks.shape[0]):
        rranks[i] = ranks[i]
    return rranks, n_iterations


def processInput(filename):
    webs = {}
    rows = numpy.array([], dtype='int8')
    cols = numpy.array([], dtype='int8')
    data = numpy.array([], dtype='float32')
    for line in open(filename, 'r'):
        line = line.rstrip()

        m = re.match(r'^n\s([0-9]+)\s(.*)', line)
        if m:
            webs[int(m.groups()[0])] = m.groups()[1]
            continue
        m = re.match(r'^e\s([0-9]+)\s([0-9]+)', line)
        if m:
            rows = numpy.append(rows, int(m.groups()[0]))
            cols = numpy.append(cols, int(m.groups()[1]))
            data = numpy.append(data, 1)

    graph = coo_matrix((data, (rows, cols)), dtype='float32',
                       shape=(max(webs.keys()) + 1, max(webs.keys()) + 1))
    return (webs, graph)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze web data and output PageRank")
    parser.add_argument("file", type=str, help="file to be processed")
    parser.add_argument("--beta", type=float,
                        help="β value to be considered", default=0.8)
    args = parser.parse_args()

    webs, graph = processInput(args.file)
    start = time.time()
    ranks, n_iterations = pagerank(graph, args.beta)
    end = time.time()
    print >> sys.stderr, "It took %f seconds to converge" % (end - start)
    keys = map(lambda x: ranks.keys()[x],
               numpy.argsort(ranks.values())[-1::-1])
    values = map(lambda x: ranks.values()[
        x], numpy.argsort(ranks.values())[-1::-1])
    for p, (k, v) in enumerate(zip(keys, values)):
        print "[%d] %s:\t%e" % (p, webs[k], v)
