import mysql.connector

from datetime import date

sql_connection = mysql.connector.connect(
       host='localhost', database='library', user='root', password='Sanskriti123')
sql_cursor = sql_connection.cursor()

import os

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def wait_for_user():
   further = input('\n---------- Press Any Key To Continue ----------\n\n')


def add_book():
  title = input('\nEnter Book Title : ')
  author = input('Enter Book Author : ')
  publisher = input('Enter Book Publisher : ')
  pages = input('Enter Number of Pages : ')
  price = input('Enter Book Price : ')
  edition = input('Enter Book Edition : ')
  sql_query = 'insert into book(title,author,price,pages,publisher,edition,status) values ( "' + \
       title + '","' + author+'",'+price+','+pages+',"'+publisher+'","'+edition+'","available");'
  sql_cursor.execute(sql_query)
  sql_connection.commit()
  print('\nYour book added successfully!')
  wait_for_user()


def add_user():
  name = input('\nEnter User\'s Name : ')
  user_class = input('Enter User\'s Class : ')
  address = input('Enter User\'s Address : ')
  phone = input('Enter User\'s Phone : ')
  email = input('Enter User\'s Email : ')
  sql_query = 'insert into user(name,class,address,phone,email) values ( "' + \
      name + '","' + user_class+'","'+address+'","'+phone + \
        '","'+email+'");'
  sql_cursor.execute(sql_query)
  sql_connection.commit()
  print('\nNew user added successfully!')
  wait_for_user()


def modify_book():
    clean_screen()
    print('----------   MODIFY BOOK DETAILS SCREEN   ----------')
    print('\n1. Book Title')
    print('2. Book Author')
    print('3. Book Publisher')
    print('4. Book Pages')
    print('5. Book Price')
    print('6. Book Edition')
    print('\n')
    choice = int(input('Please enter your choice : '))
    selected_field = ''
    if choice == 1:
      selected_field = 'title'
    if choice == 2:
      selected_field = 'author'
    if choice == 3:
      selected_field = 'publisher'
    if choice == 4:
      selected_field = 'pages'
    if choice == 5:
      selected_field = 'price'
    if selected_field == '':
       print("\nPlease select valid choice\n\n")
       return
    book_id = input('Enter Book ID : ')
    value = input('Enter new value for the selected field : ')
    if selected_field =='pages' or selected_field == 'price':
        sql_query = 'update book set ' + selected_field + ' = '+value+' where id = '+book_id+';'
    else:
        sql_query = 'update book set ' + selected_field + ' = "'+value+'" where id = '+book_id+';'
    sql_cursor.execute(sql_query)
    print('\nBook details successfully updated!')
    sql_connection.commit()
    wait_for_user()


def modify_user():
    clean_screen()
    print('----------   MODIFY USER DETAILS SCREEN   ----------')
    print('\n1. Name')
    print('2. Class')
    print('3. Address')
    print('4. Phone')
    print('5. Email')
    print('\n')
    choice = int(input('Please enter your choice : '))
    selected_field =''
    if choice == 1:
      selected_field ='name'
    if choice == 2:
      selected_field = 'class'
    if choice ==3:
      selected_field ='address'
    if choice == 4:
      selected_field = 'phone'
    if choice == 5:
      selected_field = 'email'
    if selected_field == '':
       print("\nPlease select valid choice\n")
       return
    mem_id =input('Enter user ID : ')
    value = input('Enter new value for the selected field : ')
    sql_query = 'update user set '+ selected_field +' = "'+value+'" where id = '+mem_id+';'
    sql_cursor.execute(sql_query)
    print('User details successfully updated!')
    sql_connection.commit()
    wait_for_user()


def user_issue_status(user_id):
    sql_query ='select * from record where user_id ='+user_id +' and date_return is NULL;'
    sql_cursor.execute(sql_query)
    results = sql_cursor.fetchall()
    return results


def book_status(book_id):
    sql_query = 'select * from book where id ='+book_id + ';'
    sql_cursor.execute(sql_query)
    result = sql_cursor.fetchone()
    return result[5]


def book_issue_status(book_id,user_id):
    sql_query = 'select * from record where book_id ='+book_id + ' and user_id ='+ user_id +' and date_return is NULL;'
    sql_cursor.execute(sql_query)
    result = sql_cursor.fetchone()
    return result


def issue_book():
    clean_screen()
    print('----------   BOOK ISSUE SCREEN   ----------')
    book_id = input('\nEnter Book ID : ')
    user_id  = input('Enter User ID : ')
    book_status_result = book_status(book_id)
    user_isuue_status_result = user_issue_status(user_id)
    today = date.today()
    if len(user_isuue_status_result) == 0:
      if book_status_result == 'available':
          sql = 'insert into record(book_id, user_id, date_issue) values('+book_id+','+user_id+',"'+str(today)+'");'
          sql_book = 'update book set status="issue" where id ='+book_id + ';'
          sql_cursor.execute(sql)
          sql_cursor.execute(sql_book)
          print('\nYour book is issued successfully!')
      else:
          print('\nBook is not available at the moment... Current status :',book_status_result)
    else:
        print('\nUser has already issued a book from the library!')
    sql_connection.commit()
    wait_for_user()


