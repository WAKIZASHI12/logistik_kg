import os
import time
import psycopg2


def wait_for_postgres(host, port, user, password, database, timeout=30):
    start_time = time.time()
    while True:
        try:
            conn = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            conn.close()
            print("PostgreSQL is ready for write operations.")
            break
        except psycopg2.OperationalError as e:
            if time.time() - start_time >= timeout:
                print(f"Timeout ({timeout} seconds) reached. Unable to connect to PostgreSQL.")
                raise e

            print("PostgreSQL is not ready yet. Retrying in 1 second...")
            time.sleep(1)


if __name__ == "__main__":
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_NAME")
    wait_for_postgres(host, port, user, password, database)
