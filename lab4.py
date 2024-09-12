
import random as r

color_reset = "\033[0m"

attributes = 3

def get_dist(elem, w):
    return sum(elem[i] * w[i] for i in range(attributes))

def dec(w, x, c):
    return tuple(w[i] - c * x[i] for i in range(attributes))

def inc(w, x, c):
    return tuple(w[i] + c * x[i] for i in range(attributes))

def norm(vector):
    hypot = sum(x ** 2 for x in vector) ** 0.5
    if hypot == 0:
        return 0
    return tuple(x / hypot for x in vector)

def show_result(w):

    color_green = "\033[32m" 
    print(f'{color_green}RESULT')


    text = ""
    
    for t in range(len(w)):
        res_text = [f"({w[t][i]}*x{i+1})" for i in range(len(w[t]))]
        res_text = " + ".join(res_text)
        text +=f'd({t}) = {res_text} \n'
    
    print(text)

    print("Конечные веса:")
    for i in range(len(w)):
        print(w[i])

    print(f'{color_reset}') 




def algorythm():
    classes_len= int(input("Введите целое число: "))

    test=[]
    max_iter = 1000
    for i in range(classes_len):
        random_values = tuple(r.randint(-10, 10) for _ in range(attributes))
        test.append(random_values)
    color_red = "\033[31m" 
    
    print('-'*15)
    print(f'{color_red}Attributes of classes{color_reset}')
    for row in test:
        for elem in row:
            print(f" {color_red}{elem}{color_reset} ", end="") 
        print() 
    print()

    print('-'*15)     
    w = [([0] * attributes)] * classes_len
    c = 1

    for _ in range(max_iter):
        need_to_break = True
        for i in range(classes_len):
            dist = [get_dist(test[i], w[j]) for j in range(classes_len)]
            curr_dist = dist[i]
            need_to_inc = False
            for j in range(classes_len):
                if i != j:
                    if dist[j] >= curr_dist:
                        need_to_inc = True
                        need_to_break = False
                        w[j] = dec(w[j], test[i], c)
            if need_to_inc:
                w[i] = inc(w[i], test[i], c)
        if need_to_break:
            break

    show_result(w)
  

algorythm()
