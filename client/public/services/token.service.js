retail
    .factory('Token', function($resource) {
        return $resource(
            'http://localhost:8000/get_auth_token/',
            {username: "username", password: "password"},
            {
                'save': {
                    method:'POST',
                    headers: {
                        'Content-Type':'application/json'
                        }
                }
            },
            {
                stripTrailingSlashes: false
            }
        );
    });