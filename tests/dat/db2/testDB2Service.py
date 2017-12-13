"""Python test fixture to check that action can connect to db2 service"""

import ibm_db

def main(args):
    ssldsn = args["__bx_creds"]["dashDB"]["ssldsn"]
    conn = ibm_db.connect(ssldsn, "", "")
    if conn:
        print ("Connection succeeded.")
    else:
        print ("Connection failed.")
        return {"error":"Error connecting to db2"}

        # Select from TestTable (the row just inserted)
    cmd = "SELECT HISP_DESC FROM SAMPLES.HISPANIC_ORIGIN WHERE HISP_CODE='03'"
    result = ibm_db.exec_immediate(conn, cmd)

    if not result:
        return {"error":"error :"+cmd}
    else:
        ibm_db.fetch_both(result,0)
        value = ibm_db.result(result,"HISP_DESC")
        ibm_db.close(conn)
        return {"HISP_DESC":value}


if __name__ == "__main__":
    # execute only if run as a script
    input = {"__bx_creds":{"dashDB":{"ssldsn":"<ssldsn from credentials>"}}}
    print(main(input))