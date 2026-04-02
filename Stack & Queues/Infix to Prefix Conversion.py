class Solution:
    def infix_to_prefix(self, s: str) -> str:
        def priority(op):
            if op == '^':
                return 3
            elif op == '*'or op == '/':
                return 2
            elif op == '+'or op == '-':
                return 1
            return 0

        n = len(s)
        reversed_s = ''
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                reversed_s += ')'
            elif s[i] == ')':
                reversed_s += '('
            else:
                reversed_s += s[i]

        st = []
        ans = ""
        i = 0

        while i < len(reversed_s):
            char = reversed_s[i]

            if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9'):
                ans += char

            elif char == '(':
                st.append(char)
            
            elif char == ')':
                while st and st[-1] != '(':
                    ans += st.pop()
                if st:
                    st.pop()

            else:
                if char == '^':
                    while st and priority(char) < priority(st[-1]):
                        ans += st.pop()
                else:
                    while st and priority(char) <= priority(st[-1]):
                        ans += st.pop()
                st.append(char)

            i += 1

        while st:
            ans += st.pop()

        revAns = ans[::-1]
        return revAns
