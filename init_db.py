import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import init_db
from app.utils.logger import setup_logging

async def main():
    """Initialize the database."""
    print("🚀 Initializing Syncly Database...")
    
    try:
        setup_logging()

        await init_db()
        
        print("✅ Database initialized successfully!")
        print("📁 SQLite database file: syncly.db")
        
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main()) 