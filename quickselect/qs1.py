class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # https://leetcode.com/problems/k-closest-points-to-origin/discuss/219442/Python-with-quicksort-algorithm
        # O(N) quickselect is most optimal time complexity
        # but O(NlogK) heap w slight modification runs faster in practice
        
        # quickselect: we want to find a pivot K, the kth smallest element
        # in which there are k smaller elements to its left (not necessarily sorted order)
        self.sort(points, 0, len(points)-1, K)
        return points[:K] # the k smallest elements
    
    def sort(self, points, l, r, K):
        if l < r:
            # obtain p, the rank of the curr pivot
            # this means there are p elements smaller or equal to curr pivot
            p = self.partition(points, l, r)
            if p == K: # if there are K elements <= pivot, we found soln
                return
            elif p < K: # less than K elements <= curr pivot
                self.sort(points, p+1, r, K) # search for pivot on the right side
            elif p > K: # more than K elements <= curr pivot
                self.sort(points, l, p-1, K) # search left side
                
    def partition(self, points, l, r):
        pivot = points[r] # we can also randomize or use MoM
        pivot_dist = pivot[0]**2 + pivot[1]**2
        a = l # a is the eventual rank of the curr pivot
        for i in range(l, r):
            point_dist = points[i][0]**2 + points[i][1]**2
            if point_dist <= pivot_dist:
                points[a], points[i] = points[i], points[a] # put ele on the left
                a += 1 # increment a when we find element <= pivot
        points[a], points[r] = points[r], points[a] # put the pivot in the center of elements <= it and elements > it
        return a
    