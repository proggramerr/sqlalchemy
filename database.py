from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///data.db')
Base = declarative_base()

class Data(Base):
    __tablename__ = 'data_base'
    id = Column(Integer, primary_key=True)
    s_name = Column(String(512))
    c_name = Column(String(512))
    c_id = Column(String(32))
    a_type = Column(String(128))
    direction = Column(String(32))
    activation = Column(String(32))
    c_state = Column(String(32))
    control = Column(String(32))

Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def save_data(s_name, c_name, c_id, a_type, direction, activation, c_state, control):
    # Проверяем, существуют ли уже данные с такими же значениями полей
    existing_data = session.query(Data).filter_by(s_name=s_name, c_name=c_name, c_id=c_id, 
                                                   a_type=a_type, direction=direction, 
                                                   activation=activation, c_state=c_state, 
                                                   control=control).first()
    if existing_data:
        # Если данные уже существуют, то не сохраняем их повторно
        return
    # Если данные не существуют, то сохраняем их
    data = Data(s_name=s_name, c_name=c_name, c_id=c_id, a_type=a_type, 
                direction=direction, activation=activation, c_state=c_state, control=control)
    session.add(data)
    session.commit()

# тесты
save_data("name1", "company1", "id1", "type1", "direction1", "activation1", "state1", "control1")
save_data("name2", "company2", "id2", "type2", "direction2", "activation2", "state2", "control2")
save_data("qqprog", "order", "asd", "asdasd", "asdasd", "asdasd", "123", "controlasdasd2")
