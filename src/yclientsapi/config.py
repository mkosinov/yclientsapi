class Config:
    api_base_url = "https://api.yclients.com/api/v1"

    def __init__(self, company_id: int):
        self.company_id = company_id

    # def compose_url(self, api_version: str = "v1", *args: str) -> str:
    #     return "/".join([self.api_base_url, api_version, *args])
