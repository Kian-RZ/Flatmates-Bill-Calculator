import math
import fpdf

class Flatmate:
    def __init__(self, name, days):
        self.name = name
        self.days = days
        self.pay = None

class Room:
    def __init__(self, amount):
        self.amount = amount

    def calculate_bills(self,flatmate_list: list):
        if len(flatmate_list) == 0: return
        for test in flatmate_list:
            if type(test) != Flatmate:
                return ValueError('Your List Should Be List Of Flatmate Type Objects')
        days = 0
        for flatmate in flatmate_list:
            days += int(flatmate.days)
        unit = math.ceil(self.amount / days)
        for flatmate in flatmate_list:
            flatmate.pay = unit * int(flatmate.days)

class PdfReport:
    def __init__(self, path):
        self.path = path

    def set_path(self,path):
        if str(path)[-1] != 'f' or str(path)[-2] != 'd' or str(path)[-3] != 'p' or str(path)[-4] != '.':
            path += '.pdf'
        self.path = path

    def export(self,room,flatmate_list):

        pdf = fpdf.FPDF(format='letter')
        pdf.add_page()
        pdf.set_font("Arial", size=18)
        pdf.set_text_color(69,115,255)
        pdf.cell(200, 10, txt="Flatmates Bill Calculator Report", ln=1, align="L")
        pdf.set_text_color(143,143,143)
        pdf.cell(200, 10, txt=f"Total Bill: {room.amount}", ln=2, align="L")
        pdf.set_text_color(71,71,71)
        count = 3
        for flatmate in flatmate_list:
            pdf.cell(200, 10, txt=f"{flatmate.name} ( {flatmate.days} ) -> {flatmate.pay}", ln=count, align="L")
            count += 1
        pdf.output(self.path)