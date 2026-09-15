Question 3 : Find the letter count for a String 

Answer: 
def letter_count(s):
    a={}

    for i in s :
        a[i]=a.get(i,0)+1
    print(a)

if __name__ == '__main__' :
    print(letter_count("Parnab"))
    print(letter_count("Sayan"))
