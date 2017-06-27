/**
 * Created by Nobay on 26/06/2017.
 */
retail
    .controller('LoginController', function($scope, $state, Token) {
    if(localStorage.getItem("user_token") === "")
    {
        $scope.user = {
            "username":"",
            "password":""
        };

        $scope.register = function(){
            if($scope.user.username !== "" && $scope.user.password !== "")
            {
                console.log("helloooooo");
                Token.save({username: $scope.user.username, password: $scope.user.password}).$promise.then(function(data){
                    localStorage.setItem("user_token",data.token);
                    console.log(localStorage.getItem("user_token"));
                    $state.go('home-content');
                })
            }
        }
    }
    else
    {
        $state.go('home-content');
    }


});