/**
 * Created by Nobay on 28/06/2017.
 */
retail
    .controller('RegisterController', function($scope, $state, Customer) {
    if(localStorage.getItem("user_token") === "")
    {
        $scope.customer = {
            "username":"",
            "password":"",
            "confirm_password":"",
            "first_name":"",
            "last_name":"",
            "email":"",
            "address":"",
	        "phone_number":""
        };

        $scope.register = function(){
            if($scope.customer.username !== "" && $scope.customer.password !== "" && $scope.customer.first_name !== ""
             && $scope.customer.last_name !== "" && $scope.customer.email !== "" && $scope.customer.address !== ""
            && $scope.customer.phone_number !== "")
            {
                Customer.save({username: $scope.customer.username, password: $scope.customer.password,
                    first_name: $scope.customer.first_name, last_name: $scope.customer.last_name,
                    email: $scope.customer.email, address: $scope.customer.address, phone_number: $scope.customer.phone_number})
                    .$promise.then(function(data){
                    console.log("Your registration was successful !");
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