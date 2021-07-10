import sys
import json
import requests
from requests.exceptions import InvalidURL, HTTPError, ConnectionError, ConnectTimeout


class CVE:
    def __init__(self, _id) -> None:
        self.__id = _id
    
    def get_info_cve(self):
        try:
            response = requests.get("https://cve.circl.lu/api/cve/{}".format(self.__id))
            json_raw = json.loads(response.text)
            json_formated_data = json.dumps(json_raw, indent=5)
            print(json_formated_data)
        
        except InvalidURL as e:
            print(f"Error: no existe CVE '{self.__id}'\n{e} o el servidor de cve.circl.lu está fuera de linea")
        except ConnectionError as e:
            print(f"Error: Fallo de la conexión\n{e}")
        except ConnectTimeout as e:
            print(f"Error: Tiempo de espera agotado\n{e}")
        except HTTPError as e:
            print(f"Error: Fallo HTTP\n{e}")
        except Exception as e:
            print(f"Error: Desconocido\n{e}")



if __name__ == "__main__":
    id = sys.argv[1]
    cve = CVE(id)
    cve.get_info_cve()

