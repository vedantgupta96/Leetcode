class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            temp[tuple(arr)].append(s)
        return temp.values()
        
        