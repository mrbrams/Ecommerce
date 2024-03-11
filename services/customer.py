from fastapi import HTTPException, status

from schema.customer import customers, CustomerCreate, Customer

#Dependency class injected to customer creation

class CustomerService:
    #create a dependency that checks that username not in the system when creating a new customer
    @staticmethod
    def is_username_unique(payload : CustomerCreate):
        for customer in customers:
            if customer.username == payload.username:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Username {payload.username}already exists",
                )
            return payload
    
customer_service = CustomerService()