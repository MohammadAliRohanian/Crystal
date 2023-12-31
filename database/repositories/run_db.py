import pymysql
import config

host = config.DB_HOST
port = config.DB_PORT
user = config.DB_USER
password = config.DB_PASS
database = config.DB_NAME


# Insert to db and save started_at
def init_run(name, started_at, description):
    connection = pymysql.connect(
        host=host, port=port, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "insert into runs (name, started_at, description) values(%s, %s, %s)"

    val = (name, started_at, description)

    cursor.execute(query, val)
    connection.commit()
    connection.close()

    # Print stared run
    print("------ Run started at " + str(started_at) + " ------")

    return cursor.lastrowid


# Upadte runs
def finalize_run(run_model):
    connection = pymysql.connect(
        host=host, port=port, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "update runs set status = %s, ended_at = %s, duration = %s where id = %s"

    val = run_model.get_csv_array()

    cursor.executemany(query, val)
    connection.commit()
    connection.close()

    # print ended_at & duration
    print(
        "------ Run ended at "
        + str(val[0][1])
        + ". Duration: "
        + str(val[0][2])
        + " ------"
    )

    return cursor.lastrowid


# Select the last 10 rows
def get_run():
    connection = pymysql.connect(
        host=host, user=user, passwd=password, database=database
    )
    cursor = connection.cursor()

    query = "select * from runs order by id desc limit 10"

    cursor.execute(query)
    rows = cursor.fetchall()

    for i in rows:
        print(i)

    connection.commit()
    connection.close()
