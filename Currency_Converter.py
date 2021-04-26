import time
print ("Welcome to the currency converter.")
time.sleep (1)
Choice1 = input ("What currency would you like to convert from? (JPY, GBP, USD, EUR, RUP) ")

if Choice1 == "JPY":
  
  JPY = float(input("Input your amount in Yen. ¥"))
  GBP = (JPY * 0.0068)
  USD = (JPY * 0.008)
  EUR = (JPY * 0.0081)
  RUP = (JPY * 1.41)
  Choice2 = input("Do you want that in GBP, USD, EUR or RUP? ")

  if Choice2 == "GBP":
    print ("¥",JPY, "is equal to:")
    print ("£", GBP)
  
  elif Choice2 == "USD":
    print ("¥",JPY, "is equal to:")
    print ("$", USD)
    
  elif Choice2 == "EUR":
    print ("¥",JPY, "is equal to:")
    print ("€", EUR)
    
  elif Choice2 == "KRW":
    print ("¥",JPY, "is equal to:")
    print ("₹", RUP)
    
############################################################################
elif Choice1 == "GBP":

  GBP = float(input("Input your amount in Pounds. £"))
  JPY = (GBP * 146.56)
  USD = (GBP * 1.2898)
  EUR = (GBP * 1.1092)
  RUP = (GBP * 96.1069)
  Choice2 = input("Do you want that in JPY, USD, EUR or RUP? ")

  if Choice2 == "JPY":
    print ("£",GBP, "is equal to:")
    print ("¥", JPY)
  
  elif Choice2 == "USD":
    print ("£",GBP, "is equal to:")
    print ("$", USD)
    
  elif Choice2 == "EUR":
    print ("£",GBP, "is equal to:")
    print ("€", EUR)
    
  elif Choice2 == "RUP":
    print ("£",GBP, "is equal to:")
    print ("₹", RUP)
    
############################################################################
elif Choice1 == "USD":

  USD = float(input("Input your amount in Dollars. $"))
  JPY = (USD * 113.76)
  GBP = (USD * 0.78)
  EUR = (USD * 0.92)
  RUP = (USD * 74.48)
  Choice2 = input("Do you want that in JPY, GBP, EUR or RUP? ")

  if Choice2 == "JPY":
    print ("$",USD, "is equal to:")
    print ("¥", JPY)
  
  elif Choice2 == "GBP":
    print ("$",USD, "is equal to:")
    print ("£", GBP)
    
  elif Choice2 == "EUR":
    print ("$",USD, "is equal to:")
    print ("€", EUR)
    
  elif Choice2 == "RUP":
    print ("$",USD, "is equal to:")
    print ("₹", RUP)
    
############################################################################
elif Choice1 == "EUR":

  EUR = float(input("Input your amount in Euros. €"))
  JPY = (EUR * 123.67)
  GBP = (EUR * 0.84)
  USD = (EUR * 1.09)
  RUP = (EUR * 86.65)
  Choice2 = input("Do you want that in JPY, GBP, USD or RUP? ")

  if Choice2 == "JPY":
    print ("€",EUR, "is equal to:")
    print ("¥", JPY)
  
  elif Choice2 == "GBP":
    print ("€",EUR, "is equal to:")
    print ("£", GBP)
    
  elif Choice2 == "USD":
    print ("€",EUR, "is equal to:")
    print ("$", USD)
    
  elif Choice2 == "RUP":
    print ("€",EUR, "is equal to:")
    print ("₹", RUP)
    
############################################################################
elif Choice1 == "RUP":

  RUP = float(input("Input your amount in Rupees. ₹"))
  JPY = (RUP * 1.40729)
  GBP = (RUP * 0.0104)
  USD = (RUP * 0.01342)
  EUR = (RUP * 0.01154)
  Choice2 = input("Do you want that in JPY, GBP, USD or EUR? ")

  if Choice2 == "JPY":
    print ("₹",RUP, "is equal to:")
    print ("¥", JPY)
  
  elif Choice2 == "GBP":
    print ("₹",RUP, "is equal to:")
    print ("£", GBP)
    
  elif Choice2 == "USD":
    print ("₹",RUP, "is equal to:")
    print ("$", USD)
    
  elif Choice2 == "EUR":
    print ("₹",RUP, "is equal to:")
    print ("€", EUR)
