import csv
print('Choose either Make new quiz as Make:')
print('Choose either Attempt existing quiz as Attempt:')
print('Choose either Edit existing quiz as Edit:')
option=input()
if option=='Make':
    if type=='Fun':
        path="D:\Personals\Progess\Python Project\STUDY\ "
        name=input('Enter file name.csv')
        path=path+name
        file=open(path,'w',newline='')
        questions = []
        for i in range(15):
            print(f"Question {i+1}:")
            q = input("Enter question: ")
            a = input("Option A: ")
            b = input("Option B: ")
            c = input("Option C: ")
            d = input("Option D: ")
            questions.append([q, a, b, c, d])
        writer = csv.writer(file)
        print("Now enter result messages for each option:")
        result_A = input("Message if user chooses mostly A: ")
        result_B = input("Message if user chooses mostly B: ")
        result_C = input("Message if user chooses mostly C: ")
        result_D = input("Message if user chooses mostly D: ")
        l=[result_A,result_B,result_C,result_D]
        questions.append(l)
        writer.writerows(questions)
        print("All questions saved successfully")
        file.close()
    elif type=='Study':
        path="D:\Personals\Progess\Python Project\STUDY\ "
        name=input('Enter file name.csv')
        path=path+name
        file=open(path,'w',newline='')
        n = int(input("Enter number of questions: "))
        questions=[]
        for i in range(n):
            print(f"Question {i+1}:")
            q = input("Enter question: ")
            o1 = input("Option 1: ")
            o2 = input("Option 2: ")
            o3 = input("Option 3: ")
            o4 = input("Option 4: ")
            ans = input("Enter correct option: ")
            l=[q,o1,o2,o3,o4,ans]
            questions.append(l)
        writer = csv.writer(file)
        writer.writerows(questions)
        print("All questions saved successfully")
        file.close()
    else:
        print('INVALID CHOICE')
elif option=='Attempt':
    if type=='Study':
        path="D:\Personals\Progess\Python Project\STUDY\ "
        name=input('Enter file name.csv')
        path=path+name
        file=open(path,'r')
        correct = 0
        incorrect = 0
        not_attempted = 0
        total = 0
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 6:
                continue
            question = row[0]
            options = row[1:5]
            answer = row[5].strip().upper()
            print("\nQuestion:", question)
            print(f"A) {options[0]}")
            print(f"B) {options[1]}")
            print(f"C) {options[2]}")
            print(f"D) {options[3]}")
            user_ans = input("Enter your answer (A/B/C/D or space to skip): ").strip().upper()
            if user_ans == "":
                not_attempted += 1
            elif user_ans == answer:
                correct += 1
            else:
                incorrect += 1
            total += 1
        print("\n--- Quiz Summary ---")
        print("Total Questions:", total)
        print("Correct Answers:", correct)
        print("Incorrect Answers:", incorrect)
        print("Not Attempted:", not_attempted)
        if total > 0:
            accuracy = (correct / total) * 100
            print(f"Accuracy: {accuracy:.2f}%")
        file.close()
    elif type =='Fun':
        path="D:\Personals\Progess\Python Project\FUN\ "
        name=input('Enter file name.csv')
        path=path+name
        f=open(path,'r')
        reader = csv.reader(f)
        data = list(reader)
        print("\nWelcome to the Fun Quiz!\n")
        count_a = count_b = count_c = count_d = 0
        for i in range(15):
            print(f"\nQ{i+1}: {data[i][0]}")
            print(f"a) {data[i][1]}")
            print(f"b) {data[i][2]}")
            print(f"c) {data[i][3]}")
            print(f"d) {data[i][4]}")
            ans = input("Your answer (a/b/c/d): ").lower().strip()
            if ans == 'a':
                count_a += 1
            elif ans == 'b':
                count_b += 1
            elif ans == 'c':
                count_c += 1
            elif ans == 'd':
                count_d += 1
            else:
                print('Invalid choice')
        max_count = max(count_a, count_b, count_c, count_d)
        if max_count == count_a:
            result = "Option A personality/result!"
        elif max_count == count_b:
            result = "Option B personality/result!"
        elif max_count == count_c:
            result = "Option C personality/result!"
        else:
            result = "Option D personality/result!"
        print("Your result:", result)
        f.close()
    else:
        print('INVALID CHOICE')
elif option=='Edit':
    type=input()
    if type=='Fun':
        path="D:\Personals\Progess\Python Project\FUN\ "
        name=input('Enter file name.csv')
        path=path+name
        f=open(path,'r')
        change=input('Change questions as q or option description as o')
        c=csv.reader
        l=list(c)
        if change=='q':
            num=int(input('Enter the question number to be corrected'))
            q=input('Enter the question:')
            a=input('Option 1:')
            b=input('Option 2:')
            c=input('Option 3:')
            d=input('Option 4:')
            lf=[num,q,a,b,c,d,ans]
            l[num-1]=lf
        elif change=='o':
            num=int(input('Enter option number'))
            op='Option'+num+' :'
            des=input('Enter the description:')
            lf=[op,des]
            l[num-5]=lf
        else:
            print('INVALID CHOICE')
        f.close()
        f=open(path,'w')
        c=csv.writer
        c.writerows(l)
        f.close()
    elif type=='Study':
        path="D:\Personals\Progess\Python Project\STUDY\ "
        name=input('Enter file name.csv')
        path=path+name
        f=open(path,'r')
        c=csv.reader
        l=list(c)
        num=int(input('Enter the question number to be corrected'))
        q=input('Enter the question:')
        a=input('Option 1:')
        b=input('Option 2:')
        c=input('Option 3:')
        d=input('Option 4:')
        ans=input('Answer:')
        lf=[num,q,a,b,c,d,ans]
        l[num-1]=lf
        f.close()
        f=open(path,'w')
        c=csv.writer
        c.writerows(l)
        f.close()
    else:
        print('INVALID CHOICE')
else:
    print('INVALID CHOICE')
    
