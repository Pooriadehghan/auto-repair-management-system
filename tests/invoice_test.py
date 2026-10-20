from model.invoice import Invoice
from datetime import date, time, datetime
from data_access.invoice_da import InvoiceDA
from service.invoice_service import InvoiceService

#==============================================================
# INVOICE TEST----PASSED
#==============================================================
invoice1=Invoice(
    invoice_id=1,
    car_id=3,
    parts_cost=1500000,
    total_service_cost=800000,
    discount_amount=200000,
    payment_method="cash",
    date_exit=date(2026, 10, 20),
    time_exit=time(14, 30),
    status="completed",
    acceptance_timestamp=datetime(2026, 10, 20, 10, 0)
)
invoice2=Invoice(
    invoice_id=2,
    car_id=4,
    parts_cost=160000,
    total_service_cost=99000,
    discount_amount=50000,
    payment_method="transfer",
    date_exit=date(2026, 10, 20),
    time_exit=time(14, 30),
    status="exited",
    acceptance_timestamp=datetime(2026, 10, 20, 10, 0)
)

# print(invoice1.to_tuple())
# print(invoice1.to_dict())



#==============================================================
# INVOICE Da TEST----PASSED
#==============================================================
invoice_da=InvoiceDA()

# invoice_da.save(invoice1)
# invoice_da.save(invoice2)
# print("DONE")
# print(invoice_da.find_all())
# print(invoice_da.find_by_id(2))
# print(invoice_da.find_by_id(1))

# invoice1.status="completed"
# invoice_da.update(invoice1)

# invoice_da.delete_by_id(1)
# print("done")


#==============================================================
# INVOICE Service TEST----PASSED
#==============================================================
# invoice_service=InvoiceService()
# Invoice.parts_cost=155
# invoice_service.update(invoice2)
# print("done")
