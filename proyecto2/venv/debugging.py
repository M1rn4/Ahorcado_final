def divisor(num):
    divisor=[]
    for i in range(1, num+1):
        if num % i ==0:
            divisor.append(i)
    return divisor

def run():
    try:
        
        num = int(input("Ingrese un numero: "))

        try:
            if num<=0:
                raise ValueError("Ingrese un numero positivo")
            print(divisor(num))
            print("Termino mi programa")
        except ValueError as ve:
            print(ve)
            return False     
                
    except ValueError:
        print("Valor invalido, ingrese un numero")

if __name__=="__main__":
    run()  