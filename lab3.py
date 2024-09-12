
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root
import scipy.stats as stats
from scipy.integrate import quad

def p(x,mean,std):
    return np.exp(-0.5 * ((x -  mean) / std) ** 2) /(std * np.sqrt(2 * np.pi))

def equation(x):
    global mean1,mean2,std1,std2,pc1,pc2
    t =p(x,mean1,std1) /p(x,mean2,std2)
    P= pc2/pc1
    return t - P


mean1 = 150  
std1 = 50   
mean2 = 300  
std2 = 80


x = np.linspace(mean1 - 3*std1, mean1 + 3*std1+100, 1000)

pdf1 = stats.norm.pdf(x, mean1, std1)
pdf2 = stats.norm.pdf(x, mean2, std2)

pc1 =0.3
pc2 =1-pc1
pdf11 =pc1* stats.norm.pdf(x, mean1, std1)
pdf21 =pc2* stats.norm.pdf(x, mean2, std2)

result= root(equation,x0=100)
print(result.x)

def pdf1func(x):
    return pc2*stats.norm.pdf(x, mean1, std1)
def pdf2func(x):
    return pc1*stats.norm.pdf(x, mean2, std2)


integral1, xz = quad(pdf2func, -np.inf, result.x)
integral2, xz = quad(pdf1func, result.x, np.inf)

print("Ложная тревога [{}, {}]: {}".format(-np.inf, result.x, integral1))
print("Пропуск обнаружения [{}, {}]: {}".format(result.x, np.inf,integral2))
print("Значение  {}".format(integral1+integral2) )


plt.plot(x, pdf1, label='1 cdf',alpha=0.3,linestyle='--')
plt.plot(x, pdf2, label='2 cdf',alpha=0.3,linestyle='--')

plt.plot(x, pdf11, label='1" cdf')
plt.plot(x, pdf21, label='2" cdf')
plt.fill_between(x, pdf11, color='skyblue', alpha=0.4)
plt.fill_between(x, pdf21, color='y', alpha=0.4)
plt.fill_between(x, np.minimum(pdf11, pdf21), color='b', alpha=0.4, label='Общая область')
plt.axvline(x=result.x, color='r', label='x', linewidth=2)  

plt.text(result.x, 0.0003, 'Ошибка {}%'.format(round(100*(integral1+integral2),3)), fontsize=12, color='black', ha='center')

plt.title('РЕЗУЛЬТАТ')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)


plt.show()
