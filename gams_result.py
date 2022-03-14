from gams.workspace import GamsWorkspace
import pandas as pd
import os


class GamsResult:

    def __init__(self, path):
        self.ws = GamsWorkspace()
        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), path)

        self.gams_db = self.ws.add_database_from_gdx(path)

    def param_as_df(self, param_name):
        gms_param = self.gams_db.get_parameter(param_name)
        data = [[*rec.keys, rec.value] for rec in gms_param]

        # domains have changed and now may contain sets
        domains = [x if type(x) == str else x.name for x in gms_param.domains]

        columns = domains + ["value"]
        param_df = pd.DataFrame(data=data, columns=columns)
        return param_df
