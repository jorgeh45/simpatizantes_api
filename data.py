import json
import psycopg2
from pprint import pprint
from collections import namedtuple
import urllib.parse as url


class DataSource:
    config_info = None
    cursor= None

    def get_connection(self):

        with open('config.json') as data_file:
            config = json.load(data_file, object_hook=lambda d: namedtuple('config', d.keys())(*d.values()))


        self.config_info=config


    def connect(self):

        conf = self.config_info

        try:

            conn = psycopg2.connect("dbname='{}' user='{}' password='{}'".format(conf.dbname,conf.user,conf.passwd))
            pprint("Connection Success with database!")
        except:

            print ("I am unable to connect to the database.")

        self.cursor = conn.cursor()

    def get_simpatizantes(self,cedula):

        self.cursor.execute("SELECT * FROM simpatizantes WHERE cedula='{}'".format(cedula))
        old_records = self.cursor.fetchone()

        if old_records is None:
            return None
        #records = self.emptyField(old_records);

        records=old_records

        # checking, but the problem with this is that doesnt accept None,
        # simpatizante =json.dumps(url.parse_qs("cedula={}&nombres={}&apellido1={}&apellido2={}&provincia={}&circ={}&municipio={}&codigocolegio={}&recinto={}&direccion={}&sectorparaje={}&provincia_org={}circ_org={}&municipio_org={}&intermedio={}&cb={}&mun_ced={}&seq_ced={}&ver_ced={}&cole_municipio={}"
        #                                       .format(records[0],records[1],records[2],records[3],records[4],records[5],records[6],records[7],records[8],records[9],records[10],records[11],records[12],records[13],records[14],records[15],records[16],records[17],records[18],records[19])))


        return json.dumps({

            "cedula": records[0],
            "Nombre": records[1],
            "Apellido1": records[2],
            "Apellido2": records[3],
            "Provincia": records[4],
            "Circ": records[5],
            "Municipio": records[6],
            "CodigoColegio": records[7],
            "Recinto": records[8],
            "Direccion": records[9],
            "SectorParaje": records[10],
            "provincia_org": records[11],
            "circ_org": records[12],
            "municipio_org": records[13],
            "Intermedio": records[14],
            "cb": records[15],
            "mun_ced": records[16],
            "seq_ced": records[17],
            "ver_ced": records[18],
            "cole_municipio": records[19]

        })

    def emptyField(self,records):
        new_records=[]
        for field in records:

            if field==None:
                new_records.append("null")
            else:
                new_records.append(field)

        return tuple(new_records)
