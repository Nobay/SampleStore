/**
 * Created by Nobay on 26/06/2017.
 */
retail
    .factory('Customer', function($resource) {
        return {
             withToken : function (token){
                 return $resource(
                        'http://localhost:8000/customers/:id/',
                        {id : "@id"},
                        {
                            'get': {
                                method: 'GET',
                                isArray: false,
                                headers: {
                                    'Content-Type':'application/json',
                                    'Authorization':token
                                }
                            },
                            'query': {
                                method: 'GET',
                                isArray: true,
                                headers: {
                                    'Content-Type':'application/json',
                                    'Authorization':token
                                }
                            },
                            'update': {

                            },
                            'save': {
                                method:'POST',
                                url: 'http://localhost:8000/customers/add/',
                                params: {
                                    username: "username", password: "password",
                                    first_name: "first_name", last_name: "last_name",
                                    email: "email", address: "address", phone_number: "phone_number"
                                },
                                headers: {
                                    'Content-Type':'application/json'
                                }
                            }
                        },
                        {
                            stripTrailingSlashes: false
                        }
                    );
             }
        }
    });