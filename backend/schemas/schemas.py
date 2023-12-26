from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    lastname: str
    email: str
    password: str
    position: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Reestr_s(BaseModel):
    reestr_id: int
    risk_year: int
    quarter_id: int
    risk_category_id: int
    risk_code_id: str
    owner: str
    control_sp: str
    risk_factor_1: str
    risk_factor_2: str
    risk_factor_3: str
    risk_factor_4: str
    source: str
    swot_id: int
    kri_id:int
    probability: float
    impact: float
    expected_losses: float
    comments: str
    total_probability: float
    total_impact: float
    total_expected_losses: float
    period: str
    priority_id: int
    event_name: str
    event_cost: int
    responsible_sp: str
    effectivity_id: int
    parent_id: int

