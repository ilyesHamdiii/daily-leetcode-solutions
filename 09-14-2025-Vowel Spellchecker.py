#https://leetcode.com/problems/vowel-spellchecker/?envType=daily-question&envId=2025-09-14
# Time:O(n*m)
# 
# # Space:O(n)

class Solution:
    def replace_vowels(self, word):
        vowels = "aeiouAEIOU"
        result = ""
        for char in word:
            if char in vowels:
                result += "*"
            else:
                result += char
        return result
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Preprocess wordlist
        exact_matches = set(wordlist)
        case_insensitive = {}
        vowel_errors = {}
        
        for word in wordlist:
            # Case-insensitive mapping (store first occurrence)
            lower_word = word.lower()
            if lower_word not in case_insensitive:
                case_insensitive[lower_word] = word
            
            # Vowel error mapping (store first occurrence)
            vowel_pattern = self.replace_vowels(lower_word)
            if vowel_pattern not in vowel_errors:
                vowel_errors[vowel_pattern] = word
        
        # Process queries
        res = []
        for query in queries:
            # 1. Exact match
            if query in exact_matches:
                res.append(query)
            
            # 2. Case-insensitive match
            elif query.lower() in case_insensitive:
                res.append(case_insensitive[query.lower()])
            
            # 3. Vowel error match
            elif self.replace_vowels(query.lower()) in vowel_errors:
                res.append(vowel_errors[self.replace_vowels(query.lower())])
            
            # 4. No match
            else:
                res.append("")
        
        return res