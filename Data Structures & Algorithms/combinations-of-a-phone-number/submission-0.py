class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Perform dfs such that each ndoe gets added to Path, and at a dead end, PATH is the string formed.

        num_to_str = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []
        
        ans = []

        def dfs (start_point:int, path:List[str]):
            if start_point == len(digits):
                ans.append("".join(path))
                """
                with ans.append(path): Since lists are mutable, path is a pointer to the list's value (path)
                Therefore, in the end after everything, all in ans are pointers which point to path, which
                is now null (all was popped from path).
                "".join creates a new String (immutable) with unique memory. It joins all characters
                from the path and assigns the string space in memory.
                """
                return 
            
            for char in num_to_str[digits[start_point]]:
                path.append(char)
                dfs(start_point+1, path)
                path.pop()
                
            return
            
        
        dfs(0, []) # Modifies ans

        return ans