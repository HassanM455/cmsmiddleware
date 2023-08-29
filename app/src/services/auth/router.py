'''
Author: Hassan Mahmood

Version: 0.0.1

Description: 
'''


from typing import Union, Annotated
from fastapi import (
	APIRouter, Depends, 
	Request, status
)




router = APIRouter()


@router.post(
	"/", 
	summary="", 
	description="""
        """
	, 
	status_code=status.HTTP_201_CREATED
)
async def func(
	request: Request,
) -> int:

	"""
	Description: 
    """



	# return status.HTTP_201_CREATED

	pass
