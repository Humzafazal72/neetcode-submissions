class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_boxes = {"1":{
                        "1":{},
                        "4":{},
                        "7":{},
                        },
                    "4":{
                        "1":{},
                        "4":{},
                        "7":{},
                    },
                    "7":{
                        "1":{},
                        "4":{},
                        "7":{},
                    }
                }
        rows = {}
        cols = {}

        for row in range(9):
            rows[row] = {}
            for col in range(9):
                num = board[row][col]
                if num=='.':
                    continue
                if num in rows.get(row,{}):
                    return False
                if num in cols.get(col,{}):
                    return False
                
                rows[row][num] = ""
                cols.setdefault(col,{})[num] = ""

                if str(row) in sub_boxes:
                    sub_row = str(row)
                else:
                    sub_row = str(int(row)-1) if str(int(row)-1) in sub_boxes else str(int(row)+1)
                
                if str(col) in sub_boxes:
                    sub_col = str(col)
                else:
                    sub_col = str(int(col)-1) if str(int(col)-1) in sub_boxes else str(int(col)+1)
                if num in sub_boxes[sub_row][sub_col]:
                    return False
                sub_boxes[sub_row][sub_col][num]=""
        
        return True