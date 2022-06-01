from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from mock import Mock
from dotenv import load_dotenv


class ApiClient:
    def __init__(self, api_key: str, timeout: int):
        self.api_key = api_key
        self.timeout = timeout


class Service:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    api_client = providers.Singleton(
        ApiClient,
        api_key=config.api_key,
        timeout=config.timeout,
    )

    service = providers.Factory(
        Service,
        api_client=api_client,
    )


@inject
def main(service: Service = Provide[Container.service]):
    ...


if __name__ == "__main__":
    load_dotenv()
    container = Container()
    container.config.api_key.from_env("API_KEY", required=True)
    container.config.timeout.from_env("TIMEOUT", as_=int, default=5)
    container.wire(modules=[__name__])

    main()

    with container.api_client.override(Mock()):
        main()
