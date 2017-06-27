retail
    .factory('Product', function($resource) {
        return $resource(
            'http://localhost:8000/products/:id/',
            {id : "@id"},
            {
                'get': {
                    method: 'GET',
                    isArray: false,
                    headers: {
                        'Content-Type':'application/json',
                        'Authorization':'Token '+localStorage.getItem("user_token")
                    }
                },
                'query': {
                    method: 'GET',
                    isArray: true,
                    headers: {
                        'Content-Type':'application/json',
                        'Authorization':'Token '+localStorage.getItem("user_token")
                    }
                }
            },
            {
                stripTrailingSlashes: false
            }
        );
    });
