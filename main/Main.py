class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    def printList(self):
      printval = self.head
      print('\t\tPhonebook directory:')
      while (printval):
          str = printval.data[0].name.title() + ' - '
          x = 0
          for i in printval.data[0].numbers:
              str = str + i
              if x < len(printval.data[0].numbers) - 1:
                  str = str + ', '
                  x = x + 1
          print('\t\t' + str),
          printval = printval.next_node
    def findName(self, name):
      find = False
      printval = self.head
      while (printval and not(find)):
         if printval.data[0].name == name:
             find = True
             return printval.data
         printval = printval.next_node
      return find
    def findOne(self, name):
        data = self.findName(name)
        if data != False:
            str = 'Contact Number(s):'
            x = 0
            for n in data[0].numbers:
                str = str + n
                if x < len(data[0].numbers) - 1:
                    str = str + ', '
                    x = x + 1
            print('\t\t' + str)
        else:
            print('\t\tContact not found')
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.numbers = []
list = LinkedList()
def valid_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
while True:
    command = input('Command> ')
    arr = command.strip().split(' ')
    command = name = number = ''
    if len(arr) == 3:
        [ command, name, number  ] = arr
        name = name.lower()
        command = command.lower()
    elif len(arr) == 4:
        [ command, name, number, new_number  ] = arr
        name = name.lower()
        command = command.lower()
    elif len(arr) == 2: 
        [ command, name ] = arr
        name = name.lower()
        command = command.lower()
    else:
        command =  arr[0]
        command = command.lower()
    if len(arr) == 3 and command == 'i' and (len(number) == 7 or len(number) == 11) and valid_number(number):
        if list.size() > 0:
            find = list.findName(name)
            if find == False:
                contact = Contact(name, number)
                contact.numbers.append(contact.number)
                list.insert([contact])
                print('\t\tRemarks: New contact added')
                print('\t\tNumber of contacts:', list.size())
            else:
                contact = Contact(name, number)
                for n in find[0].numbers:
                    contact.numbers.append(n)
                contact.numbers.append(contact.number)
                list.delete(find)
                list.insert([contact])
                print('\t\tRemarks: New number added')
        else:
            contact = Contact(name, number)
            contact.numbers.append(contact.number)
            list.insert([contact])
            print('\t\tRemarks: New contact added')
            print('\t\tNumber of contacts:', list.size())
    elif command == 'd' and len(arr) == 2:
        find = list.findName(name)
        if find != False:
            try:
                list.delete(find)
                print('\t\tRemarks: Contact deleted')
                print()
            except ValueError:
                print('\t\tFailed to delete contact')
        else:
            print('\t\tRemarks: Contact not found')
    elif command == 'd' and len(arr) == 3:
        find = list.findName(name)
        if find != False:
            numbers = find[0].numbers 
            try:
                numbers.remove(number)
                find[0].numbers = numbers
                list.delete(list.findName(name))
                list.insert(find)
                print('\t\tRemarks: Number deleted')
            except ValueError:
                print('\t\tContact number not found')
        else: 
           print('\t\tRemarks: Contact not found') 
    elif command == 'v' and len(arr) == 1:
        list.printList()
    elif command == 'v' and len(arr) == 2:
        list.findOne(name.strip())
    elif command == 'u' and len(arr) == 3:
        update_name = number.lower()
        find = list.findName(name)
        if find != False:
            new_contact = find
            new_contact[0].name = update_name
            list.delete(find)
            list.insert(new_contact)
            print('\t\tRemarks: Contact updated')
        else:
            print('\t\tRemarks: Contact not found')
    elif command == 'u' and len(arr) == 4 and (len(number) == 7 or len(number) == 11 and valid_number(number)) and (len(new_number) == 7 or len(new_number) == 11 and valid_number(new_number)):
        find = list.findName(name)
        if find != False:
            new_contact = find
            try:
                new_contact[0].numbers.remove(number)
                new_contact[0].numbers.append(new_number)
                list.delete(find)
                list.insert(new_contact)
                print('\t\tRemarks: Contact updated')
            except ValueError:
                print('\t\tContact number not found')
        else:
            print('\t\tRemarks: Contact not found')
    elif command == 'x':
        print('Remarks: The program ended')
        break
    else:
        print('Remarks: Invalid command')
