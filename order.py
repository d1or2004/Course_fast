from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from models import Order, User, Product
from schemas import OrderStatusModel, OrderModel
from database import session, engine
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException

order_rooter = APIRouter(prefix="/order")
session = session(bind=engine)


@order_rooter.get('/')
async def order(Authorsize: AuthJWT = Depends()):
    try:
        Authorsize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token")
    return {"msg": "Bu order router sahifasi"}
#
#
# @order_rooter.post('/make', status_code=status.HTTP_200_OK)
# async def make_order(order: Order, Authorize: AuthJWT = Depends()):
#     try:
#         Authorize.jwt_required()
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token")
#     current_user = Authorize.get_jwt_subject()
#     user = session.query(Order).filter(User.username == current_user).first()
#
#     new_order = Order(
#         quantity=order.quantity,
#     )
#     new_order.user = user
#     session.add(new_order)
#     session.commit()
#
#     response = {
#         "id": new_order.id,
#         "quantity": new_order.quantity,
#         "order_status": new_order.order_status,
#     }
#     return jsonable_encoder(response)
