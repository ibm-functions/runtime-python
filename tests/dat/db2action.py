import ibm_db

def main(args):
  #Connect to the DB2 database
  conn = ibm_db.connect("DATABASE=TEST;HOSTNAME=172.17.0.1;PORT=50000;PROTOCOL=TCPIP;UID=DB2INST1;PWD=db2inst1-pwd;", "", "")
  cmd = "DELETE FROM TESTTABLE WHERE name='Angela'"
  result = ibm_db.exec_immediate(conn, cmd)
  #output of the above can succeed or fail. Either is fine.

  # Insert into TestTable
  cmd = "INSERT INTO TESTTABLE (NAME, AGE, LOCATION) VALUES ('Angela', 27, 'Texas')"
  result = ibm_db.exec_immediate(conn, cmd)
  if not result:
      return {"err":"error :"+cmd}

  # Select from TestTable (the row just inserted)
  cmd = "SELECT * FROM TESTTABLE WHERE name='Angela'"
  result = ibm_db.exec_immediate(conn, cmd)
  if not result:
      return {"err":"error :"+cmd}
  else:
      ibm_db.fetch_both(result,0)
      value = ibm_db.result(result,"NAME")
      # Make sure the row was correctly inserted
      if value != 'Angela' :
          return {"err":"Expected name 'Angela', but instead found: "+ value}

  # Delete the row from TestTable
  cmd = "DELETE FROM TESTTABLE WHERE name='Angela'"
  result = ibm_db.exec_immediate(conn, cmd)
  if not result:
      return {"err":"error :"+cmd}

  # If no detected errors occurred so far; return Success status
  return {"message":"Successfully called db2 action"}
