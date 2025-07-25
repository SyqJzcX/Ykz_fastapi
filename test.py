from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:*Sqzx*0524@localhost:3306/sqzx",
    echo=True
)

# 测试连接是否有效
def test_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("连接成功!")
        return True
    except Exception as e:
        print(f"连接失败: {str(e)}")
        return False


if __name__ == "__main__":
    test_connection()
