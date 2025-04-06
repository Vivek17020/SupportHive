import aiohttp
import asyncio
from typing import Union, List
from vectorizer.app.core.settings import get_settings
from vectorizer.app.core.llogger import logger  # fixed: was incorrectly imported as `logger`

settings = get_settings()

def _sync_run(coro):
    """Utility to run async coroutine from sync context"""
    return asyncio.get_event_loop().run_until_complete(coro)

async def _get_embedding_from_olmo(content: Union[str, List[str]]) -> Union[List[float], List[List[float]]]:
    async with aiohttp.ClientSession() as session:
        try:
            payload = {"input": content}
            headers = {}

            # Optional auth header if API key is provided
            if hasattr(settings, "OLMO_API_KEY") and settings.OLMO_API_KEY:
                headers["Authorization"] = f"Bearer {settings.OLMO_API_KEY}"

            async with session.post(settings.OLMO_EMBEDDING_URL, headers=headers, json=payload) as response:
                if response.status != 200:
                    raise ValueError(f"Failed to get embedding: {response.status}, {await response.text()}")

                result = await response.json()
                return result.get("embedding") if isinstance(content, str) else result.get("embeddings")

        except Exception as e:
            logger.error(f"Error generating embedding from OLMo: {str(e)}")
            raise

def generate_embedding(content: Union[str, List[str]]) -> Union[List[float], List[List[float]]]:
    return _sync_run(_get_embedding_from_olmo(content))
