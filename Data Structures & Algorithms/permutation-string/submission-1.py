class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

    # Build frequency maps for s1 and first window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

    # Count initial matches
        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1

    # Slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

        # Add new character on the right
            idx = ord(s2[r]) - ord('a')
            window_count[idx] += 1
            if window_count[idx] == s1_count[idx]:
                matches += 1
            elif window_count[idx] - 1 == s1_count[idx]:
                matches -= 1

        # Remove old character on the left
            idx = ord(s2[l]) - ord('a')
            window_count[idx] -= 1
            if window_count[idx] == s1_count[idx]:
                matches += 1
            elif window_count[idx] + 1 == s1_count[idx]:
                matches -= 1

            l += 1

        return matches == 26