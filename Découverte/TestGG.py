# petits tricks python : https://www.turing.com/kb/22-hottest-python-tricksfor-efficient-coding
# petites fonctions avancées : : https://www.codingame.com/playgrounds/500/advanced-python-features
# top 100 astuces : https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958
# doc Microsoft les basiques : https://code.visualstudio.com/docs/python/python-tutorial

def sum_number(*numbers) -> float:
    print(numbers)
    return sum(numbers)

print(sum_number(1,2,3,4,5,6,7,8,9))