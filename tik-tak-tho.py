
w="yes"
while w=="yes":

    a=b=c=d=e=f=g=h=f=i=" "
    print("LET's PLAY TIC TAK TOE")
    print("       |       |     ")
    print    ("  ",'a', "  |  ",'b',"  |  ",'c')
    print("----------------------")
    print    ("       |       |     ")
    print    ("  ",'d', "  |  ",'e',"  |  ",'f')
    print("----------------------")
    print    ("       |       |     ")
    print     ("  ",'g', "  |  ",'h',"  |  ",'i')

    for I in range (4):
        p=input("enter your choice player 1 b\w a-i:")
        if p not in "a,b,c,d,e,f,g,h,i":
            print("invalid choice you missed your chance player 1")
        if p=="a":
            a="X"
        if p=="b":
            b="X"
        if p=="c":
            c="X"
        if p=="d":
            d="X"
        if p=="e":
            e="X"
        if p=="f":
            f="X"
        if p=="g":
            g="X"
        if p=="h":
            h="X"
        if p=="i":
            i="X"
        print    ("       |       |     ")
        print    ("  ",a, "  |  ",b,"  |  ",c)
        print("----------------------")
        print    ("       |       |     ")
        print    ("  ",d, "  |  ",e,"  |  ",f)
        print("----------------------")
        print    ("       |       |     ")
        print     ("  ",g, "  |  ",h,"  |  ",i)
   
    
        if a==b==c=="X":
            print("player 1 win")
            break
        if d==e==f=="X":
            print("player 1 win")
            break
        if g==h==i=="X":
            print("player 1 win")
            break
        if a==d==g=="X":
            print("player 1 win")
            break
        if b==e==h=="X":
            print("player 1 win")
            break
        if i==f==c=="X":
            print("player 1 win")
            break
        if a==e==i=="X":
            print("player 1 win")
            break
        if g==e==c=="X":
            print("player 1 win")
            break
        l=input("enter your choice player 2 b\w a-i:")
        if l not in "a,b,c,d,e,f,g,h,i":
            print("invalid choice you missed your chance player 2")
            
        if l=="a":
            a="O"
        if l=="b":
            b="O"
        if l=="c":
            c="O"
        if l=="d":
            d="O"
        if l=="e":
            e="O"
        if l=="f":
            f="O"
        if l=="g":
            g="O"
        if l=="h":
            h="O"
        if l=="i":
            i="O"
        print    ("       |       |     ")
        print    ("  ",a, "  |  ",b,"  |  ",c)
        print("----------------------")
        print    ("       |       |     ")
        print    ("  ",d, "  |  ",e,"  |  ",f)
        print("----------------------")
        print    ("       |       |     ")
        print     ("  ",g, "  |  ",h,"  |  ",i)
   

        if a==b==c=="O":
            print("player 2 win")
            break
        if d==e==f=="O":
            print("player 2 win")
            break
        if g==h==i=="O":
            print("player 2 win")
            break
        if a==d==g=="O":
            print("player 2 win")
            break
        if b==e==h=="O":
            print("player 2 win")
            break
        if i==f==c=="O":
            print("player 2 win")
            break
        if a==e==i=="y":
            print("player 2 win")
            break
        if g==e==c=="O":
            print("player 2 win")
            break
    else:
            print("DRAW")
    w=input("want to play more yes / no:")

    
    
    
    
    
    
    


 

