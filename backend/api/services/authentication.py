from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
import jwt
from api.services.companies import CompanyServices, JWT_SECRET, oauth2_scheme, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES

class Authentication:
    """
        Function that is used to validate the token in the case that it requires it
    """
    def has_access(credentials = Depends(HTTPBearer())):
        try:
            payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=JWT_ALGORITHM)
            return payload
        except jwt.exceptions.DecodeError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except jwt.exceptions.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")

        

auth = Authentication