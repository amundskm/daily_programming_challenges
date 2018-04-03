""" A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers. """

import math



def main():
    # The Largest possible product of two 3-digit numbers is 999 X 999.
    largeProduct = 999 * 999
    #print("largestProduct = %d" % (largeProduct))

    # Working backwards from largeProduct, we can find a palindrome number.
    productsFound = False
    while productsFound == False:
        for testProduct in range(largeProduct, 0, -1):
            testStr = str(testProduct)
            #print(len(testStr) /2)
            #print(testStr[math.floor(len(testStr) /2):])
            #print(testStr[:math.floor(len(testStr) /2) - 1:-1])
            
            # Determine if number is palindrome
            if (testStr[:math.floor(len(testStr) / 2)] == testStr[:math.floor(len(testStr) /2) - 1:-1]
                or testStr[: math.floor(len(testStr) / 2)] == testStr[:math.floor(len(testStr) /2):-1]):
                productsFound = checkProduct(testStr)
                if productsFound == True:
                    break
                


                
  
def checkProduct(palStr):
    # check if palindrom has two 3-digit products

    palInt = int(palStr)
    productPairs = []
    top = palInt
    bottom = 100

    while top > math.sqrt(palInt):
        if palInt % bottom == 0:
            top = palInt / bottom
            if top >= 100 and bottom >= 100 and top <= 999 and bottom <= 999:
                print("%d X %d = %d" % (top, bottom, palInt))
                return  True
        bottom += 1

    return False

        

        
main()