from estd_connection import estd_connection

cursor = estd_connection()


sql = """
DELETE  FROM MYSHARE
WHERE SYMBOL = 'HEI'
"""
cursor.execute(sql)
print("Deleted")