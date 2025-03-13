from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

DATABASE_URL = ""

# TODO: Need Testing.
# Database connection Class.
class DBconnection:
    def __init__(self):
        self.engine = create_engine(url=DATABASE_URL)
        self.session = sessionmaker(bind=self.engine)()
        
    def get_session(self):
        return self.session
    
    def insert(self, obj):
        try:
            self.session.add(obj)
            self.session.commit()
            return obj
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Insert error: {str(e)}")
    
    def delete(self, obj):
        try:
            self.session.delete(obj)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Delete error: {str(e)}")
    
    def update(self, model, obj_id, **updated_fields):
        try:
            obj = self.session.query(model).filter_by(id=obj_id).first()
            if not obj:
                raise Exception("Object not found")
            for key, value in updated_fields.items():
                setattr(obj, key, value)
            self.session.commit()
            return obj
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Update error: {str(e)}")
    
    def query(self, model, **filters):
        try:
            return self.session.query(model).filter_by(**filters).all()
        except Exception as e:
            raise Exception(f"Query error: {str(e)}")
        
@contextmanager
def get_db():
    db = DBconnection().get_session()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise Exception(f"Database error: {str(e)}")
    finally:
        db.close()