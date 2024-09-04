class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs',
                         '8':'tuv', '9':'wxyz'}
        if digits == '':
            return []
        stack = []
        answer = []
        num_length = len(digits)
        
        stack.append("")
        
        while len(stack) > 0:
            current = stack.pop()
            
            if len(current) == num_length:
                answer.append(current)
            else:
                current_num_index = len(current)
                num_letters = num_to_letters[digits[current_num_index]]
                for letter in num_letters:
                    stack.append(current + letter)
                    
        return answer