/**
 * Created by Nobay on 28/06/2017.
 */
retail
    .controller('LogoutController', function($scope, $state, Token) {
    if(localStorage.getItem("user_token") === "")
    {
        $state.go('home-content');
    }
    else
    {
        localStorage.setItem("user_token", "");
        $state.go('home-content');
    }


});