import math









#Operations with triangles


def acuteAmbig():
  print("")
  


def trignometricRatios():
  print("")
  print("Pick an option")
  print("")
  print("1. Calculate trignometric ratios from angle")
  print("2. Calculate trinometric ratios of sides respective to an angle \u03F4")
  print("")
  choice=int(input("Pick the number for the operation you would like to do: "))
  if choice==1:
    trigRatioFromAngle()
  elif choice==2:
    trigRatio()
  else:
    print("That is not a valid choice")



def trigRatio():
  Opposite=float(input("What is the length of the side Opposite to \u03F4: "))
  Adjacent=float(input("What is the length of the side Adjacent to \u03F4: "))
  Hypotenuse=float(input("What is the length of the Hypotenuse: "))
  Sine=float(Opposite/Hypotenuse)
  Cosine=float(Adjacent/Hypotenuse)
  Tangent=float(Opposite/Adjacent)
  Cosecant=float(1/Sine)
  Secant=float(1/Cosine)
  Cotangent=float(1/Tangent)
  print("")
  print("                 Trignometric Ratio Values                ")
  print("          +--------------------------------------+")
  print("          +   Sin(\u03F4)= {:.2f}        Csc(\u03F4)= {:.2f}   +".format(Sine,Cosecant))
  print("          +                                      +")
  print("          +   Cos(\u03F4)= {:.2f}        Sec(\u03F4)= {:.2f}   +".format(Cosine,Secant))
  print("          +                                      +")
  print("          +   Tan(\u03F4)= {:.2f}        Cot(\u03F4)= {:.2f}   +".format(Tangent,Cotangent))
  print("          +--------------------------------------+")
  print("")




def trigRatioFromAngle():
  AngleMeasurement=float(input("enter the angle measurement in degrees: "))
  AngleMeasurement=(AngleMeasurement*math.pi)/180

  Sine=float(math.sin(AngleMeasurement))
  Cosine=float(math.cos(AngleMeasurement))
  Tangent=float(math.tan(AngleMeasurement))
  Cosecant=float(1/Sine)
  Secant=float(1/Cosine)
  Cotangent=float(1/Tangent)

  print("")
  print("                 Trignometric Ratio Values                ")
  print("          +--------------------------------------+")
  print("          +   Sin(\u03F4)= {:.2f}        Csc(\u03F4)= {:.2f}   +".format(Sine,Cosecant))
  print("          +                                      +")
  print("          +   Cos(\u03F4)= {:.2f}        Sec(\u03F4)= {:.2f}   +".format(Cosine,Secant))
  print("          +                                      +")
  print("          +   Tan(\u03F4)= {:.2f}        Cot(\u03F4)= {:.2f}   +".format(Tangent,Cotangent))
  print("          +--------------------------------------+")
  print("")





def trianglePerimeter():
  sideA=int(input("what is the length of side 1: "))
  sideB=int(input("what is the length of side 2: "))
  sideC=int(input("what is the length of side 3: "))
  perimeter=sideA+sideB+sideC
  print("the perimeter of the triangle is "+ str(perimeter)+ " (don't forget the units!!)")



def triangleArea():

    base=input("enter the length of the base ")
    height=input("enter the height ")
    area=(float(base)*float(height))/2
    print("The area of this triangle is {:.2f} (don't forget units\u00b2)".format(area))




def herons():
    a=input("enter the length of side A: ")
    b=input("enter the length of side B: ")
    c=input("enter the length of side C: ")
    s=(float(a)+float(b)+float(c))/2
    area=(s*(s-float(a))*(s-float(b))*(s-float(c)))**(1/2)
    print("The area of this triangle is {:.2f} (don't forget units\u00b2)".format(area))



def triangleAreaOperations():

  print("Which method would you like to use to calculate the area?")
  print("1. Traditional area method")
  print("2. Heron's formula")
  choice=input("enter a number for your choice: ")

  if int(choice)==1:
    triangleArea()
  elif int(choice)==2:
    herons()
  else:
    print("sorry this is not a valid choice")
    
def triangles():
    print("Pick the number for the triangle operation you would like to perform")
    print("1.Trignometric ratios")
    print("2.Area")
    print("3.perimeter")
    print("")
    choice=int(input("Pick the number for the operation you would like to do: "))
    if choice==1:
      trignometricRatios()
    elif choice==2:
      triangleAreaOperations()
    elif choice==3:
      trianglePerimeter()
    else:
      print("That is not a valid option")


#close operations with triangles