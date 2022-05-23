import xlsxwriter


class Client:

    row = 0
    coloumn = 0

    def __init__(self, *args, **kwargs):

        self.cnme = clntname
        self.date = date
        self.adv = advance
        self.tot = total
        self.bal = balance

        details = [self.cnme, self.date, self.adv, self.tot, self.bal]

        content = ["Client name", "date", "Advance", "Balance", "Total"]

        for item in content:
            bookSheet.write(Client.row, Client.coloumn, content)
            row += 1

    def Sheet(self):

        Client.row = 0
        Client.coloumn += 1

        self.tot = self.adv + self.bal

        for items in Client.details:
            bookSheet.write(Client.row, Client.coloumn, Client.details)
            Client.row += 1

        bookSheet.close()


if __name__ == "__main__":

    bookName = xlsxwriter.Workbook("AccountingsRam.xlsx")
    bookSheet = bookName.add_worksheet()

    clntname = str(input("Please Enter your Client's name\n"))
    date = str(input("Please Enter the date: \n"))
    advance = str(input("Enter the advance amount given by the Client\n"))
    balance = str(input("Enter the balance amount give by the Client\n"))

    total = advance + balance

    exec = Client(clntname, date, advance, balance, total)
