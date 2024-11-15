from models import DeliveryRider, Order, db


def createOrder(data): 
    order = Order(
        user = data.name,
        phone = data.phone,
        location = data.location,
        description = data.description,
        notes = data.notes,
        status = "pending",
        paid = False
    )
    
    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        print(e)
    
    return order


# get available riders
def getAvailableRider():
    riders = DeliveryRider.get_available_riders()
    # write selection logic


    return riders
    