import asyncio
import aiosqlite
from pathlib import Path

MIGRATIONS_DIR = Path(__file__).parent / "src" / "infrastructure" / "database" / "migrations"

async def migrate():
    db_path = "db.sqlite3"
    
    async with aiosqlite.connect(db_path) as conn:
        # Создаем таблицу миграций
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                name TEXT PRIMARY KEY
            )
        """)
        
        # Получаем примененные миграции
        cursor = await conn.execute("SELECT name FROM migrations")
        applied = {row[0] for row in await cursor.fetchall()}
        
        # Применяем новые миграции
        if MIGRATIONS_DIR.exists():
            migration_files = sorted(MIGRATIONS_DIR.glob("*.sql"))
            
            for file in migration_files:
                if file.name in applied:
                    continue
                
                print(f"Applying: {file.name}")
                sql = file.read_text(encoding='utf-8')
                await conn.executescript(sql)
                await conn.execute(
                    "INSERT INTO migrations (name) VALUES (?)",
                    (file.name,)
                )
                await conn.commit()
        
        print("✅ Migrations completed")

if __name__ == "__main__":
    asyncio.run(migrate())