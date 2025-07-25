from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine, text

partner = APIRouter()
engine = create_engine(
    "mysql+pymysql://root:*Sqzx*0524@localhost:3306/sqzx",
    echo=True
)


@partner.get("/partners")
def get_all_():
    try:
        # 使用连接池获取数据库连接
        with engine.connect() as connection:
            # 创建SQL查询
            sql = text("SELECT * FROM partner")

            # 执行查询
            result = connection.execute(sql)

            # 将结果转换为字典列表
            partners_data = [
                {
                    "id": row.id,
                    "name": row.name,
                    "age": row.age,
                    "sex": row.sex,
                    "major": row.major,
                    "hobby": row.hobby
                }
                for row in result
            ]

            return {"data": partners_data}

    except Exception as e:
        # 捕获并处理异常
        raise HTTPException(
            status_code=500,
            detail=f"数据库查询失败: {str(e)}"
        )
