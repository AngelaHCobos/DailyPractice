class Solution():
    def plusOne(self, digits):
        reversed_digits = reversed(digits)
        for i, x in enumerate(reversed_digits):
            position = len(digits) - i - 1
            if x < 9:
                digits[position]+= 1
                return digits
            digits[position] = 0
        digits.insert(0, 1)
        return digits


num = [9, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]