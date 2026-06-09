class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        window = {}
        have = 0
        need = len(t_map)
        result = ""
        result_len = float("infinity")
        left = 0

        for right in range(len(s)):
        # expand window
            c = s[right]
            window[c] = window.get(c, 0) + 1

        # check if this character satisfied a requirement
            if c in t_map and window[c] == t_map[c]:
                have += 1

        # shrink from left while window is valid
            while have == need:
            # update result if this window is smaller
                if (right - left + 1) < result_len:
                    result_len = right - left + 1
                    result = s[left:right + 1]

            # remove left character
                window[s[left]] -= 1
                if s[left] in t_map and window[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1

        return result