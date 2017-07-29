from Services.LoginService import LoginService
from Services.RESTService import RESTService
from Services.CubeService import CubeService


login = LoginService.native('admin', 'apple')

with RESTService(ip='', port=8001, login=login, ssl=False) as tm1_rest:
    cube_service = CubeService(tm1_rest)
    cube_service.delete('Rubiks Cube')