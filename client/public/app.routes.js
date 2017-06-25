angular.module('app.routes',["ui.router"])
    .config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('home', {
            url: '/',
            templateUrl: '/templates/home.template.html',
            controller: 'HomeController'
        })

        .state('categories', {
            url: '/categories',
            templateUrl: '/templates/categories.template.html',
            controller: 'CategoryController'
        });

});

