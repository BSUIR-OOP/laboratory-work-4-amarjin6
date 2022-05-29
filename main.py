from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    api_client = providers.Singleton(
        api_key=config.api_key,
        timeout=config.timeout,
    )

    service = providers.Factory(
        api_client=api_client,
    )


@inject
def main():
    ...


if __name__ == "__main__":
    container = Container()
    # container.config.api_key.from_env("API_KEY", required=True)
    # container.config.timeout.from_env("TIMEOUT", as_=int, default=5)
    container.wire(modules=[__name__])

    main()  # <-- dependency is injected automatically