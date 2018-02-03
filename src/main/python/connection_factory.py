import mysql.connector

class ConnectionFactory(object):

    def __init__(self, connection_params_list):
        self.connection_params_list = connection_params_list

    def connect(self, host, database):
        params = self.get_connection_params(host, database)
        return mysql.connector.connect(**params)

    def get_connection_params(self, host, database):
        for params in self.connection_params_list:
            if params["host"] == host and params["database"] == database:
                return params
        return None

