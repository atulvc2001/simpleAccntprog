import xlsxwriter

class Client:

    row = 0
    coloumn = 0

    def __init__(self, clientname, date, advance,balance,total):

        self.cnme = clientname
        self.date = date
        self.adv = advance
        self.tot = total

        content = ["Client name", "date", "Advance", "Balance", "Total"]

        for item in content:
            bookSheet.write(Client.row,Client.coloumn,content)
            Client.row += 1
        
    def Sheet(self):

        for 
            for items in Client.content:
                bookSheet.write(Client.row, Client.coloumn+1,self.cnme)

        

if __name__ == "__main__":
    
    Client.run()
  

    bookName = xlsxwriter.Workbook('AccountingsRam.xlsx')
    bookSheet = bookName.add_worksheet()
   
    clntname = str(input("Please Enter your Client's name"))
"
