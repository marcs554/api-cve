import sys
import json
import requests
from requests.exceptions import InvalidURL, HTTPError, ConnectionError, ConnectTimeout


class CVE:

    def __init__(self, _id) -> None:
        """

        Args:
            _id (str): Id del CVE
        """
        self.__id = _id
    
    def fetch_info_cve(self):
        """Esta función se recoge de la url 'https://cve.circl.lu/api/cve/<id>' los datos que se le indique.
        Estos datos son extraidos de la web, parseados a formato json e imprimidos en pantalla.
        """
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
    cve.fetch_info_cve()

