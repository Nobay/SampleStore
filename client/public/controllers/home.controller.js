/**
 * Created by Nobay on 24/06/2017.
 */
retail
    .controller('HomeController', function($scope, $state, Category) {
        console.log(localStorage.getItem("user_token"))
        if(localStorage.getItem("user_token") === "")
        {
            $state.go('login');
        }
        else
        {

        }
    });