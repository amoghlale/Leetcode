class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output_list = []
        counter = 0
        while counter < len(asteroids):
            if len(output_list) > 0 and output_list[-1] > 0 and asteroids[counter] < 0:
                if abs(asteroids[counter]) > output_list[-1]:
                    output_list.pop()
                    continue
                elif abs(asteroids[counter]) == output_list[-1]:
                    output_list.pop()
            else:
                output_list.append(asteroids[counter])
            counter += 1
        return output_list
