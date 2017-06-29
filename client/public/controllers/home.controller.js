/**
 * Created by Nobay on 24/06/2017.
 */
retail
    .controller('HomeController', function($scope, $state, Category) {
        if(localStorage.getItem("user_token") === "")
        {
            localStorage.setItem("username","visitor");
        }
        $scope.username = localStorage.getItem("username");
    });