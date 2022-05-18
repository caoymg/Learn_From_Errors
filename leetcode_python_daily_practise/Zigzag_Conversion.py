
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        line = 0
        direction = 1
        # Note the idea of out_line_lst for saving each line as a string in a list
        out_line_lst = [""] * numRows
        
        for i in range(len(s)):
            # Note this, beautiful!
            out_line_lst[line] += s[i]
            
            if numRows > 1:
                line += direction
                # Note this, beautiful!
                if line == 0 or line == numRows -1:
                    direction *= -1
                    
        outputStr = ""
        for j in range(numRows):
            outputStr += out_line_lst[j]
            
        return outputStr
        