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

    # Select from TestTable (the row just inserted).
    #
    # Due to the db2 lite plan we use, the schema name is fixed to be
    # the same as the username. We cut the value of the UID field
    # in the ssldsn to get it and insert it in the select statement.
    # The ssldsn looks like this:
    # ssldsn="DATABASE=BLUDB;HOSTNAME=dashdb-xxxx.services.dal.bluemix.net;PORT=50001;PROTOCOL=TCPIP;UID=yyyyyyy;PWD=<hidden>;"
    #
    ssldsndict = dict(x.split("=") for x in ssldsn.rstrip(";").split(";"))
    print("user={}".format(ssldsndict["UID"]))

    cmd = "SELECT HISP_DESC FROM {}.HISPANIC_ORIGIN WHERE HISP_CODE='03'".format(ssldsndict["UID"])
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
