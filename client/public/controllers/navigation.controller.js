retail
    .controller('NavigationController', function($scope) {
        $scope.logged = (localStorage.getItem("user_token") !== "");
        console.log($scope.logged);
});