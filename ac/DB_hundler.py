import pymysql
from tools import get_Conf_data



class DBcheck():

    superfans_db=pymysql.connect(
        host=get_Conf_data.getConfigData('db.conf','db','host'),
        port=int(get_Conf_data.getConfigData('db.conf','db','port')),
        user=get_Conf_data.getConfigData('db.conf','db','user'),
        passwd=get_Conf_data.getConfigData('db.conf','db','pass'),
        database=get_Conf_data.getConfigData('db.conf','db','DBname'),
        autocommit=True
    )

    def get_DB_data(self):
        sql = 'select * from superfans.ad order by id DESC limit 1;'
        execute = self.execute(sql)
        return  execute


    def execute(self,sql):
        cursor = self.superfans_db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        # cursor.execute(sql)
        fetchall = cursor.fetchall()
        self.superfans_db.close()
        cursor.close()
        self.superfans_db.close()
        return fetchall


    def clear_tables(self,sql_list):
        for x in sql_list:
            self.superfans_db.cursor().execute('delete from %s' % (x))

    def close_conn(self):
        self.superfans_db.cursor().close()
        self.superfans_db.close()

