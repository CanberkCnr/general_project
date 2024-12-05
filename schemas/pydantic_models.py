from pydantic import BaseModel, Field


class ExampleModel(BaseModel):
    id: str = Field(default="",
                      description=""),
    example_1: str = Field(default="C",
                           description="")
