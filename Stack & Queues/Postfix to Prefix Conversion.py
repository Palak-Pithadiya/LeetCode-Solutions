class Solution:
    def postToPre(self, s: str) -> str:
        # Your code goes here
        st = []
        i = 0

        while i < len(s):
            char = s[i]

            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9'):
                st.append(char)

            else:
                t1 = st.pop()
                t2 = st.pop()
                con = char + t2 + t1 

                st.append(con)

            i += 1

        return st[0] if st else ''
