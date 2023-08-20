from Employee import Employee

def main():
    Adams = Employee("Adams", "E7876", 5000, "Accounting")
    Jones = Employee("Jones", "E7499", 45000, "Research")
    Martin = Employee("Martin", "E7900", 5000, "Sales")
    Smith = Employee("Smith", "E7698", 5000, "Operations")

    print(Adams.descrip())
    print(Jones.descrip())
    print(Martin.descrip())
    print(Smith.descrip())

#if __name__ == "__main__":
main()