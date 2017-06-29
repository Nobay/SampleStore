/**
 * Created by Nobay on 21/06/2017.
 */
retail
    .controller('CategoryController', function($scope, $state, Category, Product, Asset) {
        var token = "Token ";
        if(localStorage.getItem("user_token") === "")
        {
            token = undefined;
        }
        else
        {
            token += localStorage.getItem("user_token");
        }

        Category.withToken(token).query().$promise.then(function(data){
            var categories = data;
            $scope.categories = [];

            // Foreach category get the first image of its product
            for(var i=0; i<categories.length; i++)
            {
                var current_category = categories[i];
                // Initialize with de   fault image
                current_category.image_url = "http://xpenology.org/wp-content/themes/qaengine/img/default-thumbnail.jpg";
                console.log(current_category);

                Product.withToken(token).get({ id: current_category.products[0]}).$promise.then(function(data) {

                    Asset.withToken(token).get({ id: data.assets[0]}).$promise.then(function(data) {
                        console.log(data);
                        current_category.image_url = data.image_url;
                    });
                });
                $scope.categories.push(current_category);
            }
            console.log($scope.categories);
        });
    });