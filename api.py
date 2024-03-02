from fastapi import FastAPI  # api 모듈
from pydantic import BaseModel  # api 값 검증 모듈

import calculator  # 사용자 계산기 모듈

app = FastAPI()


@app.get("/", description="main route")
async def get_root_route():
    return {"message":"hello world"}

class formula(BaseModel):
    """
    pydantic 모듈을 활용해 x, y, operator값 type 지정
    """
    x: float
    y: float
    operator: str

@app.post("/calculator", description='계산식을 사용자가 인풋으로 넣습니다.')
async def input_formula(Input:formula):
    """
    Input을 우리가 지정한 class를 받아 계산기 각 인자(x,y,operator) 할당
    여기서 type 검증된 값이 들어감
    return: 계산기 모듈의 리턴 결과
    """
    result = calculator.calculate_values(x=Input.x, y=Input.y, operator=Input.operator)
    return result