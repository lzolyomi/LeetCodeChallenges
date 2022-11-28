class Solution:
    def convert(self, s: str, numRows: int):
        rowSolutions = [[] for _ in range(numRows)] # create an empty list for each row
        index = 0
        direction = 'down' # whether we are going up or down
        for char in s:
            rowSolutions[index].append(char)
            if direction=='down':
                if index < numRows - 1: # -1 important to not overflow row index
                    index +=1
                else: # if we reached the downmost row
                    direction='up'
                    index -= 1
            
            elif direction=='up':
                if index > 0:
                    index -= 1
                else:
                    direction = 'down'
                    index += 1

        sol = ''.join([''.join(sublist) for sublist in rowSolutions])
        return sol

if __name__ == "__main__":
    obj = Solution()

    s = "PAYPALISHIRING" 
    numR = 3

    obj.convert(s, numR)