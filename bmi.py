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

        # 10以上40以下のチェック
        if not (10 <= self.value <= 40):
            raise ValueError("基準値外です")

    def __str__(self):
        # return = f"{self.value:.2f}"
        #  基準値(18.5~25)の確認
        if (18 <= self.value <=25):
            return (f"{self.value:.2f} : (普通体重)")
        if (self.value <=18 ):
            return (f"{self.value:.2f} : (低体重)")
        if (25 <= self.value):
            return (f"{self.value:.2f} : (肥満)")
        # if ( self.value < 18.5 or 25 < self.value ):
        # return("正常値を外れます")

    # def calculate_bmi(self):
    # BMI = 体重÷身長^2
    # return self.weight/(self.height ** 2)


tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)
chie_bmi = BMI(height=1.65, weight=49.0)
# 入力に対してBMIを出力

# tanaka_bmiの身長を出力
print(tanaka_bmi.height)

# BMI出力
# print(tanaka_bmi.calculate_bmi())
# print(tanaka_bmi.value)
print(tanaka_bmi)  # 20.ggggg
print(sasami_bmi)
