from python_with_mysql import DBHelper

def main():

    while True:
        db = DBHelper()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice = int(input())
            if choice == 1:
                #insert user
                id = int(input("Enter UserId:"))
                name = input("Enter Username:")
                phone = input("Enter user phone:")
                db.insert_into(id , name, phone)
            elif choice == 2:
                #display
                db.fetch_all()
            elif choice == 3:
                #delete
                id = int(input("Which UserId you want to delete:"))
                db.delete_record(id)
            elif choice == 4:
                #update
                id = int(input("Which userid you want to update"))
                newName = input("Enter the new name:")
                newPhone = input("Enter the new phone")
                db.update_table(id, newName, newPhone)
            elif choice == 5:
                break
            else:
                print("Invalid input! Try again")
        except Exception as e:
            print(e)
            print("Invalid Details! Try again")

if __name__ == '__main__':
    main()






