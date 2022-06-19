"""
class (成人の)BMI:
    関連しそうな属性:
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - BMIは10以上40以下 <- 常識的な範囲
        - 表示するときは小数点第2位まで
            - ex: 23.689 => 23.69
            - ex: 23.681 => 23.68
    できること:
        - BMIの計算

"""


from genericpath import sameopenfile


class BMI:
    """docstring for ClassName."""

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.value = self.weight / (self.height**2)

    # def calculate_bmi(self):
    # BMI = 体重÷身長^2
    # return self.weight/(self.height ** 2)


tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

# tanaka_bmiの身長を出力
print(tanaka_bmi.height)

# BMI出力
# print(tanaka_bmi.calculate_bmi())
print(tanaka_bmi.value)
