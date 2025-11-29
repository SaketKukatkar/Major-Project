import asyncio
import sys
import os
import uvicorn

if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import init_db
from app.utils.logger import setup_logging
from app.core.config import settings

async def initialize_database():        
    try:
        print("🔧 Initializing database..")
        await init_db()
    except Exception as e:
        print(f"⚠️  Database initialization warning: {e}")

def main():
    """Main function to run the application."""
    print(f"📡 Server will run on: http://localhost:{settings.PORT}")
    print()
    
    asyncio.run(initialize_database())
    print()
    
    uvicorn.run(    
        "app.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()  