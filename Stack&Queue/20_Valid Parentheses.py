'''给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。'''


class Solution:
    def isValid(self, s: str):
        # 有效字符串长度必然为偶数，如果字符串长度为奇数，直接返回无效
        if len(s) % 2 == 1:
            return False
        # 为了便于判断括号匹配，建立哈希表，键为右括号，值为左括号
        pairs = {')': '(', ']': '[', '}': '{'}  # 用右括号索引左括号
        stack = list()
        for ch in s:  # 遍历字符串中每个字符
            if ch in pairs:  # 判断字符是否属于右括号。注意，遍历的变量中存储的是字典的键，这里判断的也是键'。
                if not stack or stack[-1] != pairs[ch]:  # 如果栈为空或者栈顶元素不是右括号索引到的左括号匹配失败
                    return False
                stack.pop()  # 右括号要出栈
            # 否则遇到左括号就进栈
            else:
                stack.append(ch)
        # 遍历结束后，如果栈中没有左括号，说明字符串中所有左括号闭合，否则匹配无效
        return not stack
