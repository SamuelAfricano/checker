from http.client import HTTPConnection
from urllib.parse import urlparse

def verifica_status_do_site(url, timeout=2):
    """ Esta função retona True se a url esta online

        Em outros casos retorna False
    """
    error = Exception("Desconhecida")
    parse = urlparse(url)
    host = parse.netloc or parse.path.split("/")[0]
    for port in (80, 443):
        conexao = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            conexao.request("HEAD", "/")
            return True
        except Exception as e:
            return False
        finally:
            conexao.close()
    return error

