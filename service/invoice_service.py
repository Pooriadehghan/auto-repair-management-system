from data_access.invoice_da import InvoiceDA


class InvoiceService:
    def __init__(self):
        self.da = InvoiceDA()

    def save(self, invoice):

        if hasattr(invoice, "invoice_id") and invoice.invoice_id and self.da.find_by_id(invoice.invoice_id):
            raise ValueError("invoice already exists!")
        if self.da.find_by_car_id(invoice.car_id):
            raise ValueError("invoice car already exists!")
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
        return self.da.find_by_id(invoice_id)

    def find_all(self):
        return self.da.find_all()
