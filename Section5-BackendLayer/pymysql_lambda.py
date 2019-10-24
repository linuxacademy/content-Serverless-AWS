import pymysql.cursors

def lambda_handler(event, context):
# Connect to the database
  connection = pymysql.connect(host='<IP-OR-DB-CLUSTER-URL>',
                               user='<username>',
                               password='<secure-password>',
                               db='information_schema',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
  
  try:
      with connection.cursor() as cursor:
          # Read a single record
          sql = "select * from information_schema.tables LIMIT 1"
          cursor.execute(sql)
          result = cursor.fetchall()
          print(result)
  finally:
      connection.close()
