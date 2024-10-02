from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    country = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Customer(id={self.customer_id}, email={self.email})>"

# To create the table, use something like this in your main code or migration script:
# Base.metadata.create_all(engine)  # Assuming `engine` is your SQLAlchemy engine instance.


"""
Explanation:
customer_id: Unique ID for each customer (primary key).
first_name: Customer’s first name.
last_name: Customer’s last name.
email: Unique email for each customer (index added for performance).
phone_number: Optional phone number of the customer.
address, city, country: Optional fields for storing the customer's address details.
created_at: Automatically stores the timestamp when the customer was created.
is_active: Boolean field to indicate if the customer account is active.
"""