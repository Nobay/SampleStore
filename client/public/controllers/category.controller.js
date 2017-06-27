/**
 * Created by Nobay on 21/06/2017.
 */
retail
    .controller('CategoryController', function($scope, $state, Category, Product, Asset) {
        if(localStorage.getItem("user_token") === "")
        {
            $state.go("login");
        }
        else
        {
            Category.query().$promise.then(function(data){
                var categories = data;
                console.log(categories);
                $scope.categories = [];

                // Foreach category get the first image of its product
                for(var i=0; i<categories.length; i++)
                {
                    var current_category = categories[i];
                    // Initialize with default image
                    current_category.image_url = "http://xpenology.org/wp-content/themes/qaengine/img/default-thumbnail.jpg";
                    console.log(current_category);

                    Product.get({ id: current_category.products[0]}).$promise.then(function(data) {

                        Asset.get({ id: data.assets[0]}).$promise.then(function(data) {
                            console.log(data);
                            current_category.image_url = data.image_url;
                        });
                    });
                    $scope.categories.push(current_category);
                }
                console.log($scope.categories);
            });
        }

    });