class Solution:
    def infixToPostfix(self, s: str) -> str:
        def priority(op):
            if op == '^':
                return 3
            elif op == '*' or op == '/':
                return 2
            elif op == '+' or op == '-':
                return 1
            return 0

        st = []
        ans = ''
        i = 0

        while i < len(s):
            if (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9'):
                ans += s[i]

            elif s[i] == '(':
                st.append(s[i])
            
            elif s[i] == ')':
                while st and st[-1] != '(':
                    ans += st.pop()
                if st:
                    st.pop()

            else:
                while (st and priority(s[i]) <= priority(st[-1])):
                    ans += st.pop()
                st.append(s[i])

            i += 1

        while st:
            ans += st.pop()

        return ans
