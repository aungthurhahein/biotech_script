#! /usr/bin/env/ python

"""
#
# usage: text clustering to group similar text into cluster groups
# majorclust algorithm based on k-means unsupervised clusterting
# output:
# Dev: __author__ = 'aung'
# Date: 20150914
"""
import sys
import re
from math import log, sqrt
from itertools import combinations
from collections import OrderedDict


def cosine_distance(a, b):
    cos = 0.0
    a_tfidf = a["tfidf"]
    for token, tfidf in b["tfidf"].iteritems():
        if token in a_tfidf:
            cos += tfidf * a_tfidf[token]
    return cos


def normalize(features):
    if sqrt(sum(i**2 for i in features.itervalues())) != 0.0:  # quick fix of float zero division error
        norm = 1.0 / sqrt(sum(i**2 for i in features.itervalues()))
    else:
        norm = 0.0
    for k, v in features.iteritems():
        features[k] = v * norm
    return features


def add_tfidf_to(documents):
    tokens = {}
    for id, doc in enumerate(documents):
        tf = {}
        doc["tfidf"] = {}
        doc_tokens = doc.get("tokens", [])
        for token in doc_tokens:
            tf[token] = tf.get(token, 0) + 1
        num_tokens = len(doc_tokens)
        if num_tokens > 0:
            for token, freq in tf.iteritems():
                tokens.setdefault(token, []).append((id, float(freq) / num_tokens))

    doc_count = float(len(documents))
    for token, docs in tokens.iteritems():
        idf = log(doc_count / len(docs))
        for id, tf in docs:
            tfidf = tf * idf
            if tfidf > 0:
                documents[id]["tfidf"][token] = tfidf

    for doc in documents:
        doc["tfidf"] = normalize(doc["tfidf"])

def choose_cluster(node, cluster_lookup, edges):
    new = cluster_lookup[node]
    if node in edges:
        seen, num_seen = {}, {}
        for target, weight in edges.get(node, []):
            seen[cluster_lookup[target]] = seen.get(
                cluster_lookup[target], 0.0) + weight
        for k, v in seen.iteritems():
            num_seen.setdefault(v, []).append(k)
        new = num_seen[max(num_seen)][0]
    return new

def majorclust(graph):
    cluster_lookup = dict((node, i) for i, node in enumerate(graph.nodes))

    count = 0
    movements = set()
    finished = False
    while not finished:
        finished = True
        for node in graph.nodes:
            new = choose_cluster(node, cluster_lookup, graph.edges)
            move = (node, cluster_lookup[node], new)
            if new != cluster_lookup[node] and move not in movements:
                movements.add(move)
                cluster_lookup[node] = new
                finished = False

    clusters = {}
    for k, v in cluster_lookup.iteritems():
        clusters.setdefault(v, []).append(k)
    return clusters.values()

def get_distance_graph(documents):
    class Graph(object):
        def __init__(self):
            self.edges = {}

        def add_edge(self, n1, n2, w):
            self.edges.setdefault(n1, []).append((n2, w))
            self.edges.setdefault(n2, []).append((n1, w))

    graph = Graph()
    doc_ids = range(len(documents))
    graph.nodes = set(doc_ids)
    for a, b in combinations(doc_ids, 2):
        graph.add_edge(a, b, cosine_distance(documents[a], documents[b]))
    return graph

def get_documents(textlist):
    texts = [ t.strip() for t in textlist.split("\n") if t and t.strip() ]
    return [{"text": text, "tokens": text.split()}
             for i, text in enumerate(texts)]

def list_string(listObj):
    tmplist= ""
    for x in listObj:
        line_split = x.split(',')
        for m in line_split:
            if tmplist == "":
                tmplist = m.lower() + " "
            else:
                tmplist += m.lower() + " "
    return tmplist

def main(args):
    descfile = sys.argv[1]

    with open(descfile, 'rb') as f1:
        for x in f1:
            tmplist = ""
            line_split = x.split('\t')
            # l_split = re.split(';', line_split[3].strip('\n').strip())
            # l_split = line_split[3].strip('\n').strip().split(';')
            # if len(l_split) == 1:
            l_split = line_split[1].strip('\n').strip().split('|')
            uniqlsplit = list(set(l_split))
            tmpuniqlit = []
            for mem in uniqlsplit:
                if mem.strip() not in tmpuniqlit:
                    tmpuniqlit.append(mem.strip())
            for m in tmpuniqlit:
                if tmplist == "":
                    tmplist = m.strip('\n')+"\n"
                else:
                    tmplist += m.strip('\n')+"\n"

            if len(tmplist.strip('\n').split('\n')) == 1:
                sys.stdout.write(x.strip('\n')+"\t"+line_split[3])
            else:
                documents = get_documents(tmplist.strip('\n'))      # input as list
                add_tfidf_to(documents)
                dist_graph = get_distance_graph(documents)
                final_string = ""
                # print result
                for cluster in majorclust(dist_graph):
                    tmp_result = []
                    print "="*20
                    for doc_id in cluster:
                        print documents[doc_id]["text"]
                        tmp_result.append(documents[doc_id]["text"])
                    uniqlist = sorted(list(set(tmp_result)))
                    
                #     # playing with the clusters
                #     words = list_string(uniqlist)
                #     d2 = OrderedDict()

                #     for word in words.split():
                #         if word.strip('|').strip(';') not in d2:
                #             d2[word.strip('|').strip(';')] = 1
                #         else:
                #             d2[word.strip('|').strip(';')] += 1

                #     # print d2
                #     if len(uniqlist) > 1:
                #         tmpstring = ""
                #         for k, v in d2.iteritems():
                #             if v > 1:
                #                 # tmpstring += k+' '
                #                 if tmpstring == "":
                #                     if "{" in k:
                #                         tmpstring = k.split('{')[0]
                #                     elif "}" in k:
                #                         tmpstring = k.split('}')[1]
                #                     else:
                #                         tmpstring = k
                #                 else:
                #                     if "{" in k:
                #                         tmpstring += " " + k.split('{')[0]
                #                     elif "}" in k:
                #                         tmpstring += " " + k.split('}')[1]
                #                     else:
                #                         tmpstring += " " + k
                #         if tmpstring == "":
                #             for mem in uniqlist:
                #                 if tmpstring == "" and mem != "NoDesc":
                #                     if "{" in mem:
                #                         tmpstring = mem.split('{')[0]
                #                     elif "}" in mem:
                #                         tmpstring = mem.split('}')[1]
                #                     else:
                #                         tmpstring = mem
                #                 elif mem != "NoDesc":
                #                     if "{" in mem:
                #                         tmpstring += ";"+mem.split('{')[0]
                #                     elif "}" in mem:
                #                         tmpstring += ";"+mem.split('}')[1]
                #                     else:
                #                         tmpstring += ";"+mem
                #         if final_string == "":
                #             final_string = tmpstring
                #         else:
                #             final_string = ";"+tmpstring
                #         # sys.stdout.write(x.strip('\n') + "\t" + tmpstring + '\n')
                #     else:
                #         if final_string == "":
                #             final_string = ''.join(uniqlist)
                #         else:
                #             final_string = ";" + ''.join(uniqlist)
                # # print final_string
                # sys.stdout.write(x.strip('\n') + "\t" + final_string + '\n')

if __name__ == '__main__':
    main(sys.argv)

