import allure
from jsonschema.validators import validate
from utils.helper import load_json_schema, base_url


@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Login user')
def test_post_successful_loin():
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'
    schema = load_json_schema('post_successful_loin.json')
    response = base_url.post(
        '/api/login',
        json={
            'email': email,
            'password': password
        })

    validate(instance=response.json(), schema=schema)

@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Registration')
def test_post_successful_register():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    response = base_url.post(
        '/api/register',
        json={
            'email': email,
            'password': password
        })
    schema = load_json_schema('post_successful_register.json')
    validate(instance=response.json(), schema=schema)

@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Use update by put')
def test_put_update_user():
    name = 'An'
    job = 'student'

    response = base_url.put(
        '/api/users/2',
        json={
            'name': name,
            'job': job
        }
    )
    schema = load_json_schema('put_update_user.json')
    validate(instance=response.json(), schema=schema)

@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Use update by patch')
def test_patch_update_user():
    name = 'An'
    job = 'student'

    response = base_url.patch(
        '/api/users/2',
        json={
            'name': name,
            'job': job
        }
    )

    schema = load_json_schema('patch_update_user.json')
    validate(instance=response.json(), schema=schema)

@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Create user')
def test_post_create_user():
    name = 'An'
    job = 'student'

    response = base_url.post(
        '/api/users',
        json={
            'name': name,
            'job': job
        }
    )
    schema = load_json_schema('post_create_user.json')
    validate(instance=response.json(), schema=schema)

@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Found unknown user')
def test_get_unknown_users():

    response = base_url.get('/api/unknown')
    schema = load_json_schema('get_unknown_users.json')
    validate(instance=response.json(), schema=schema)

@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Found single user')
def test_get_single_users():

    response = base_url.get('/api/users/2')
    schema = load_json_schema('get_single_users.json')
    validate(instance=response.json(), schema=schema)


@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Unsuccessful loin')
def test_post_unsuccessful_loin():
    response = base_url.post('/api/login')
    schema = load_json_schema('post_unsuccessful_loin.json')
    validate(instance=response.json(), schema=schema)

@allure.label('owner', 'An')
@allure.feature('Tests reqres.in')
@allure.title('Unsuccessful registration')
def test_post_unsuccessful_register():

    response = base_url.post('/api/register')
    schema = load_json_schema('post_unsuccessful_register.json')
    validate(instance=response.json(), schema=schema)