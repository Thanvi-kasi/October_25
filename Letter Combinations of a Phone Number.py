class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        # Mapping of digits to letters
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []

        # Backtracking function to generate combinations
        def backtrack(index, current_combination):
            # If the current combination length is equal to digits length, add to result
            if index == len(digits):
                result.append(''.join(current_combination))
                return
            
            # Get the letters for the current digit
            letters = digit_to_letters[digits[index]]
            
            # Explore each letter corresponding to the current digit
            for letter in letters:
                current_combination.append(letter)  # Choose the letter
                backtrack(index + 1, current_combination)  # Recurse for the next digit
                current_combination.pop()  # Undo the choice (backtrack)

        # Start backtracking from index 0
        backtrack(0, [])
        
        return result
