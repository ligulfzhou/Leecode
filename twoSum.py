class Solution:
    def twoSum(self, numbers, target):
        num = sorted(numbers)
        length = len(numbers)
        left = 0
        right = length - 1
        index = []
        while left < right:
            sums = num[left] + num[right]
            if sums > target:
                right -= 1
            elif sums < target:
                left += 1
            else:
                for i in range(length):
                    if numbers[i] == num[left]:
                        index.append(i + 1)
                    elif numbers[i] == num[right]:
                        index.append(i + 1)
                    if len(index) == 2:
                        break
                break

        res = tuple(index)
        return res