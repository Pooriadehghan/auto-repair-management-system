from model.invoice import Invoice
from service.invoice_service import InvoiceService
from utils.decorator import exception_handling


class InvoiceController:

    @classmethod
    @exception_handling
    def save(cls, car_id, parts_cost=0, total_service_cost=0, discount_amount=0,
             payment_method="transfer", date_exit=None, time_exit=None,
             status="in_progress", acceptance_timestamp=None):
        invoice = Invoice(None, car_id, parts_cost, total_service_cost, discount_amount,
                          payment_method, date_exit, time_exit,
                          status, acceptance_timestamp)
        InvoiceService.save(invoice)
        return True, invoice

    @classmethod
    @exception_handling
    def update(cls, invoice_id, parts_cost, total_service_cost, discount_amount, payment_method, status):
        existing_invoice = InvoiceService.find_by_id(invoice_id)
        if existing_invoice is None:
            return False, "Invoice not found"

        invoice = Invoice(invoice_id=invoice_id, car_id=existing_invoice.car_id, parts_cost=parts_cost,
                          total_service_cost=total_service_cost,
                          discount_amount=discount_amount, payment_method=payment_method,
                          date_exit=existing_invoice.date_exit,
                          time_exit=existing_invoice.time_exit,
                          status=status, acceptance_timestamp=existing_invoice.acceptance_timestamp)
        InvoiceService.update(invoice)
        return True, invoice

    @classmethod
    @exception_handling
    def delete(cls, invoice_id):
        invoice = InvoiceService.find_by_id(invoice_id)
        return True, invoice

    @classmethod
    @exception_handling
    def find_all(cls):
        invoices = InvoiceService.find_all()
        return True, invoices

    @classmethod
    @exception_handling
    def find_by_id(cls, invoice_id):
        invoice = InvoiceService.find_by_id(invoice_id)
        return True, invoice

    @classmethod
    @exception_handling
    def find_by_date_range(cls, start_date, end_date=None):
        return InvoiceService.find_by_date_range(start_date, end_date)

    @classmethod
    @exception_handling
    def register_exit(cls, invoice_id, date_exit, time_exit):
        return InvoiceService.register_exit(invoice_id, date_exit, time_exit)
