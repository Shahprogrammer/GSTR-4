class GST_Company():
    def __init__(self, gstno, rate,pos,st):
        self.GSTNO = gstno
        self.RATE = rate
        self.POS=pos
        self.ST=st
        self.__taxable = 0.00
        self.__cgst = 0.00
        self.__sgst = 0.00
        self.__igst = 0.00
        self.__cess = 0
        self.__total = 0.00

    def updata_invoice(self, taxable, cgst, sgst, igst,cess):
        self.__taxable += taxable
        self.__cgst += cgst
        self.__sgst += sgst
        self.__igst += igst
        self.__cess+= cess
        self.__total += (taxable + cgst + sgst + igst + cess)

    def generate_output(self):
        return [
            self.GSTNO, self.POS,self.ST,self.__taxable, self.RATE, self.__igst, self.__cgst, self.__sgst,self.__cess,
             self.__total
        ]
    def test(self):
        return self.__taxable
    @classmethod
    def from_dict(cls,df_dict):
        return cls(df_dict['GSTNO'],df_dict['RATE'],df_dict['POS'],df_dict['ST'])