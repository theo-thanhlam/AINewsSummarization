from models import BaseModel
from typing import Type, TypeVar, Generic, Optional,List
from sqlalchemy.exc import SQLAlchemyError
from libs.database import getSession

T = TypeVar("T")


class CRUD(Generic[T]):
    # def __init__(self, model:Type[T]):
    #     self.model = model
    
    def getOneBy(self, model:BaseModel,**filters):
        with getSession() as db:
            if filters:
                query = db.query(model).filter_by(**filters)
                return query.first()
    
    def getMultipleBy(self, model:BaseModel,**filters):
        with getSession() as db:
            if filters:
                query = db.query(model).filter_by(**filters)
                return query.all()
            
    
    def getById(self,model:BaseModel,  id:int) -> Optional[T]:
        with getSession() as db:
            return db.query(model).filter_by(id=id).first()
    
    def getAll(self,model:BaseModel, limit=50, skip=0)->List[T]:
        with getSession() as db:
            return db.query(model).offset(skip).limit(limit).all()
    
    def create(self, model:BaseModel)->T:
        with getSession() as db:
            try:
                # new_obj = self.model(**data)
                db.add(model)
                db.commit()
                db.refresh(model)
                return model
            except SQLAlchemyError as e:
                db.rollback()
                raise e
    
    def update(self,model:BaseModel,id:int, new_data:dict)->T:
        with getSession() as db:
            obj = db.query(model).filter_by(id=id).first()
            if obj:
                for field, value in new_data.items():
                    setattr(obj, field, value)
                db.commit()
                db.refresh(obj)
            return obj
        
    def delete(self, id:int) -> Optional[T]:
        with getSession() as db:
            obj = db.query(self.model).filter_by(id=id).first()
            if obj:
                db.delete(obj)
                db.commit()
            return obj
    