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
        
        while stack:
            current = stack.pop()
            
            if len(current) == num_length:
                answer.append(current)
            else:
                current_num_index = len(current)
                num_letters = num_to_letters[digits[current_num_index]]
                for letter in num_letters:
                    stack.append(current + letter)
                    
        return answer


        # # If the input is empty, immediately return an empty answer array
        # if len(digits) == 0:
        #     return []

        # # Map all the digits to their corresponding letters
        # letters = {
        #     "2": "abc",
        #     "3": "def",
        #     "4": "ghi",
        #     "5": "jkl",
        #     "6": "mno",
        #     "7": "pqrs",
        #     "8": "tuv",
        #     "9": "wxyz",
        # }

        # def backtrack(index, path):
        #     # If the path is the same length as digits, we have a complete combination
        #     if len(path) == len(digits):
        #         combinations.append("".join(path))
        #         return  # Backtrack

        #     # Get the letters that the current digit maps to, and loop through them
        #     possible_letters = letters[digits[index]]
        #     for letter in possible_letters:
        #         # Add the letter to our current path
        #         path.append(letter)
        #         # Move on to the next digit
        #         backtrack(index + 1, path)
        #         # Backtrack by removing the letter before moving onto the next
        #         path.pop()

        # # Initiate backtracking with an empty path and starting index of 0
        # combinations = []
        # backtrack(0, [])
        # return combinations