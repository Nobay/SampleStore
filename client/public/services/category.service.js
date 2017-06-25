retail
    .factory('Category', function($resource) {
        return $resource(
            'http://localhost:8000/categories/:id/',
            {id : "@id"},
            {
                'get': {
                    method: 'GET',
                    isArray: false,
                    headers: {
                        'Content-Type':'application/json',
                        'Authorization':'Token 28c1e4b88ee2ac1ee4ff44615c7f074bfc83262c'
                    }
                },
                'query': {
                    method: 'GET',
                    isArray: true,
                    headers: {
                        'Content-Type':'application/json',
                        'Authorization':'Token 28c1e4b88ee2ac1ee4ff44615c7f074bfc83262c'
                    }
                }
            },
            {
                stripTrailingSlashes: false
            }
        );
    });