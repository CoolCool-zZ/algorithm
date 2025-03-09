from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # TODO time limit exceeded
        result = 0
        for index in range(len(colors)):
            target_colors = colors[index:min(len(colors), index + k)] + colors[0:max(0, index + k - len(colors))]

            success_flag = True
            prev = target_colors[0]
            for color in target_colors[1:]:
                if prev == color:
                    success_flag = False
                    break
                prev = color

            if success_flag:
                result += 1

        return result
