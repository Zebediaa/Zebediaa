import numpy as np
import pandas as pd

class SudokuSolver:
    def __init__(self, problem_grid):
        self.problem_grid = problem_grid
        self.n = len(problem_grid)

    def verify_if_value_is_valid(self,index_row,index_column,value):

        # verify line and column

        for i in range(self.n):
            if value == self.problem_grid[index_row][i]:

                return False

        for i in range(self.n):
            if value == self.problem_grid[i][index_column]:

                return False

        # verify Matrix

        matr_line = (index_row//3)*3
        matr_column = (index_column//3)*3


        for i in range(0,3):
            for k in range(0,3):
                if value == self.problem_grid[matr_line + i][matr_column + k]:
                    return False
        return True

        pass


    def __str__(self):
        return f"Le problème est \n{self.problem_grid}"


    def count(self):

        if 0 not in self.problem_grid:

            print(self.problem_grid)

        for i in range(0,self.n):
            for k in range(0,self.n):
                if self.problem_grid[i][k] == 0:
                    for m in range(1,1 + self.n):
                        if self.verify_if_value_is_valid(i,k,m):
                            self.problem_grid[i][k] = m
                            self.count()
                            self.problem_grid[i][k] = 0
                    return None


    def solve(self):
        # self.count()
        self.count()
        self.problem_grid
        # print(range(1,self.n))










    # return print(self.df[0].iloc[0])
