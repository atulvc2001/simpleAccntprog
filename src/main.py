import xlsxwriter

class theBook:

    content = ["Client name","Advance","Balance","Total"]

    def Accnt(self,clnm):
        bookName = xlsxwriter.Workbook('AccountingsRam.xlsx')
        bookSheet = bookName.add_worksheet()

        row = 0
        coloumn = 0

        for item in content:

            bookSheet.write(row,coloumn,item)
            row += 1

    def clientname(clntname)

if __name__ == "__main__":
    
    theBook.run()
    bookName = xlsxwriter.Workbook('AccountingsRam.xlsx')
    bookSheet = bookName.add_worksheet()
   
    clntname = str(input("Please Enter your Client's name"))
