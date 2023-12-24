from config.database import conn, engine
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, Table, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Quarter(Base):
    __tablename__ =  'quarter'
    quarter_id = Column(Integer, primary_key=True, autoincrement=True)
    quarter_value = Column(Integer)

    reestr = relationship('Reestr', back_populates='quarter')


class Priority(Base):
    __tablename__ = 'priority'
    priority_id = Column(Integer, primary_key=True, autoincrement=True)
    priority_type = Column(String(255))

    reestr = relationship('Reestr', back_populates='priority')


class Swot(Base):
    __tablename__ = 'swot'
    swot_id = Column(Integer, primary_key=True, autoincrement=True)
    swot_type = Column(String(20))

    reestr = relationship('Reestr', back_populates='swot')


class RiskCategory(Base):
    __tablename__ = 'risk_category'
    risk_category_id = Column(Integer, primary_key=True, autoincrement=True)
    risk_category_name = Column(String(255))

    reestr = relationship('Reestr', back_populates='risk_category')
    risk_category_code = relationship('RiskCode', back_populates='risk_category')



class RiskCode(Base):
    __tablename__ = 'risk_code'
    risk_code_id = Column(String(50), primary_key=True)
    risk_code_full_name = Column(String(100))
    description = Column(String(1000))

    reestr = relationship('Reestr', back_populates='risk_code')
    risk_category = relationship('RiskCategory', back_populates='risk_code')


RiskCategoryCode = Table('risk_category_code', Base.metadata,
    Column('risk_category_id', Integer, ForeignKey('risk_category.risk_category_id')),
    Column('risk_code_id', String(50), ForeignKey('risk_code.risk_code_id'))
)

class Units(Base):
    __tablename__ = 'units'
    unit_id = Column(Integer, primary_key=True, autoincrement=True)
    unit_name = Column(String(50))



class Kri(Base):
    __tablename__ = 'kri'
    kri_id = Column(Integer, primary_key=True, autoincrement=True)
    kri_name = Column(String(500))
    unit_id = Column(Integer, ForeignKey('units.unit_id'), nullable=False)
    calculation_formula = Column(String(1000))
    description = Column(String(1000))
    green_zone = Column(Float)
    yellow_zone = Column(Float)
    orange_zone = Column(Float)
    red_zone = Column(Float)
    owner_name = Column(String(50))

    reestr = relationship('Reestr', back_populates='kri')


# effectivity_probability_m = Table('effectivity_probability', meta,
#     Column('effectivity_probability_id', Integer, primary_key=True, autoincrement=True),
#     Column('effectivity_probability_type', String(20))
# )

class Effectivity(Base):
    __tablename__ = 'effectivity'
    effectivity_id = Column(Integer, primary_key=True, autoincrement=True)
    effectivity_type = Column(String(20))

    reestr = relationship('Reestr', back_populates='effectivity')



class Reestr(Base):
    __tablename__ = 'reestr'

    reestr_id = Column(Integer, primary_key=True, autoincrement=True)
    risk_year = Column(Integer)
    quarter_id = Column(Integer, ForeignKey('quarter.quarter_id'))
    risk_category_id = Column(Integer, ForeignKey('risk_category.risk_category_id'), nullable=False)
    risk_code_id = Column(String(50), ForeignKey('risk_code.risk_code_id'), nullable=False)
    owner = Column(String(100))
    control_sp = Column(String(100))
    risk_factor_1 = Column(String(500), nullable=False)
    goal = Column(Float)
    threshold = Column(Float)
    fact = Column(Float)
    estimation = Column(Float)
    kpi_at_risk = Column(Float)
    risk_factor_2 = Column(String(1000))
    risk_factor_3 = Column(String(2000))
    risk_factor_4 = Column(String(3000))
    source = Column(String(100))
    swot_id = Column(Integer, ForeignKey('swot.swot_id'), nullable=False)
    kri_id = Column(Integer, ForeignKey('kri.kri_id'))
    probability = Column(Float)
    impact = Column(Float)
    expected_losses = Column(Float)
    comments = Column(String(1000))
    total_probability = Column(Float)
    total_impact = Column(Float)
    total_expected_losses = Column(Float)
    period = Column(String(50))
    priority_id = Column(Integer, ForeignKey('priority.priority_id'))
    event_name = Column(String(2000))
    event_cost = Column(Integer)
    responsible_sp = Column(String(500))
    effectivity_id = Column(Integer, ForeignKey('effectivity.effectivity_id'))
    parent_id = Column(Integer, ForeignKey('reestr.reestr_id'))

    quarter = relationship('Quarter', back_populates='reestr')
    risk_category = relationship('RiskCategory', back_populates='reestr')
    risk_code = relationship('RiskCode', back_populates='reestr')
    swot = relationship('Swot', back_populates='reestr')
    priority = relationship('Priority', back_populates='reestr')
    effectivity = relationship('Effectivity', back_populates='reestr')
    kri = relationship('Kri', back_populates='reestr')



Base.metadata.create_all(engine)
