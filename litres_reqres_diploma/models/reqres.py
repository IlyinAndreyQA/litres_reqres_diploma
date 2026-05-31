from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBody(BaseModel):
    name: str
    job: str


class RegisterBody(BaseModel):
    email: str
    password: str | None = None

    def model_dump_without_none(self) -> dict:
        return self.model_dump(exclude_none=True)


class UserData(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class UsersListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[UserData]
    support: Support


class SingleUserResponse(BaseModel):
    data: UserData
    support: Support


class CreatedUserResponse(BaseModel):
    name: str
    job: str
    id: str
    created_at: str = Field(alias="createdAt")

    model_config = ConfigDict(populate_by_name=True)


class UpdatedUserResponse(BaseModel):
    name: str
    job: str
    updated_at: str = Field(alias="updatedAt")

    model_config = ConfigDict(populate_by_name=True)


class ErrorResponse(BaseModel):
    error: str
