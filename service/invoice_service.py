from datetime import datetime
from data_access.invoice_da import InvoiceDA
from model.invoice import Invoice


class InvoiceService:
    def __init__(self):
        self.da = InvoiceDA()

    def save(self, invoice):

        if hasattr(invoice, "invoice_id") and invoice.invoice_id and self.da.find_by_id(invoice.invoice_id):
            raise ValueError("invoice already exists!")
        if self.da.find_by_car_id(invoice.car_id):
            raise ValueError("invoice car already exists!")
        invoice.acceptance_timestamp = datetime.now()
        self.da.save(invoice)

    def update(self, invoice):
        if not hasattr(invoice, "invoice_id") or not self.da.find_by_id(invoice.invoice_id):
            raise ValueError("invoice not found!")
        self.da.update(invoice)

    def delete_by_id(self, invoice_id):
        if not self.da.find_by_id(invoice_id):
            raise ValueError("invoice not found!")
        return self.da.delete_by_id(invoice_id)

    def find_by_id(self, invoice_id):
        row= self.da.find_by_id(invoice_id)
        if row:
            return Invoice(*row)

        return None
    def find_all(self):
        return self.da.find_all()

    def register_exit(self, invoice_id, date_exit, time_exit):
        row = self.da.find_by_id(invoice_id)

        if not row:
            return False, "Invoice not found"

        invoice = Invoice(*row)

        invoice.date_exit = date_exit
        invoice.time_exit = time_exit
        invoice.status = "exited"

        self.da.update(invoice)

        return True, invoice

    def find_by_date_range(self, start_date, end_date=None):
        rows = self.da.find_by_date_range(start_date, end_date)
        invoice_list = [Invoice(*row) for row in rows]
        return True, invoice_list
