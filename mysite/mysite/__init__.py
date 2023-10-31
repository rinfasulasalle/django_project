import pymysql

# Configura pymysql para ser compatible con Django
pymysql.version_info = (1, 4, 6, "final", 0)
pymysql.install_as_MySQLdb()
