class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # instead of 'push()', I am using append to add elements at the top of the stack.
                stack.append(c)

        return True if not stack else False




        """
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

1/ Open brackets must be closed by the same type of brackets.
2/ Open brackets must be closed in the correct order.

Example 1:                    => Rule 1 and 2
Input: s = "()"
Output: true

Example 2:                    => Rule 1 and 2
Input: s = "()[]{}"
Output: true

Example 3:                    => Rule 2
Input: s = "(]"
Output: false

Example 4:                    => Rule 3
Input: s = "(])"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


- Need to define "valid"
- "Valid" means a few things:
    - 1. An open always is eventually closed
    - 2. An open is always closed by the same "type"
        - Eg. (} is not the same type
    
    (pause, check with interviewer)

    - 3. There are no "dangling closes"

Stacks as LIFO ("last in, first out")

                |   |
                |   |
                |   |
                | z |
                | y |
                |_x_|

Queue FIFO
          last in line -> ... z  y  x ... -> first served


"""


class Solution:
    def isValid(self, s: str) -> bool:
        """This is where your answer goes
        Example: (())
                   .

        """
        stack = []
        for character in s:
            if character == "(":
                stack.append(character)
            else:  # character == ")"
                if len(stack) == 0:
                    return False
                last_element = stack.pop()
                if last_element == "(":  # found a match!
                    pass
                # only happens when character == ")" but the last element
                # on the stack is NOT an "("
                else:
                    return False  # bailing early
        # if you've gotten to the end, and there's still
        # stuff on the stack, then you know that there
        # are a bunch of opens that haven't yet been closed
        if len(stack) > 0:  # we've paired all opens
            return False  # bailing early
        return True


def main() -> None:
    sol = Solution()
    # ans = sol.isValid("(())")
    # ans = sol.isValid("((")  # return False
    # ans = sol.isValid("(()")  # return False
    # ans = sol.isValid(")")  # return False
    # ans = sol.isValid("))")  # return False
    # ans = sol.isValid("((())")  # return False
    ans = sol.isValid("()()")  # return True
    print(ans)


if __name__ == "__main__":
    main()