import csv

def write_data(data_list):
    with open('student_database.csv','a',newline = '') as f:
        mywriter = csv.writer(f,delimiter = ',')
        if f.tell() == 0:
            mywriter.writerow(['Name','Age','Phone','E-mail'])
        mywriter.writerow(data_list)

def Enter():
    running = True
    stud_num = 1
    
    while running:
        data_list = eval(input('Enter info in the format [Name,Age,Phone No.,Email]: '))
        print()
        print(('''The entered information is:
Name: {}
Age: {}
Phone: {}
E-mail: {}''').format(data_list[0],data_list[1],data_list[2],data_list[3]))
        print()
        choice = input("Is the entered information correct? (yes/no) ")
        print()
        if choice == 'yes':
            write_data(data_list)

            cont = input('Enter (yes/no) if you want to enter details of another student: ')
            print()
            if cont == 'yes':
                running = True
                stud_num += 1
            elif cont == 'no':
                running = False
        elif choice == 'no':
            print('Please re-enter the details: ')
            print()

def View():
    with open('student_database.csv','r',newline = '') as f:
        myreader = csv.reader(f,delimiter = ',')
        for row in myreader:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3])
        print()

while True:
    option = int(input('''Choose option numbers required:
1. Enter student details
2. View student database
3. Exit '''))
    print()
    
    if option == 1:
        Enter()
    elif option == 2:
        View()
    elif option == 3:
        print('Thank you for using our services.')
        break
    else:
        print('Please enter valid option.')
        print()
        
#Thank you MyCaptain Team!
