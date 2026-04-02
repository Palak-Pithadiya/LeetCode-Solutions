class Solution:
    def prefixToPostfix(self, s: str) -> str:
        # Your code goes here
        st = []
        i = len(s) - 1

        while i >= 0:
            char = s[i]

            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9'):
                st.append(char)

            else:
                t1 = st.pop()
                t2 = st.pop()
                con = t1 + t2 + char

                st.append(con)

            i -= 1

        return st[0] if st else ''
