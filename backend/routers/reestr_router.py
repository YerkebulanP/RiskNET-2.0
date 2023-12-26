from fastapi import APIRouter
from config.database import conn
from models.reestr import Reestr, RiskCategory, RiskCode, Priority, Kri, Effectivity, Swot, Quarter
from schemas.schemas import Reestr_s
from sqlalchemy import select

from fastapi import HTTPException
import traceback

reestr_routers = APIRouter()


async def get_id_by_name(model_class, column, name):
    table = model_class.__table__
    query = table.select().where(column == name)
    result = conn.execute(query).fetchone()
    if result:
        return {'id': result[f'{column.name}']}
    else:
        return {'message': f'{column.name} not found'}
        
# Example handler to get risk_category_id by risk_category_name
@reestr_routers.get('/get_risk_category_id/{risk_category_name}', tags=['reestr'])
async def get_risk_category_id(risk_category_name: str):
    return await get_id_by_name(RiskCategory, RiskCategory.risk_category_name, risk_category_name)

# RISK_CODE
@reestr_routers.get('/get_risk_code_id/{risk_code_id}', tags=['reestr'])
async def get_risk_code_id(risk_code_id: str):
    return await get_id_by_name(RiskCode, RiskCode.risk_code_id, risk_code_id)

# PRIORITY
@reestr_routers.get('/get_priority_id/{priority_type}', tags=['reestr'])
async def get_priority_id(priority_type: str):
    return await get_id_by_name(Priority, Priority.priority_type, priority_type)

# KRI
@reestr_routers.get('/get_kri_id/{kri_name}', tags=['reestr'])
async def get_kri_id(kri_name: str):
    return await get_id_by_name(Kri, Kri.kri_name, kri_name)

# EFFECTIVITY
@reestr_routers.get('/get_effectivity_id/{effectivity_type}', tags=['reestr'])
async def get_effectivity_id(effectivity_type: str):
    return await get_id_by_name(Effectivity, Effectivity.effectivity_type, effectivity_type)

# SWOT
@reestr_routers.get('/get_swot_id/{swot_type}', tags=['reestr'])
async def get_effectivity_id(swot_type: str):
    return await get_id_by_name(Swot, Swot.swot_type, swot_type)

# QUARTER
@reestr_routers.get('/get_quarter_id/{quarter_value}', tags=['reestr'])
async def get_effectivity_id(quarter_value: int):
    return await get_id_by_name(Quarter, Quarter.quarter_value, quarter_value)



@reestr_routers.get('/reestr', tags=['reestr'])
async def fetch_all_Reestr():
    return conn.execute(select(Reestr)).fetchall()

# @reestr_routers.post('/reestr', tags=['reestr'])
# async def create_Reestr(reestr: Reestr_s):


#     conn.execute(reestr_m.insert().values(reestr_id = reestr.reestr_id, 
#                                        risk_year = reestr.risk_year, 
#                                        risk_quarter = reestr.quarter
#                                        )
#                 )
#     return conn.execute(reestr_m.select()).fetchall()

@reestr_routers.post('/reestr', tags=['reestr'])
async def create_Reestr(risk_category_name: str, 
                        risk_code_id:str, 
                        priority_type: str,
                        kri_name: str,
                        effectivity_type: str,
                        swot_type:str,
                        quarter_value:int,
                        reestr: Reestr_s):

    risk_category_id_response = await get_id_by_name(RiskCategory, RiskCategory.risk_category_name, risk_category_name)
    risk_code_id_response = await get_id_by_name(RiskCode, RiskCode.risk_code_id, risk_code_id)
    priority_id_response = await get_id_by_name(Priority, Priority.priority_type, priority_type)
    kri_id_response = await get_id_by_name(Kri, Kri.kri_name, kri_name)
    effectivity_id_response = await get_id_by_name(Effectivity, Effectivity.effectivity_type, effectivity_type)
    swot_id_response = await get_id_by_name(Swot, Swot.swot_type, swot_type)
    quarter_id_response = await get_id_by_name(Quarter, Quarter.quarter_value, quarter_value)

    try:
        if 'risk_category_id' in risk_category_id_response \
        and 'risk_code_id' in risk_code_id_response and 'priority_id' in priority_id_response and 'kri_id' in kri_id_response \
        and 'effectivity_id' in effectivity_id_response and 'swot_id' in swot_id_response and 'quarter_id' in quarter_id_response:

            risk_category_id = risk_category_id_response['risk_category_id']
            risk_code_id = risk_code_id_response['risk_code_id']
            priority_id = priority_id_response['priority_id']
            kri_id = kri_id_response['kri_id']
            effectivity_id = effectivity_id_response['effectivity_id']
            swot_id = swot_id_response['swot_id']
            quarter_id = quarter_id_response['quarter_id']

            conn.execute(Reestr.insert().values(
                reestr_id=reestr.reestr_id,
                risk_year=reestr.risk_year,
                quarter_id=quarter_id,
                risk_category_id=risk_category_id,
                risk_code_id=risk_code_id,
                owner=reestr.owner,
                control_sp=reestr.control_sp,
                risk_factor_1=reestr.risk_factor_1,
                risk_factor_2=reestr.risk_factor_2,
                risk_factor_3=reestr.risk_factor_3,
                risk_factor_4=reestr.risk_factor_4,
                source=reestr.source,
                swot_id=swot_id, 
                kri_id=kri_id,
                probability=reestr.probability,
                impact=reestr.impact,
                expected_losses=reestr.expected_losses,
                comments=reestr.comments,
                total_probability=reestr.total_probability,
                total_impact=reestr.total_impact,
                total_expected_losses=reestr.total_expected_losses,
                period=reestr.period,
                priority_id=priority_id,
                event_name=reestr.event_name,
                event_cost=reestr.event_cost,
                responsible_sp=reestr.responsible_sp,
                effectivity_id=effectivity_id,
                parent_id=reestr.parent_id
            ))
            print(risk_category_id)


            return {'message': 'Reestr record created successfully'}

    except Exception as e:
        traceback.print_exc()
        return {'detail': f"IntegrityError: {e}", 'message': 'Failed to create Reestr record'}
# @reestr_routers.put('/reestr/{reestr_id}', tags=['reestr'])
# async def update_Reestr(reestr: Reestr_s, reestr_id: int):
#     conn.execute(reestr_m.update().values(reestr_id = reestr.reestr_id, 
#                                        risk_year = reestr.risk_year, 
#                                        risk_quarter = reestr.quarter).where(reestr_m.c.reestr_id == reestr_id)
#                 )
#     return conn.execute(reestr_m.select().where(reestr_m.c.reestr_id == reestr_id)).first()

# @reestr_routers.delete('/reestr/{reestr_id}', tags=['reestr'])
# async def delete_Reestr(reestr: Reestr_s, reestr_id: int):
#     conn.execute(reestr_m.delete().where(reestr_m.c.reestr_id == reestr_id))
#     return conn.execute(reestr_m.select().where(reestr_m.c.reestr_id == reestr_id)).first()
