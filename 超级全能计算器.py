import math
import statistics
import sys

import numpy as np
from sympy import *


def calculator():
    global sum
    print("欢迎使用万能计算机！")
    while True:
        print("0. 退出程序","1. 加法","2. 减法","3. 乘法","4. 除法","5. 平方根","6. 立方根","7. 次方根""8. 幂函数""9. 指数函数","10. 自然对数","11. 常用对数")
        print("12. 绝对值","13. 阶乘""14. 向上取整","15. 向下取整","16. 四舍五入""17. 三角函数","18. 反三角函数","19. 矩阵函数","20. 平均值","21. 标准差")
        print("22. 方差","23. 中位数","24. 众数","25. 累计分布函数","26. 非标尊/正态分布函数","27. 偏度","28. 峰度","29. 对数函数","30. 最大公约数")
        print("31. 最小公倍数","32. 等差数列求和","33. 对比数列求和","34. 自变量","35. 体积/面积/周长","36. 混合运算","37. 十进制转换")
        choice = input("请选择要进行的操作: ")
        if choice == '1':
            try:
                num1 = float(input("请输入被加数: "))
                num2 = float(input("请输入加数: "))
                result = num1 + num2
                print(num1, ' + ', num2, ' = ', result)
            except ValueError:
                print("输入错误，请输入数字!")

        elif choice == '2':
            try:
                num1 = float(input("请输入被减数: "))
                num2 = float(input("请输入减数: "))
                result = num1 - num2
                print(num1, '-', num2, '=', result)
            except ValueError:
                print("输入错误，请输入数字!")

        elif choice == '3':
            try:
                num1 = float(input("请输入被乘数: "))
                num2 = float(input("请输入乘数: "))
                result = num1 * num2
                print(num1, 'x', num2, '=', result)
            except ValueError:
                print("输入错误，请输入数字!")

        elif choice == '4':
            try:
                num1 = float(input("请输入被除数: "))
                num2 = float(input("请输入除数: "))
                result = num1 // num2
                result1 = num1 % num2
                print(f"{num1} ÷ {num2} = {result} ...... {result1}")
            except ValueError:
                print("输入错误:请输入数字!")
            except ZeroDivisionError:
                print("输入错误:除数不能为零!")

        elif choice == '5':
            try:
                num = float(input("请输入一个数字: "))
                result = math.sqrt(num)
                print(num, "的平方根为: ", result)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '6':
            try:
                num = float(input("请输入一个数字: "))
                result = num ** (1 / 3)
                print(num, "的立方根为: ", result)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '7':
            try:
                num1 = float(input("请输入一个数字: "))
                num2 = int(input("请输入次方数: "))
                result = num1 ** (1 / num2)
                print(num2, "的次方根为: ", result)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '8':
            try:
                num1 = float(input("请输入底数: "))
                num2 = float(input("请输入指数: "))
                def power(num1, num2):
                    result = num1 ** num2
                    return result
                print(f"{num1}^{num2} = {power(num1, num2)}")
            except ValueError:
                print("输入错误:请输入数字。")

        elif choice == '9':
            try:
                num1 = float(input('请输入一个数字: '))
                print(f"e^{num1} = {math.exp(num1)}")
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '10':
            try:
                num1 = float(input('请输入一个数字: '))
                if num1 <= 0:
                    print("输入错误: 数字必须大于0")
                else:
                    print(f"ln({num1}) = {math.log(num1)}")
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '11':
            try:
                num1 = float(input('请输入一个数字: '))
                if num1 <= 0:
                    return "输入错误: 数字必须大于0"
                else:
                    print(f"log10({num1}) = {math.log10(num1)}")
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '12':
            try:
                num1 = float(input('请输入一个数字: '))
                result = abs(num1)
                print(num1, "的绝对值为: ", result)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '13':
            try:
                num1 = int(input("请输入第一个正数:"))
                factorial = 1
                if num1 < 0:
                    print("输入无效:负数没有阶乘!")
                else:
                    for i in range(1, num1 + 1):
                        factorial = factorial * i
                print(num1, "的阶乘为: ", factorial)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '14':
            try:
                num1 = float(input("请输入一个数字: "))
                num2 = int(input("请输入二个数字: "))
                print(num1, '和', num2, "的向上取整的结果为: ", math.ceil(num1), math.ceil(num2))
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '15':
            try:
                num1 = float(input("请输入一个数字: "))
                num2 = int(input("请输入二个数字: "))
                print(num1,'和',num2,"的向下取整的结果为: ", math.floor(num1),math.floor(num2))
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '16':
            try:
                num1 = float(input("请输入一个数字: "))
                print(num1,"的四舍五入的结q果为: ", round(num1))
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '17':
            while True:
                print("-1. 退出程序","0. 退出函数","1. sin正弦值","2. cos余弦值")
                print("3. tan正切值","4. cot正切的倒数","5. sec余弦的倒数","6. csc正弦的倒数")
                choice = int(input("请选择要计算的三角函数："))
                if choice == -1:
                    print("感谢使用超级全能计算机，欢迎下次再来，再见！")
                    sys.exit()
                elif choice == 0:
                    print("已退出三角函数")
                    break

                elif choice == 1:
                    try:
                        num1 = float(input("请输入角度(0~360度): "))
                        if num1 < 0 or num1 > 360:
                            print("输入无效:请输入0~360度之间的角度值！")
                        else:
                            print("sin({}) = {}".format(num1, math.sin(math.radians(num1))))
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 2:
                    try:
                        num1 = float(input("请输入角度(0~360度): "))
                        if num1 < 0 or num1 > 360:
                            print("输入无效:请输入0~360度之间的角度值！")
                        else:
                            print("cos({}) = {}".format(num1, math.cos(math.radians(num1))))
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 3:
                    try:
                        num1 = float(input("请输入角度(0~360度): "))
                        if num1 < 0 or num1 > 360:
                            print("输入无效:请输入0~360度之间的角度值！")
                        else:
                            print("tan({}) = {}".format(num1, math.tan(math.radians(num1))))
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 4:
                    try:
                        num1 = float(input("请输入角度(0~360度): "))
                        if num1 < 0 or num1 > 360:
                            print("输入无效:请输入0~360度之间的角度值！")
                        else:
                            print("cot({}) = {}".format(num1, 1 / math.tan(math.radians(num1))))
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 5:
                    try:
                        num1 = float(input("请输入角度(0~360度): "))
                        if num1 < 0 or num1 > 360:
                            print("输入无效:请输入0~360度之间的角度值！")
                        else:
                            print("sec({}) = {}".format(num1, 1 / math.cos(math.radians(num1))))
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 6:
                    try:
                        num1 = float(input("请输入角度(0~360度): "))
                        if num1 < 0 or num1 > 360:
                            print("输入无效:请输入0~360度之间的角度值！")
                        else:
                            print("csc({}) = {}".format(num1, 1 / math.sin(math.radians(num1))))
                    except ValueError:
                        print("输入错误:请输入数字!")
                else:
                    print("选择无效: 请重新选择！")

        elif choice == '18':
            while True:
                print("-1. 退出程序","0. 退出函数","1. 反正弦","2. 反余弦","3. 反正切")
                choice = float(input("请选择要计算的反三角函数："))

                if choice == -1:
                    print("感谢使用超级全能计算机，欢迎下次再来，再见！")
                    sys.exit()

                elif choice == 0:
                    print("已退出反三角函数")
                    break

                elif choice == 1:
                    try:
                        num1 = float(input("请输入正弦值(-1到1之间): "))
                        if num1 < -1 or num1 > 1:
                            print("输入无效:数字必须在-1到1之间")
                        else:
                            result = math.asin(num1)
                            print(f"{num1} {'的反正弦的结果为: '} {result}")
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 2:
                    try:
                        num1 = float(input("请输入余弦值(-1到1之间): "))
                        if num1 < -1 or num1 > 1:
                            print("输入无效:数字必须在-1到1之间")
                        else:
                            result = math.acos(num1)
                            print(f"{num1} {'的余弦值的结果为: '} {result}")
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 3:
                    try:
                        x = float(input("请输入正切值: "))
                        result = math.atan(x)
                        print("反正切值为: ", result)
                    except ValueError:
                        print("输入错误:请输入数字!")
                else:
                    print("选择无效: 请重新选择！")

        elif choice == '19':
            while True:
                print("-1. 退出程序","0. 退出函数","1. 矩阵加法","2. 矩阵减法","3. 矩阵乘法")
                print("4. 矩阵转置","5. 矩阵求逆","6. 矩阵行列式","7. 矩阵特征值和特征向量")
                choice = int(input("请选择要计算的矩阵函数: "))

                if choice == -1:
                    print("感谢使用超级全能计算机，欢迎下次再来，再见！")
                    sys.exit()

                elif choice == 0:
                    print("已退出反三角函数")
                    break

                elif choice == 1:
                    try:
                        n = int(input("请输入矩阵的行数和列数: "))
                        m1 = np.zeros((n, n))
                        m2 = np.zeros((n, n))
                        a = int(input("请输入第一个矩阵的元素: "))
                        for i in range(n):
                            for j in range(n):
                                m1[i][j] = a
                        b = int(input("请输入第二个矩阵的元素: "))
                        for i in range(n):
                            for j in range(n):
                                m2[i][j] = b
                        result = m1 + m2
                        print("矩阵相加的结果为: ")
                        print(result)
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 2:
                    try:
                        n = int(input("请输入矩阵的行数和列数: "))
                        m1 = np.zeros((n, n))
                        m2 = np.zeros((n, n))
                        a = int(input("请输入第一个矩阵的元素: "))
                        for i in range(n):
                            for j in range(n):
                                m1[i][j] = a
                        b = int(input("请输入第二个矩阵的元素: "))
                        for i in range(n):
                            for j in range(n):
                                m2[i][j] = b
                        result = m1 - m2
                        print("矩阵相减的结果为: ")
                        print(result)
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 3:
                    try:
                        n = int(input("请输入第一个矩阵的行数: "))
                        m = int(input("请输入第一个矩阵的列数和第二个矩阵的行数: "))
                        p = int(input("请输入第二个矩阵的列数: "))
                        m1 = np.zeros((n, m))
                        m2 = np.zeros((m, p))
                        c = int(input("请输入第一个矩阵的元素: "))
                        for i in range(n):
                            for j in range(m):
                                m1[i][j] = c
                        e = int(input("请输入第二个矩阵的元素: "))
                        for i in range(m):
                            for j in range(p):
                                m2[i][j] = e
                        result = np.dot(m1, m2)
                        print("矩阵相乘的结果为: ")
                        print(result)
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 4:
                    try:
                        n = int(input("请输入矩阵的行数和列数: "))
                        m = np.zeros((n, n))
                        t = int(input("请输入矩阵的元素:  "))
                        for i in range(n):
                            for j in range(n):
                                m[i][j] = t
                        result = m.transpose()
                        print("矩阵转置的结果为:  ")
                        print(result)
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 5:
                    try:
                        num1 = int(input("请输入矩阵的维数: "))
                        matrix = []
                        for i in range(num1):
                            row = list(map(float, input("请输入矩阵的元素: ").split()))
                            matrix.append(row)
                        matrix = np.array(matrix)
                        try:
                            inverse = np.linalg.inv(matrix)
                            print("矩阵的逆矩阵为: ")
                            print(inverse)
                        except np.linalg.LinAlgError:
                            print("矩阵不可逆，无法计算逆矩阵！")
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 6:
                    try:
                        def get_matrix_size():
                            rows = int(input("请输入矩阵的行数: "))
                            cols = int(input("请输入矩阵的列数: "))
                            return rows, cols
                        def get_matrix_elements(rows, cols):
                            print("请输入矩阵的元素: ")
                            elements = []
                            for i in range(rows):
                                row = []
                                for j in range(cols):
                                    element = float(input("请输入第{}行第{}列的元素: ".format(i + 1, j + 1)))
                                    row.append(element)
                                elements.append(row)
                            return elements
                        def calculate_determinant(matrix):
                            det = np.linalg.det(matrix)
                            return det
                        def main():
                            rows, cols = get_matrix_size()
                            elements = get_matrix_elements(rows, cols)
                            matrix = np.array(elements)
                            determinant = calculate_determinant(matrix)
                            print("矩阵的行列式为: {}".format(determinant))
                        if __name__ == '__main__':
                            main()
                    except ValueError:
                        print("输入错误:请输入数字!")

                elif choice == 7:
                    try:
                        def get_matrix_size():
                            rows = int(input("请输入矩阵的行数: "))
                            cols = int(input("请输入矩阵的列数: "))
                            return rows, cols
                        def get_matrix_elements(rows, cols):
                            a = int(input("请输入矩阵的元素: "))
                            elements = a
                            for i in range(rows):
                                row = []
                                for j in range(cols):
                                    element = float(input("请输入第{}行第{}列的元素: ".format(i + 1, j + 1)))
                                    row.append(element)
                                elements.append(row)
                            return elements
                        def calculate_determinant(matrix):
                            try:
                                det = np.linalg.det(matrix)
                                return det
                            except np.linalg.LinAlgError:
                                new_shape = (matrix.shape[0] * matrix.shape[1], matrix.shape[-1])
                                matrix = matrix.reshape(new_shape)
                                det = np.linalg.det(matrix)
                                matrix = matrix.reshape((matrix.shape[0] // matrix.shape[1], matrix.shape[1], matrix.shape[-1]))
                                return det
                        def main():
                            rows, cols = get_matrix_size()
                            elements = get_matrix_elements(rows, cols)
                            matrix = np.array(elements)
                            determinant = calculate_determinant(matrix)
                            print("矩阵的行列式为: {}".format(determinant))
                        if __name__ == '__main__':
                            main()
                    except ValueError:
                        print("输入错误:请输入数字!")
                else:
                    print("选择无效: 请重新选择！")

        elif choice == '20':
            try:
                nums = []
                n = int(input("请输入数字的数量: "))
                for i in range(n):
                    num = float(input("请输入第 %d 个数字: " % (i + 1)))
                    nums.append(num)
                avg = sum / n
                print("这组数字的平均值是: ", avg)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '21':
            try:
                numbers1 = input("请输入数字列表，用逗号或空格分隔: ").replace(",", " ").split()
                numbers1 = [float(x) for x in numbers1]
                mean = sum / len(numbers1)
                variance = sum / len(numbers1)
                std_deviation = math.sqrt(variance)
                print("输入的数字列表为: ", numbers1)
                print("标准差为: ", std_deviation)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '22':
            try:
                numbers2 = input("请输入数字，用逗号或空格分隔: ").replace(",", " ").split()
                numbers2 = [float(num) for num in numbers2]
                mean = sum / len(numbers2)
                diffs = [(num - mean) ** 2 for num in numbers2]
                variance = sum / len(numbers2)
                print("方差为: ", variance)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '23':
            try:
                numbers3 = input("请输入数字，用逗号或空格分隔: ").replace(",", " ").split()
                numbers3 = [float(num) for num in numbers3]
                numbers3.sort()
                n = len(numbers3)
                if n % 2 == 0:
                    median = (numbers3[n // 2 - 1] + numbers3[n // 2]) / 2
                else:
                    median = numbers3[n // 2]
                print("中位数为: ", median)
            except ValueError:
                print("输入错误:请输入数字!")

        elif choice == '24':
            numbers = input("请输入数字列表，用逗号或空格分隔: ").replace(",", " ").split()
            try:
                numbers = [int(num) for num in numbers]
                mode = statistics.mode(numbers)
                print("众数为: ", mode)
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '25':
            try:
                def normal_pdf(x, mean, std_dev):
                    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-((x - mean) ** 2) / (2 * (std_dev ** 2)))
                def normal_cdf(x, mean, std_dev):
                    z = (x - mean) / (std_dev * math.sqrt(2))
                    return 0.5 * (1 + math.erf(z))
                x = float(input("请输入x值："))
                mean = float(input("请输入均值："))
                std_dev = float(input("请输入标准差："))
                pdf = normal_pdf(x, mean, std_dev)
                cdf = normal_cdf(x, mean, std_dev)
                print("在正态分布 N(%.2f, %.2f) 下：" % (mean, std_dev))
                print("概率密度函数值为：%.4f" % pdf)
                print("累计分布函数值为：%.4f" % cdf)
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '26':
            try:
                def normal_distribution():
                    x = float(input("请输入自变量x的值："))
                    mean = float(input("请输入均值μ的值："))
                    std_dev = float(input("请输入标准差σ的值："))
                    first_part = 1 / (std_dev * math.sqrt(2 * math.pi))
                    second_part = math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
                    result = first_part * second_part
                    print("正态分布函数在x={}处的值为：{}".format(x, result))
                normal_distribution()
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '27':
            try:
                data = input("请输入数据，以空格分隔：")
                data = list(map(float, data.split()))
                def skew(data):
                    pass
                skewness = skew(data)
                print("数据的偏度为：", skewness)
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '28':
            try:
                num1 = float(input("第一个数值："))
                num2 = float(input("第二个数值："))
                sharpness = abs(num1 - num2)
                print("锋度为：", sharpness)
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '29':
            while True:
                try:
                    print("-1. 退出程序", "0. 退出函数", "1. 自然对数（以 e 为底数）","2. 以 10 为底数")
                    choice = int(input("请选择（输入数字）："))
                    num2 = float(input("真数："))

                    if choice == -1:
                        print("感谢使用超级全能计算机，欢迎下次再来，再见！")
                        sys.exit()

                    elif choice == 0:
                        print("已退出反三角函数")
                        break

                    elif choice == 1:
                        logarithm = math.log(num2)
                        print("自然对数为：", logarithm)

                    elif choice == 2:
                        logarithm = math.log10(num2)
                        print("以 10 为底数的对数为：", logarithm)
                    else:
                        print("选择无效: 请重新选择！")
                except ValueError:
                    print("输入错误:请输入数字!")

        elif choice == '30':
            try:
                num1 = int(input("第一个数："))
                num2 = int(input("第二个数："))
                while num2 != 0:
                    temp = num2
                    num2 = num1 % num2
                    num1 = temp
                print("最大公约数为：", num1)
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '31':
            try:
                print("欢迎使用最小公倍数计算器！")
                print("请输入两个正整数：")
                num1 = int(input("第一个数："))
                num2 = int(input("第二个数："))
                def gcd(x, y):
                    while y != 0:
                        x, y = y, x % y
                    return x
                lcm = num1 * num2 // gcd(num1, num2)
                print("最小公倍数为：", lcm)
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '32':
            try:
                a = float(input("首项："))
                d = float(input("公差："))
                n = int(input("项数："))
                sum = (2 * a + (n - 1) * d) * n / 2
                print("等差数列的和为：", sum)
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '33':
            try:
                a = float(input("首项："))
                d = float(input("公差："))
                n = int(input("项数："))
                sum = (2 * a + (n - 1) * d) * n / 2
                print("等差数列的和为：", sum)
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '34':
            try:
                def normal_distribution():
                    x = float(input("请输入自变量x的值："))
                    mean = float(input("请输入均值μ的值："))
                    std_dev = float(input("请输入标准差σ的值："))
                    first_part = 1 / (std_dev * math.sqrt(2 * math.pi))
                    second_part = math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
                    result = first_part * second_part
                    print("正态分布函数在x={}处的值为：{}".format(x, result))
                normal_distribution()
            except ValueError:
                print("输入错误：请输入数字！")

        elif choice == '35':
            while True:
                try:
                   print("-1. 退出程序", "0. 退出函数", "1. 圆形", "2. 矩形", "3. 立方体", "3. 立方体","4. 圆柱体", "5. 圆锥体","6. 三角形","7. 梯形",)
                   choice = int(input("请选择要计算的图形:"))

                   if choice == -1:
                       print("感谢使用超级全能计算机，欢迎下次再来，再见！")
                       sys.exit()

                   elif choice == 0:
                       print("已退出反三角函数")
                       break

                   elif choice == 1:
                       radius = float(input("请输入圆的半径:"))
                       def circle_area(radius):
                           return math.pi * radius ** 2
                       def circle_perimeter(radius):
                           return 2 * math.pi * radius
                       print("圆的面积为: ", circle_area(radius))
                       print("圆的周长为: ", circle_perimeter(radius))

                   elif choice == 2:
                       length = float(input("请输入矩形的长度: "))
                       width = float(input("请输入矩形的宽度: "))
                       def rectangle_area(length, width):
                           return length * width
                       def rectangle_perimeter(length, width):
                           return 2 * (length + width)
                       print("矩形的面积为: ", rectangle_area(length, width))
                       print("矩形的周长为: ", rectangle_perimeter(length, width))

                   elif choice == 3:
                       length = float(input("请输入立方体的边长: "))
                       def cube_volume(length):
                           return length ** 3
                       print("立方体的体积为: ", cube_volume(length))

                   elif choice == 4:
                       radius = float(input("请输入圆柱体的底面半径: "))
                       height = float(input("请输入圆柱体的高: "))
                       def cylinder_volume(radius, height):
                           return math.pi * radius ** 2 * height
                       print("圆柱体的体积为: ", cylinder_volume(radius, height))

                   elif choice == 5:
                       radius = float(input("请输入圆锥体的底面半径: "))
                       height = float(input("请输入圆锥体的: "))
                       def cone_volume(radius, height):
                           return 1 / 3 * math.pi * radius ** 2 * height
                       print("圆锥体的体积为: ", cone_volume(radius, height))

                   elif choice == 6:
                       base1 = float(input("请输入梯形的上底长: "))
                       base2 = float(input("请输入梯形的下底长: "))
                       height = float(input("请输入梯形的高: "))
                       side1 = float(input("请输入梯形的第一条斜边长: "))
                       side2 = float(input("请输入梯形的第二条斜边长: "))
                       def trapezoid_area(base1, base2, height):
                           return (base1 + base2) * height / 2
                       print("梯形的面积为: ", trapezoid_area(base1, base2, height))
                       def trapezoid_perimeter(base1, base2, height, side1, side2):
                           return base1 + base2 + side1 + side2
                       print("梯形的周长为: ", trapezoid_perimeter(base1, base2, height, side1, side2))

                   elif choice == 7:
                       base = float(input("请输入三角形的底边长: "))
                       height = float(input("请输入三角形的高: "))

                       def triangle_area(base, height):
                           return base * height / 2
                       print("三角形的面积为: ", triangle_area(base, height))
                       side1 = float(input("请输入三角形的第一条边长: "))
                       side2 = float(input("请输入三角形的第二条边长: "))
                       side3 = float(input("请输入三角形的第三条边长: "))
                       def triangle_perimeter(side1, side2, side3):
                           return side1 + side2 + side3
                       print("三角形的周长为: ", triangle_perimeter(side1, side2, side3))
                   else:
                       print("输入无效: 请重新输入! ")
                except ValueError:
                    print("输入错误：请输入数字！")

        elif choice == '36':
            try:
                x, y, z = symbols('x y z')
                expr = input("请输入表达式: ")
                result = simplify(expr)
                print("简化后的表达式为: ", result)
            except ValueError:
                print("输入错误: 请输入数字！")

        elif choice == '37':
            try:
                def decimal_to_base(n, base):
                    result = ''
                    while n > 0:
                        digit = n % base
                        if digit < 10:
                            result = str(digit) + result
                        else:
                            result = chr(ord('A') + digit - 10) + result
                        n //= base
                    return result
                decimal = int(input("请输入一个十进制数: "))
                base = int(input("请输入目标进制数(2、8、16等): "))
                if base not in [2, 8, 10, 16]:
                    print("目标进制数必须为2、8、10或16！")
                result = decimal_to_base(decimal, base)
                print(f"{decimal}的{base}进制数为: {result}")
            except ValueError:
                print("输入错误: 请输入数字！")

        elif choice == '38':
            try:
                def convert_to_decimal(num, base):
                    decimal = 0
                    power = 0
                    while num > 0:
                        digit = num % 10
                        decimal += digit * (base ** power)
                        num //= 10
                        power += 1
                    return decimal
                num = input("请输入一个多进制数（例如：1010 b=2进制, 1010 o=8进制, 1010 h=16进制:")
                if num[-1] in ['b', 'o', 'h']:
                    base = {'b': 2, 'o': 8, 'h': 16}[num[-1]]
                    num = int(num[:-1], base)
                else:
                    num = int(num)
                    base = 10
                    decimal = convert_to_decimal(num, base)
                    print(f"{num}的十进制数为:{decimal}")
            except ValueError:
                print("输入错误: 请输入数字！")
        # 
        # elif choice == '39':
        #     try:
        # 
        #     except ValueError:
        #         print("输入错误：请输入数字！")
        # 
        # elif choice == '40':
        #     try:
        # 
        #     except ValueError:
        #         print("输入错误：请输入数字！")

        elif choice == '0':
            print("感谢使用超级全能计算机，欢迎下次再来，再见！")
            sys.exit()

        else:
            print("选择无效: 请重新选择！")

calculator()

