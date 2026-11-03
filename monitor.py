import time
import logging
import httpx

HEALTH_URL = "https://dev-ops-mid-term.vercel.app/health"

logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def check_health():
    try:
        response = httpx.get(HEALTH_URL, timeout=5)

        if response.status_code == 200:
            logging.info("API is healthy")
            print("API is healthy")
        else:
            logging.error(
                "API returned status code: %s",
                response.status_code
            )
            print("API is not healthy")

    except httpx.RequestError as error:
        logging.error("API is unavailable: %s", error)
        print("API is unavailable")


if __name__ == "__main__":
    while True:
        check_health()
        time.sleep(30)
