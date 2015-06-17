class Solution:
    # @param {integer} n
    # @return {integer[][]}

    def fill(self, matrix, x, y, ctr, depth):
        rows = len(matrix) - (2 * depth)
        # go left. row remains the same.
        for i in xrange(y, y + rows):
            matrix[x][i] = ctr
            ctr += 1
        x, y = x + 1, y + rows - 1
        # go down. col remains the same.
        for i in xrange(x, x + rows - 1):
            matrix[i][y] = ctr
            ctr += 1
        x, y = x + rows - 2, y - 1
        # go left. row remains the same.
        for i in xrange(y, y - rows + 1, -1):
            matrix[x][i] = ctr
            ctr += 1
        x, y = x - 1, y - rows + 2
        # go up. col remains the same.
        for i in xrange(x, x - rows + 2, -1):
            matrix[i][y] = ctr
            ctr += 1
        x, y = x - rows + 3, y + 1
        return x, y, ctr


    def generateMatrix(self, n):
        if n == 0:
            return []
        else:
            matrix = [[0 for x in xrange(n)] for x in xrange(n)]
            flag, x, y, ctr, depth = True, 0, 0, 1, 0
            while flag:
                x, y, ctr = self.fill(matrix, x, y, ctr, depth)
                depth += 1
                if x == n or y == n or matrix[x][y] != 0:
                    break
            return matrix


s = Solution()
mat = s.generateMatrix(5)
for row in mat:
    print " ".join([str(x) for x in row])   