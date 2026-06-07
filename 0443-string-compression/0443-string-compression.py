class Solution(object):
    def compress(self, chars):
        s = []

        match = chars[0]
        count = 0

        for char in chars:
            if char == match:
                count += 1
            else:
                s.append(match)

                if count > 1:
                    for digit in str(count):
                        s.append(digit)

                match = char
                count = 1

        # process last group
        s.append(match)

        if count > 1:
            for digit in str(count):
                s.append(digit)

        chars[:len(s)] = s

        return len(s)