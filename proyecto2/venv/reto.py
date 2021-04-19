def run():

    squares=[i for i in range(1, 100000) if (i %4 ==0) & (i%6==0) & (i%9==0) ]
    print(squares)
            

if __name__=="__main__":
    run()