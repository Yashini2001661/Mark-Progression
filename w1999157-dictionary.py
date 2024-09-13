#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other source is referenced within my code solution


#Student ID:20220168/w1999157

#Date:20/04/2023

credit_pass=0
credit_defer=0
credit_fail=0

my_dictionary={}
Loop="y"
while True:
    if Loop=="y":
        student_id=input("Enter your student id:").lower()
        if len(student_id)==8 and student_id[0] == "w" and student_id[1:7].isdigit():
            if student_id not in my_dictionary:
                my_dictionary[student_id]={}
            else:
                print("student id already exist" "\n")
                continue
        else:
                print("invalid student id then try again")
                continue
            
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
                credit_defer+int(input("Enter your total DEFER credits:"))
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
            print("total is incorrect")
        elif(credit_pass==120):

            my_dictionary[student_id]=(": progress-"+str(credit_pass)+","+str(credit_defer)+","+str(credit_fail))
            print("progress")
        elif(credit_pass==100):

            my_dictionary[student_id]=(":progress (module trailer)-"+str(credit_pass)+","+str(credit_defer)+","+str(credit_fail))
            print("progress (module trailer)")
        elif(credit_fail>=80):

            my_dictionary[student_id]=(":exclude-"+str(credit_pass)+","+str(credit_defer)+","+str(credit_fail))
            print("exclude")
        else:

            my_dictionary[student_id]=(":module retriever-"+str(credit_pass)+","+str(credit_defer)+","+str(credit_fail))
            print("do not progress (module retriever)")

        print("would you like to enter another set of data?")

    elif Loop == "q":

         break
    else:
        print("invalid input")
        print("read instructions agaim")
    Loop=input("Enter 'y' for yes or 'q' to quit and view results:")
    print('-------------------------------------------------------')


for i,y in my_dictionary.items():
    print(i,y)
            

                    
                                                                                    
