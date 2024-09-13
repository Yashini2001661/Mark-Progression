#I declare that my work contains no examples of miscounduct, such as plagiarism, or collusion.
#Any code taken from other sources is refeerenced within my code solution.


#Student ID: 20220168/w1999157

#Date:20/04/2023

progress_students=0
trailing_students=0
excluding_students=0
retrievering_students=0
total_credits=0
progress_outcomes=0
module_trailer_outcomes=0
exclude_outcomes=0
module_retriever_outcomes=0
Loop="y"
i=0
count=0
List=[]

#Start the program
def progress_outcomes():
    print("progress")
    global progress_students
    progress_students+=1
    List.append("Progress-"+str(credit_pass)+","+str(credit_defer)+","+str(credit_fail))
    return progress_students
def module_trailer_outcomes():
    print("progress(module trailer)")
    global trailing_students
    trailing_students +=1
    List.append("Progress(module trailer)-"+str(credit_pass)+","+str(credit_defer)+","+str(credit_fail))
    return trailing_students
def exclude_outcomes():
    print("exclude")
    global excluding_students
    excluding_students+=1
    List.append("exclude-"+str(credit_pass)+","+str(credit_defer)+","+str(credit_fail))
    return excluding_students
def module_retrevier_outcomes():
    print("do not progress-module retriever")
    global retrievering_students
    retrievering_students+=1
    List.append("module retriever-"+str(credit_pass)+","+str(credit_defer)+","+str(credit_fail))
    return retrievering_students

#Define a function to validate the credit inputs
while True:
    if Loop =='y':
        while True:
            try:
                credit_pass=int(input("Enter your total PASS credits:"))
                if credit_pass not in range (0,121,20):
                    print("out of range")
                    continue                   
            except ValueError:
                    print("integer required")
                    continue
            break

        while True:
            try:
                credit_defer=int(input("Enter your total DEFER credits:"))
                if credit_defer not in range (0,121,20):
                    print("out of range")
                    continue               
            except ValueError:
                    print("integer required")
                    continue
            break
            
        while True:
            try:
                credit_fail=int(input("Enter your total FAIL credits:"))
                if credit_fail not in range (0,121,20):
                     print("out of range")
                     continue                    
            except ValueError:
                    print("integer required")
                    continue
            break
                
        total_credits= credit_pass + credit_defer + credit_fail
        
        if total_credits!=120:
            print("Total is incorrect")
        elif (credit_pass==120):
            progress_outcomes()
        elif (credit_pass==100):
            module_trailer_outcomes()
        elif (credit_fail>=80):
            exclude_outcomes()
        else:
            module_retrevier_outcomes()
            

        print("Would you like to enter another set of data?")
            

    elif Loop =='q':
        file=open("Output.txt",'w')
        for i in range(len(List)):
            file.write(List[i])
            file.write('\n')
        file.close()
        break
    else:
        print("invalid input")
        print("Read instructions again\n")
    Loop=input("Enter 'y' for yes or 'q' to quit and view results:")
    print('-------------------------------------------------------')
    
#Define a function to print the histogram    
print("Histogram")
print("rogress",progress_students,"   :",end='')
print('*'*progress_students,end='')
print()
print("trailer",trailing_students,"    :",end='')
print('*'*trailing_students,end='')
print()
print("retriever",retrievering_students,"  :",end='')
print('*'*retrievering_students,end='')
print()
print("excluded",excluding_students,"   :",end='')
print('*'*excluding_students,end='')
print()
print()
count=progress_students+trailing_students+retrievering_students+excluding_students
print(count,"outcomes in total")
print('--------------------------------------------------------------------------')

for i in List:
    print(i)
    

