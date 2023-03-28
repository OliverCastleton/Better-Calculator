#Imports
import time
import math
import numpy
#start program
ON = input("Wanna use the calculator?   \n")
rt = 0
#loop
while ON == "YES" or ON == "yes" or ON == "Yes" :
    print("Calcolatrice")
    question0= input("""What calculation would you like to execute?
               A: Algebry
               B: Geometry  \n """)
    if question0.lower() == "a" or question0.lower() == "A" :
        nn = input("How many numbers will your calculation have?   \n")
        #non programmed parts
        if nn == "0" or nn > "3" : print("VAFFANCULO")
        #1 digit calculation
        if nn == "1" :
            question1= input("""What calculation would you like to execute?
                   A: Square
                   B: Square root
                   C: Cube
                   D: Cube root
                   E: Factorial   \n""")
            fn = float(input("1° number :   "))
            #square 
            if question1.lower() == "a" or question1.lower() == "square": rt = fn * fn
            #sqare root 
            if question1.lower() == "b" or question1.lower() == "square root": rt = math.sqrt( fn )
            #cube
            if question1.lower() == "c" or question1.lower() == "cube": rt = fn * fn * fn
            #cube root
            if question1.lower() == "d" or question1.lower() == "cube root": rt = numpy.cbrt( fn )
            #factorial
            if question1.lower() == "e" or question1.lower() == "factorial":
                n = fn
                while n > 1:
                    n = n - 1
                    fn = fn * n
                rt = fn
            print (rt)
        #two digit calculation
        if nn  > "1" and  nn < "4":
            if nn  == "2" :
                question2= input("""What calculation would you like to execute?
                   A= Plus/Minus/For/Divided
                   B= Percent    \n""")
        #Plus/Minus/For/Divided
                if question2.lower() == "A" or question2.lower() == "a":
                    fn = float(input("1° number :   "))
                    fop = input("1° operator(+-*/) :   ")
                    sn = float(input("2° number :   "))
                    if fop == "*" : rt = fn * sn
                    if fop == "/" : rt = fn / sn
                    if fop == "+" : rt = fn + sn 
                    if fop == "-" : rt = fn - sn
        #Percent
                if question2.lower() == "B" or question2.lower() == "b":
                    fn = float(input("1° number :   "))
                    sn = float(input("2° number :   "))
                    rt = sn / 100 * fn
                
        #three digit calculation
            if nn == "3" : 
                fn = float(input("1° number :   "))
                fop = input("1° operator(+-*/) :   ")
                sn = float(input("2° number :   "))
                if fop == "*" : rt = fn * sn
                if fop == "/" : rt = fn / sn
                if fop == "+" : rt = fn + sn 
                if fop == "-" : rt = fn - sn
                sop = input("2° operator(+-*/) :   ")
                tn = float(input("3° number :   "))
                print(fn , fop , sn , sop , tn )
                if sop == "*" or sop == "/" : 
                    if sop == "*" : pzr = sn * tn 
                    if sop == "/" : pzr = sn / tn 
                    if fop == "*" : rt = fn * pzr
                    if fop == "/" : rt = fn / pzr
                    if fop == "+" : rt = fn + pzr 
                    if fop == "-" : rt = fn - pzr

                else:
                    if fop == "*" : pzr = fn * sn
                    if fop == "/" : pzr = fn / sn
                    if fop == "+" : pzr = fn + sn 
                    if fop == "-" : pzr = fn - sn
                    if sop == "+" : rt = pzr + tn 
                    if sop == "-" : rt = pzr - tn
            print(rt)
    if question0.lower() == "b" or question0.lower() == "B" :
        question3= input("""What calculation would you like to execute?
                        A: Sfere
                        B: Cube
                        C: Piramid
                        D: Rectangle \n """)
        if question3.lower() == "a" or question3.lower() == "A" :
            question4= input("""What calculation would you like to execute?
                            A: Circunference (Circle)
                            B: Volume
                            C: Surface \n """)
            if question4.lower() == "a" or question4.lower() == "A" :   
                    fn = float(input("Radious :   "))
                    rt = fn * 6.283185307
                    print(rt)
            if question4.lower() == "b" or question4.lower() == "B" :   
                    fn = float(input("Radious :   "))
                    rt = fn * fn * fn * 4.1887902048
                    print(rt)
            if question4.lower() == "c" or question4.lower() == "C" :
                    fn = float(input("Radious :   "))
                    rt = 12.566370614 * fn * fn
                    print(rt)
            
        if question3.lower() == "b" or question3.lower() == "B" :
            question5= input("""What calculation would you like to execute?
                            A: Perimetre (Square)
                            B: Volume
                            C: Surface \n """)
            if question5.lower() == "a" or question5.lower() == "A" :   
                    fn = float(input("Square side :   "))
                    rt = fn * 4
                    print(rt)
            if question5.lower() == "b" or question5.lower() == "B" :   
                    fn = float(input("Square side :   "))
                    rt = fn * fn * fn
                    print(rt)
            if question5.lower() == "c" or question5.lower() == "C" :
                    fn = float(input("Square side :   "))
                    rt = fn * fn * 6
                    print(rt)

        if question3.lower() == "c" or question3.lower() == "C" :
            question5= input("""What calculation would you like to execute?
                            A: Perimetre (Triangle)
                            B: Volume
                            C: Surface \n """)
            if question5.lower() == "a" or question5.lower() == "A" :   
                    fn1 = float(input("Base side A :   "))
                    fn2 = float(input("Base side B :   "))
                    sn = float(input("High :   "))
                    pzr1a = fn1 * fn1    
                    pzr1b = sn * sn + pzr1a
                    rt1a = math.sqrt(pzr1b)   
                    pzr2a = fn2 * fn2 
                    pzr2b = sn * sn + pzr2a
                    rt1b = math.sqrt(pzr2b)
                    rt = rt1b + rt1a + fn1 + fn2 
                    print(rt)
            if question5.lower() == "b" or question5.lower() == "B" :   
                    fn1 = float(input("Base side A :   "))
                    fn2 = float(input("Base side B :   "))
                    fn3 = float(input("Base side lateral :   "))
                    sn = float(input("High :   "))
                    pzra = sn * sn 
                    pzrb = fn1 * fn1
                    pzrc = pzra - pzrb 
                    rt1 = math.sqrt(pzrc) 
                    rt2 = fn1 + fn2 
                    rt3 = rt2 * fn3 
                    rt = rt3 * rt1 / 3
                    print(rt)
            if question5.lower() == "c" or question5.lower() == "C" :
                    fn1a = float(input("Base side A  :  "))
                    fn1c = float(input("High A  :  "))
                    fn2a = float(input("Base side B :   "))
                    fn2c = float(input("High A  :  "))
                    fn3a = float(input("Base side C :   "))
                    fn3c = float(input("High A  :  "))
                    fn4a = float(input("Base side D :   "))
                    fn4c = float(input("High A  :  "))
                    pzr1 = fn1a * fn1c / 2
                    pzr2 = fn2a * fn2c / 2
                    pzr3 = fn3a * fn3c / 2
                    pzr4 = fn4a * fn4c / 2
                    pzr5 = fn1a * fn2a 
                    rt = pzr1 + pzr2 + pzr3 + pzr4 + pzr5
                    print(rt)
        if question3.lower() == "d" or question3.lower() == "D" :
            question5= input("""What calculation would you like to execute?
                            A: Perimetre (Rectangle)
                            B: Volume
                            C: Surface \n """)
            if question5.lower() == "a" or question5.lower() == "A" :   
                    fn1 = float(input("Rectangle side A :   "))
                    fn2 = float(input("Rectangle side B :   "))
                    pzr1 = fn1 * 2
                    pzr2 = fn2 * 2
                    rt = pzr1 + pzr2
                    print(rt)
            if question5.lower() == "b" or question5.lower() == "B" :   
                    fn1 = float(input("Rectangle side A :   "))
                    fn2 = float(input("Rectangle side B :   "))
                    sn = float(input("High :   "))
                    rt = fn1 * fn2 *sn
                    print(rt)
            if question5.lower() == "c" or question5.lower() == "C" :
                    fn1 = float(input("Rectangle side A :   "))
                    fn2 = float(input("Rectangle side B :   "))
                    sn = float(input("High :   "))
                    pzr1 = fn1 * fn2 * 2
                    pzr2 = fn1 * sn * 2
                    pzr3 = fn2 * sn * 2 
                    rt = pzr1 + pzr2 + pzr3
                    print(rt)

        

                    
                
           
nn = input("How many numbers will your calculation have?   \n")           
if nn == "2": print(fn , fop , sn )
if nn == "3": print(fn , fop , sn , sop , tn )
print("Closing the Calculator...")
time.sleep(3)
exit()
