import json
import falcon
import data
from pprint import pprint

class ApiSimpatizantes(object):
    db = data.DataSource()
    db.get_connection()
    db.connect()

    def on_get(self,req,resp,cedula):
        """Handles all GET requests."""
        #origin = req.get_header('Origin')
        cedula= cedula.replace("-","")
        print(cedula)
        response =self.db.get_simpatizantes(cedula)

        if response is None:
            response= json.dumps({})


        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
        resp.body = response


app=falcon.API()
simpatizantes= ApiSimpatizantes()
app.add_route('/api/simpatizantes/{cedula}',simpatizantes)

