from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import asyncio
import sys
import os
from pathlib import Path

from app.db.chroma import init_chroma
from app.routers import query, sync, subjects, agents as agents_router, agentmemo as agentmemo_router

AGENTS_DIR = Path(__file__).resolve().parent.parent.parent / "agents"


async def _run_back_agent():
    proc = await asyncio.create_subprocess_exec(
        sys.executable, str(AGENTS_DIR / "back_agent.py"),
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    await proc.wait()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_chroma()
    asyncio.create_task(_run_back_agent())
    yield


app = FastAPI(title="LLM Wiki RAG API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router,           prefix="/api")
app.include_router(sync.router,            prefix="/api")
app.include_router(subjects.router,        prefix="/api")
app.include_router(agents_router.router,   prefix="/api")
app.include_router(agentmemo_router.router)

# Serve the GUI from project root
GUI_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "wiki_gui.html")

@app.get("/")
def serve_gui():
    return FileResponse(GUI_PATH)
