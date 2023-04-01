from estd_connection import estd_connection

cursor = estd_connection()
sql = """
UPDATE MYSHARE SET
NAME = 'Standard Chartered Bank '
WHERE SYMBOL = 'SCB'
"""

cursor.execute(sql)
print("Updated")