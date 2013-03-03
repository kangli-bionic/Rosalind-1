from string import maketrans
import functools
from itertools import chain

from decorator import decorator
from parsers import grouper
from numpy import *


def descendants(map, pop, gen):
    ''' Returns the descendants of a population given a dict
    matching the mendellian to results of that type.
    gen is the number of generations to iterate over.

    >>> from maps import mendel_hybrid_mating as m
    >>> descendants(m, 'h', 0)
    'h'
    >>> descendants(m, 'h', 1)
    'dhhr'
    >>> descendants(m, 'h', 2)
    'ddhhdhhrdhhrhhrr'
    >>> descendants(m, 'h', 3)
    'ddhhddhhdhhrdhhrddhhdhhrdhhrhhrrddhhdhhrdhhrhhrrdhhrdhhrhhrrhhrr'
    '''
    if gen == 0:
        return pop
    else:
        newpop = ''.join([map[p] for p in pop])
        return descendants(map, newpop, gen-1)


def suffix_array(s):
    ''' Generates a suffix array in linear time. '''
    for i in xrange(len(s)):
        yield s[i:], i


# Longest Common Substring functions
def common_substrings(sx, sy, _min):
    ''' Wrapper function for common substrings. '''
    M = sorted(list(_common_substrings(sx, sy, _min)), key=len)

    while True:
        try:
            compare = M.pop()
        except IndexError:
            raise StopIteration
        removelist = []
        for i in xrange(len(M)):
            if M[i] in compare:
                removelist.append(i)
        M = [M[i] for i in xrange(len(M)) if i not in removelist]
        yield compare


def _common_substrings(sx, sy, _min):
    '''Generator of all common substrings.

    Yields all common substrings of two strings, sx and sy
    longer than length _min.

    May be too slow to use, needs to be optimized. '''
    M = zeros((len(sx)+1, len(sy)+1), dtype=int16)

    # create main array
    for x in xrange(len(sx)):
        for y in xrange(len(sy)):
            if sx[x] == sy[y]:
                M[x+1][y+1] = M[x][y] + 1
                M[x][y] = 0

    flat = M.max(axis=0)
    for i in xrange(len(flat)):
        if flat[i] >= _min:
            start, length = i-flat[i], flat[i]
            yield sy[start:start+length]


def longest_common_substring(collection):
    _collection = iter(collection)
    common = ' '.join(list(common_substrings(_collection.next(),
                                             _collection.next(), 6)))

    while True:
        try:
            common = ' '.join(list(common_substrings(common,
                                                     _collection.next(), 6)))
        except StopIteration:
            return common


# SuffixTrie functions
class SuffixNode:
    ''' A SuffixNode, for use in build_suffix_trie '''
    def __init__(self, suffix_link=None):
        self.children = {}
        if suffix_link is not None:
            self.suffix_link = suffix_link
        else:
            self.suffix_link = self

    def add_link(self, c, node):
        ''' Link to node via string c '''
        self.children[c] = node


def build_suffix_trie(s):
    ''' A native python suffix trie.

    This implementation is not particularly space efficient,
    as each letter requires an instance of SuffixNode to express. '''
    assert len(s) > 0

    # explicitly build the two-node suffix tree
    root = SuffixNode()      # the root node
    longest = SuffixNode(suffix_link=root)
    root.add_link(s[0], longest)

    # for every character left in the string
    for c in s[1:]:
        current, previous = longest, None
        while c not in current.children:

            # create new_node with transition Current -c->r1
            new_node = SuffixNode()
            current.add_link(c, new_node)

            # if we came from some previous node, make that
            # node's suffix link point here
            if previous is not None:
                previous.suffix_link = new_node

            # walk down the suffix links
            previous = new_node
            current = current.suffix_link

        # make the last suffix link
        if current is root:
            previous.suffix_link = root
        else:
            previous.suffix_link = current.children[c]

        # move to the newly added child of the longest path
        # (which is the new longest path)
        longest = longest.children[c]
    return root


def search_suffix_trie(trie, s):
    ''' Recursively searches a suffix tree for a given string. '''
    try:
        for i in s:
            trie = trie.children[i]
    except KeyError:
        return False
    return True


# memoization functions
@decorator
def memodict(f):
    ''' Memoization decorator for a function taking a single argument. '''
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


def memoize(f):
    ''' Memoization decorator for a function taking multiple arguments. '''
    f.cache = {}

    @functools.wraps(f)
    def memoize(*args, **kw):
        if kw:  # frozenset is used to ensure hashability
            key = args, frozenset(kw.iteritems())
        else:
            key = args
        cache = f.cache
        if key in cache:
            return cache[key]
        else:
            cache[key] = result = f(*args, **kw)
            return result
    return functools.update_wrapper(memoize, f)


# itertools utilities
def flatten(list_of_lists):
    "Flatten one level of nesting"
    return chain.from_iterable(list_of_lists)