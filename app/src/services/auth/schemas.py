from typing import Union, Optional
from pydantic import (
	BaseModel, HttpUrl,
	DirectoryPath, validator
)

class HTMLToFileRequestSchema(BaseModel):
	name: str
	url: HttpUrl
	dirpath: DirectoryPath
	filename: str