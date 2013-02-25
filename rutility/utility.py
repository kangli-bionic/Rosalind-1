from string import maketrans
from parsers import grouper
from numpy import *
from decorator import decorator
import functools

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
            start, length = i-flat[i],flat[i]
            yield sy[start:start+length]
    
def longest_common_substring(collection):
    _collection = iter(collection)
    common = ' '.join(list(common_substrings(_collection.next(), _collection.next(), 6)))

    while True:
        try:
            common = ' '.join(list(common_substrings(common, _collection.next(), 6)))
        except StopIteration:
            return common

# SuffixTrie functions
class SuffixNode:
    ''' A SuffixNode, for use in build_suffix_trie '''
    def __init__(self, suffix_link = None):
        self.children = {}
        if suffix_link is not None:
           self.suffix_link = suffix_link
        else:
           self.suffix_link = self
    def add_link(self, c, v):
        """link this node to node v via string c"""
        self.children[c] = v

def build_suffix_trie(s):
    ''' A native python suffix trie. 
    Not very efficient. '''
    assert len(s) > 0
    # explicitly build the two-node suffix tree
    Root = SuffixNode()      # the root node
    Longest = SuffixNode(suffix_link = Root)
    Root.add_link(s[0], Longest)
    
    # for every character left in the string
    for c in s[1:]:
        Current = Longest; Previous = None
        while c not in Current.children:

            # create new node r1 with transition Current -c->r1
            r1 = SuffixNode()
            Current.add_link(c, r1)

            # if we came from some previous node, make that
            # node's suffix link point here
            if Previous is not None:
                Previous.suffix_link = r1

            # walk down the suffix links
            Previous = r1
            Current = Current.suffix_link

        # make the last suffix link
        if Current is Root:
            Previous.suffix_link = Root
        else:
            Previous.suffix_link = Current.children[c]

        # move to the newly added child of the longest path
        # (which is the new longest path)
        Longest = Longest.children[c]
    return Root

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
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

def memoize(f):
    f.cache = {}
    @functools.wraps(f)
    def memoize(*args, **kw):
        if kw: # frozenset is used to ensure hashability
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