def return_book():
    library_fine_per_day = 2  
    clean_screen()
    print('----------   BOOK RETURN SCREEN   ----------')
    book_id = input('\nEnter Book ID : ')
    user_id = input('Enter User ID : ')
    today =date.today()
    book_issue_status_result = book_issue_status(book_id,user_id)
    if book_issue_status_result ==None:
       print('Book is not issued...Please check the Book Id and User ID again..')
    else:
       sql_query='update book set status ="available" where id ='+book_id +';'
       book_issued_days = (today - book_issue_status_result[3]).days
       fine = book_issued_days * library_fine_per_day
       sql_query1 = 'update record set date_return ="'+str(today)+'" , fine='+str(fine)+' where book_id='+book_id +' and user_id='+user_id+' and date_return is NULL;' 
       sql_cursor.execute(sql_query)
       sql_cursor.execute(sql_query1)
       print('\nYour book is returned successfully!')
    sql_connection.commit()
    wait_for_user()


def search_book(field):
    clean_screen()
    print('----------   BOOK SEARCH SCREEN   ----------')
    msg ='\nEnter '+ field +' Value : '
    title = input(msg)
    sql_query ='select * from book where '+ field + ' like "%'+ title+'%"'
    sql_cursor.execute(sql_query)
    records = sql_cursor.fetchall()
    clean_screen()
    print('Search result for :',field,' :' ,title)
    print('-'*120)
    for record in records:
      print(record)
    sql_connection.commit()
    wait_for_user()


def search_menu():
    while True:
      clean_screen()
      print('----------   SEARCH   MENU   ----------')
      print("\n1.  Book Title")
      print('2.  Book Author')
      print('3.  Book Publisher')
      print('4.  Exit to Main Menu')
      print('\n')
      choice = int(input('Please enter your choice: '))
      print('\n')
      selected_field =''
      if choice == 1:
        selected_field ='title'
      if choice == 2:
        selected_field = 'author'
      if choice == 3:
        selected_field = 'publisher'
      if choice == 4:
        break
      if selected_field == '':
       print("\nPlease select valid choice")
       return
      search_book(selected_field)


def report_book_list():
    clean_screen()
    print('----------   REPORT BOOK TITLES   ----------')
    sql_query ='select * from book'
    sql_cursor.execute(sql_query)
    records = sql_cursor.fetchall()
    for record in records:
       print(record)
    sql_connection.commit()
    wait_for_user()


def report_issued_books():
    clean_screen()
    print('----------   REPORT BOOK TITLES ISSUED   ----------')
    sql_query = 'select * from book where status = "issue";'
    sql_cursor.execute(sql_query)
    records = sql_cursor.fetchall()
    for record in records:
       print(record)
    sql_connection.commit()
    wait_for_user()


def report_available_books():
    clean_screen()
    print('----------   REPORT BOOK TITLES AVAILABLE   ----------')
    sql_query = 'select * from book where status = "available";'
    sql_cursor.execute(sql_query)
    records = sql_cursor.fetchall()
    for record in records:
       print(record)
    sql_connection.commit()
    wait_for_user()


def report_user_list():
    clean_screen()
    print('----------   REPORT USERS LIST   ----------')
    sql_query = 'select * from user'
    sql_cursor.execute(sql_query)
    records = sql_cursor.fetchall()
    for record in records:
       print(record)
    sql_connection.commit()
    wait_for_user()


def report_menu():
    while True:
      clean_screen()
      print('----------   REPORT  MENU   ----------')
      print("\n1.  Book List")
      print('2.  User List')
      print('3.  Issued Books')
      print('4.  Available Books')
      print('5.  Exit to main Menu')
      print('\n')
      choice = int(input('Please enter your choice : '))
      print('\n')
      if choice == 1:
        report_book_list()
      if choice == 2:
        report_user_list()
      if choice == 3:
        report_issued_books()
      if choice == 4:
        report_available_books()
      if choice == 5:
        break


def main_menu():
    while True:
      clean_screen()
      print('----------   LIBRARY MENU   ----------')
      print("\n1.  Add Books")
      print('2.  Add User')
      print('3.  Modify Book Information')
      print('4.  Modify User Information')
      print('5.  Issue Book')
      print('6.  Return Book')
      print('7.  Search Menu')
      print('8.  Report Menu')
      print('9.  Close Application')
      print('\n')
      choice = int(input('Please enter your choice : '))
      print('\n')
      if choice == 1:
        add_book()
      if choice == 2:
        add_user()
      if choice == 3:
        modify_book()
      if choice == 4:
        modify_user()
      if choice == 5:
        issue_book()
      if choice == 6:
        return_book()
      if choice == 7:
        search_menu()
      if choice == 8:
        report_menu()
      if choice == 9:
        sql_cursor.close()
        sql_connection.close()
        print('Application is closed, thank you!')
        break


if __name__ == "__main__":
    main_menu()






