retail
    .factory('Product', function($resource) {
        return {
            withToken : function (token){
                return $resource(
                    'http://localhost:8000/products/:id/',
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
                        }
                    },
                    {
                        stripTrailingSlashes: false
                    }
                );
            }
        }
    });
